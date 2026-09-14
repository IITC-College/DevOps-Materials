import { createServer, type IncomingMessage, type ServerResponse } from "node:http";
import { randomBytes, scryptSync, timingSafeEqual } from "node:crypto";
import { z } from "zod";
import { CatalogRepository } from "./repository.js";
import { idSchema, topicSchema, draftSaveSchema, type LabDocument } from "../src/shared/catalog.js";

class HttpError extends Error { constructor(public status: number, message: string) { super(message); } }
async function body(req: IncomingMessage) {
  if (!req.headers["content-type"]?.startsWith("application/json")) throw new HttpError(415, "Send application/json");
  const chunks: Buffer[] = []; let size = 0;
  for await (const chunk of req) {
    size += chunk.length;
    if (size > 10_000_000) throw new HttpError(413, "Request exceeds 10 MB");
    chunks.push(Buffer.from(chunk));
  }
  try { return JSON.parse(Buffer.concat(chunks).toString("utf8")); }
  catch { throw new HttpError(400, "Invalid JSON"); }
}
function send(res: ServerResponse, value: unknown, status = 200) {
  res.writeHead(status, { "Content-Type": "application/json; charset=utf-8", "Cache-Control": "no-store", "X-Content-Type-Options": "nosniff" });
  res.end(JSON.stringify(value));
}
export async function createCatalogServer(options: { root: string; adminPassword: string; template: LabDocument }) {
  if (options.adminPassword.length < 16) throw new Error("KLAB_ADMIN_PASSWORD must be at least 16 characters");
  const repository = await CatalogRepository.open(options.root, options.template);
  const salt = randomBytes(16), passwordHash = scryptSync(options.adminPassword, salt, 32);
  const sessions = new Map<string, number>();
  const attempts = new Map<string, { count: number; until: number }>();
  const sweep = () => {
    for (const [key, expires] of sessions) if (expires < Date.now()) sessions.delete(key);
    for (const [key, attempt] of attempts) if (attempt.until < Date.now()) attempts.delete(key);
  };
  const server = createServer({ requestTimeout: 30_000, headersTimeout: 15_000, maxHeaderSize: 16384 }, (req, res) => {
    void (async () => {
      const path = new URL(req.url ?? "/", "http://localhost").pathname;
      const method = req.method;
      if (method === "GET" && path === "/health") return send(res, { status: "ok" });
      if (method === "GET" && path === "/api/catalog") return send(res, repository.catalog());
      const published = /^\/api\/labs\/([a-z0-9-]+)\/versions\/([1-9][0-9]*)$/.exec(path);
      if (method === "GET" && published) {
        const number = z.coerce.number().int().positive().safe().parse(published[2]);
        return send(res, repository.publication(idSchema.parse(published[1]), number));
      }
      if (method === "POST" && path === "/api/admin/login") {
        sweep();
        const address = req.socket.remoteAddress ?? "unknown";
        // Do not trust X-Forwarded-For supplied by arbitrary clients.
        const attempt = attempts.get(address) ?? { count: 0, until: Date.now() + 60_000 };
        if (attempt.count >= 10 || attempts.size >= 10000) throw new HttpError(429, "Too many login attempts; try again in a minute");
        attempt.count++; attempts.set(address, attempt);
        const input = z.object({ password: z.string().max(1000) }).strict().parse(await body(req));
        if (!timingSafeEqual(passwordHash, scryptSync(input.password, salt, 32))) throw new HttpError(401, "Invalid admin password");
        const token = randomBytes(32).toString("hex"), expiresAt = Date.now() + 8 * 60 * 60 * 1000;
        if (sessions.size >= 1000) throw new HttpError(429, "Too many active sessions");
        sessions.set(token, expiresAt);
        return send(res, { token, expiresAt });
      }
      if (!path.startsWith("/api/admin/")) throw new HttpError(404, "Endpoint not found");
      const token = req.headers.authorization?.replace(/^Bearer /, "") ?? "";
      if ((sessions.get(token) ?? 0) <= Date.now()) { sessions.delete(token); throw new HttpError(401, "Admin login required"); }
      if (method === "POST" && path === "/api/admin/logout") { sessions.delete(token); return send(res, { ok: true }); }
      if (method === "GET" && path === "/api/admin/catalog") return send(res, repository.catalog(true));
      if (method === "PUT" && path === "/api/admin/topics") {
        repository.saveTopic(topicSchema.parse(await body(req))); return send(res, { ok: true });
      }
      if (method === "POST" && path === "/api/admin/labs") {
        const input = z.object({ id: idSchema, topicId: idSchema }).strict().parse(await body(req));
        return send(res, repository.create(input.id, input.topicId, options.template), 201);
      }
      const match = /^\/api\/admin\/labs\/([a-z0-9-]+)\/(draft|publish|archive|duplicate)$/.exec(path);
      if (match) {
        const id = idSchema.parse(match[1]), action = match[2];
        if (method === "GET" && action === "draft") return send(res, repository.draft(id));
        if (method === "PUT" && action === "draft") {
          const draft = draftSaveSchema.parse(await body(req));
          if (draft.labId !== id) throw new HttpError(400, "Lab identity mismatch");
          return send(res, repository.saveDraft(draft));
        }
        if (method === "POST" && action === "publish") {
          const { revision } = z.object({ revision: z.number().int().positive() }).strict().parse(await body(req));
          return send(res, { number: repository.publish(id, revision) }, 201);
        }
        if (method === "POST" && action === "archive") {
          const { archived } = z.object({ archived: z.boolean() }).strict().parse(await body(req));
          repository.archive(id, archived); return send(res, { ok: true });
        }
        if (method === "POST" && action === "duplicate") {
          const input = z.object({ id: idSchema }).strict().parse(await body(req));
          return send(res, repository.duplicate(id, input.id), 201);
        }
      }
      throw new HttpError(404, "Endpoint not found");
    })().catch(error => {
      if (res.headersSent || res.destroyed) return;
      if (error instanceof HttpError) return send(res, { error: error.message }, error.status);
      if (error instanceof z.ZodError) return send(res, { error: error.issues.map(i => `${i.path.join(".")}: ${i.message}`).join("; ") }, 400);
      const message = error instanceof Error ? error.message : "Request failed";
      if (/not found/i.test(message)) return send(res, { error: message }, 404);
      if (/DRAFT_CONFLICT/.test(message)) return send(res, { error: message }, 409);
      if (/UNIQUE constraint/.test(message)) return send(res, { error: "That lab ID already exists" }, 409);
      if (/FOREIGN KEY constraint/.test(message)) return send(res, { error: "Choose an existing topic" }, 400);
      if (/required|needs a|before publishing|identity|cannot|Restore the lab/.test(message)) return send(res, { error: message }, 400);
      console.error("Catalog request failed:", message);
      send(res, { error: "The server could not complete this request" }, 500);
    });
  });
  server.on("close", () => repository.close());
  return { server, repository };
}
