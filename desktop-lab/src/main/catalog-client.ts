import { z } from "zod";
import { normalizeServerUrl, catalogSchema, publicationSchema, draftSaveSchema, type Draft, type Topic, type Library } from "../shared/catalog.js";
import { LocalStore } from "./local-store.js";
export class CatalogClient {
  private token?: string;
  private expiresAt = 0;
  syncError?: string;
  constructor(public store: LocalStore) {}
  get url() { return this.store.setting("serverUrl") ?? ""; }
  get admin() { return !!this.token && this.expiresAt > Date.now(); }
  configure(value: string) {
    const url = normalizeServerUrl(value);
    this.token = undefined; this.expiresAt = 0; this.syncError = undefined;
    this.store.setSetting("serverUrl", url);
  }
  private async request(path: string, method = "GET", body?: unknown, admin = false) {
    const url = this.url;
    if (!url) throw new Error("Set the lab server address first");
    if (admin && !this.admin) throw new Error("Admin login required");
    const response = await fetch(url + path, {
      method, headers: { "Content-Type": "application/json", ...(admin ? { Authorization: `Bearer ${this.token}` } : {}) },
      body: body === undefined ? undefined : JSON.stringify(body),
      signal: AbortSignal.timeout(15_000), redirect: "error",
    });
    if (Number(response.headers.get("content-length") ?? 0) > 10_000_000) { await response.body?.cancel(); throw new Error("Server response exceeds 10 MB"); }
    const reader = response.body?.getReader();
    if (!reader) throw new Error("Empty server response");
    const chunks: Uint8Array[] = []; let size = 0;
    while (true) {
      const chunk = await reader.read(); if (chunk.done) break;
      size += chunk.value.byteLength;
      if (size > 10_000_000) { await reader.cancel(); throw new Error("Server response exceeds 10 MB"); }
      chunks.push(chunk.value);
    }
    const data = JSON.parse(Buffer.concat(chunks).toString("utf8"));
    // Configuration changes cannot make an old server's response affect the new server.
    if (url !== this.url) throw new Error("Lab server changed; retry the request");
    if (!response.ok) {
      if (response.status === 401 && admin) { this.token = undefined; this.expiresAt = 0; }
      throw new Error(typeof data.error === "string" ? data.error : `Server returned ${response.status}`);
    }
    return data;
  }
  library(): Library { return { serverUrl: this.url, labs: this.store.library(), lastSynced: this.store.synced(this.url), syncError: this.syncError, admin: this.admin }; }
  async refresh() {
    try {
      const source = this.url;
      this.store.cacheCatalog(source, catalogSchema.parse(await this.request("/api/catalog")));
      this.syncError = undefined;
    } catch (error) { this.syncError = `Could not refresh labs: ${(error as Error).message}. Downloaded labs remain available.`; throw new Error(this.syncError); }
    return this.library();
  }
  async download(key: string) {
    const lab = this.store.library().find(l => l.key === key);
    if (!lab?.publishedVersion || lab.source !== this.url) throw new Error("Refresh this lab's server before downloading");
    const publication = publicationSchema.parse(await this.request(`/api/labs/${lab.id}/versions/${lab.publishedVersion}`));
    if (publication.labId !== lab.id || publication.number !== lab.publishedVersion) throw new Error("Downloaded version does not match the catalog");
    this.store.cachePublication(lab.source, publication);
    return this.library();
  }
  async login(password: string) {
    const result = z.object({ token: z.string().regex(/^[a-f0-9]{64}$/), expiresAt: z.number().int() }).strict().parse(await this.request("/api/admin/login", "POST", { password }));
    this.token = result.token; this.expiresAt = result.expiresAt;
  }
  async logout() { try { if (this.admin) await this.request("/api/admin/logout", "POST", undefined, true); } finally { this.token = undefined; this.expiresAt = 0; } }
  async adminCatalog() { return catalogSchema.parse(await this.request("/api/admin/catalog", "GET", undefined, true)); }
  async saveTopic(topic: Topic) { await this.request("/api/admin/topics", "PUT", topic, true); }
  async create(id: string, topicId: string) { return draftSaveSchema.parse(await this.request("/api/admin/labs", "POST", { id, topicId }, true)); }
  async duplicate(source: string, id: string) { return draftSaveSchema.parse(await this.request(`/api/admin/labs/${source}/duplicate`, "POST", { id }, true)); }
  async draft(id: string) { return draftSaveSchema.parse(await this.request(`/api/admin/labs/${id}/draft`, "GET", undefined, true)); }
  async saveDraft(draft: Draft) { return draftSaveSchema.parse(await this.request(`/api/admin/labs/${draft.labId}/draft`, "PUT", draft, true)); }
  async publish(id: string, revision: number) { return z.object({ number: z.number().int().positive() }).parse(await this.request(`/api/admin/labs/${id}/publish`, "POST", { revision }, true)).number; }
  async archive(id: string, archived: boolean) { await this.request(`/api/admin/labs/${id}/archive`, "POST", { archived }, true); }
}
