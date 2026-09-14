import type { DatabaseSync } from "node:sqlite";
import { createHash } from "node:crypto";
import { copyFile, readFile } from "node:fs/promises";
import { join, resolve } from "node:path";
import { z } from "zod";
import { openDatabase, transaction } from "./database.js";
import { Runtime, type Run } from "./runtime.js";
import { catalogSchema, publicationSchema, validatePublication, type Catalog, type Publication, type LibraryLab, type LabDocument } from "../shared/catalog.js";
import type { Progress } from "../shared/lab.js";
import type { Status } from "../shared/api.js";
export const labKey = (source: string, id: string) => `${source === "bundled" ? "bundled" : createHash("sha256").update(source).digest("hex").slice(0, 24)}:${id}`;
export interface Session {
  schemaVersion: 1; labVersion: string; labKey: string; version: number;
  run: Run; progress: Progress; status: Status;
}
const legacySessionSchema = z.object({
  schemaVersion: z.literal(1), labVersion: z.string(),
  run: z.object({ id: z.string().uuid(), profile: z.string(), network: z.string(), toolbox: z.string(), directory: z.string(), clusterUID: z.string().optional(), worker: z.string().optional(), controlPlane: z.string().optional() }).strict(),
  progress: z.object({ current: z.number().int().nonnegative(), checkpoints: z.record(z.string(), z.object({ passedAt: z.string(), podUID: z.string().min(1), results: z.array(z.object({ id: z.string(), label: z.string(), status: z.enum(["passed", "unmet", "error"]), expected: z.unknown(), observed: z.unknown(), message: z.string().optional() }).strict()) }).strict()) }).strict(),
  status: z.enum(["idle", "starting", "ready", "checking", "stopped", "resumable", "error", "completed"]),
}).strict();
const sessionSchema = legacySessionSchema.extend({ labKey: z.string(), version: z.number().int().positive() });
export class LocalStore {
  constructor(public db: DatabaseSync, public root: string) {}
  static async open(root: string) {
    return new LocalStore(await openDatabase(root, "labs.sqlite", `
      CREATE TABLE catalogs (source TEXT PRIMARY KEY, document TEXT NOT NULL, synced TEXT NOT NULL);
      CREATE TABLE downloads (lab_key TEXT NOT NULL, number INTEGER NOT NULL, source TEXT NOT NULL, document TEXT NOT NULL, PRIMARY KEY(lab_key,number));
      CREATE TABLE runs (lab_key TEXT PRIMARY KEY, number INTEGER NOT NULL, session TEXT NOT NULL, FOREIGN KEY(lab_key,number) REFERENCES downloads(lab_key,number));
      CREATE TABLE checkpoints (lab_key TEXT NOT NULL REFERENCES runs(lab_key) ON DELETE CASCADE, step_id TEXT NOT NULL, checkpoint TEXT NOT NULL, PRIMARY KEY(lab_key,step_id));
      CREATE TABLE settings (key TEXT PRIMARY KEY, value TEXT NOT NULL);
    `), root);
  }
  close() { this.db.close(); }
  setting(key: string): string | undefined { return (this.db.prepare("SELECT value FROM settings WHERE key=?").get(key) as any)?.value; }
  setSetting(key: string, value: string) { this.db.prepare("INSERT INTO settings VALUES (?,?) ON CONFLICT(key) DO UPDATE SET value=excluded.value").run(key, value); }
  seed(document: LabDocument) {
    if (this.setting("seeded")) return;
    transaction(this.db, () => {
      this.cachePublication("bundled", { labId: document.definition.id, number: 1, document });
      this.cacheCatalog("bundled", { topics: [{ id: "scheduling", title: "Scheduling", position: 0 }], labs: [{ id: document.definition.id, topicId: "scheduling", title: document.definition.title, description: document.definition.description, archived: false, publishedVersion: 1, total: document.definition.steps.length }] });
      this.setSetting("selected", labKey("bundled", document.definition.id));
      this.setSetting("seeded", "1");
    });
  }
  async migrateLegacy() {
    if (this.setting("legacyMigrated")) return;
    let raw: string;
    try { raw = await readFile(join(this.root, "session.json"), "utf8"); }
    catch (error) { if ((error as NodeJS.ErrnoException).code !== "ENOENT") throw error; this.setSetting("legacyMigrated", "1"); return; }
    const input = JSON.parse(raw);
    if (input === null) { this.setSetting("legacyMigrated", "1"); return; }
    const old = legacySessionSchema.parse(input), key = labKey("bundled", "manual-scheduling");
    const document = this.publication(key, 1).document;
    if (old.labVersion !== document.definition.version) throw new Error("Restore the matching bundled lab version before migrating this run");
    const session: Session = { ...old, labKey: key, version: 1 };
    this.validateSession(session);
    await copyFile(join(this.root, "session.json"), join(this.root, "session.json.backup"), 1).catch(error => { if (error.code !== "EEXIST") throw error; });
    transaction(this.db, () => {
      if (!this.session(key)) this.writeSession(session);
      this.setSetting("selected", key); this.setSetting("legacyMigrated", "1");
    });
  }
  cacheCatalog(source: string, input: Catalog) {
    const catalog = catalogSchema.parse(input);
    const topics = new Set(catalog.topics.map(t => t.id)), ids = new Set(catalog.labs.map(l => l.id));
    if (topics.size !== catalog.topics.length || ids.size !== catalog.labs.length || catalog.labs.some(l => !topics.has(l.topicId))) throw new Error("Server catalog has invalid topic or lab identities");
    this.db.prepare("INSERT INTO catalogs VALUES (?,?,?) ON CONFLICT(source) DO UPDATE SET document=excluded.document,synced=excluded.synced").run(source, JSON.stringify(catalog), new Date().toISOString());
  }
  synced(source: string): string | undefined { return (this.db.prepare("SELECT synced FROM catalogs WHERE source=?").get(source) as any)?.synced; }
  cachePublication(source: string, input: Publication) {
    const publication = publicationSchema.parse(input);
    publication.document = validatePublication(publication.document);
    if (publication.document.definition.id !== publication.labId) throw new Error("Downloaded lab identity mismatch");
    const key = labKey(source, publication.labId), json = JSON.stringify(publication);
    const existing = this.db.prepare("SELECT document FROM downloads WHERE lab_key=? AND number=?").get(key, publication.number) as any;
    if (existing && existing.document !== json) throw new Error("Server changed an immutable version; cached content was preserved");
    if (!existing) this.db.prepare("INSERT INTO downloads VALUES (?,?,?,?)").run(key, publication.number, source, json);
  }
  publication(key: string, number?: number): Publication {
    const row = (number === undefined ? this.db.prepare("SELECT document FROM downloads WHERE lab_key=? ORDER BY number DESC LIMIT 1").get(key) : this.db.prepare("SELECT document FROM downloads WHERE lab_key=? AND number=?").get(key, number)) as any;
    if (!row) throw new Error("Download this lab before starting it");
    const publication = publicationSchema.parse(JSON.parse(row.document));
    publication.document = validatePublication(publication.document);
    return publication;
  }
  validateSession(input: Session) {
    const session = sessionSchema.parse(input), doc = this.publication(session.labKey, session.version).document;
    if (session.labVersion !== doc.definition.version) throw new Error("Saved lab version mismatch");
    if (resolve(session.run.directory) !== resolve(this.root, "runs", session.run.id)) throw new Error("Saved run directory does not match its identity");
    new Runtime(session.run, doc.definition.runtime);
    const ids = doc.definition.steps.map(s => s.id);
    if (session.progress.current >= ids.length || Object.keys(session.progress.checkpoints).some(id => !ids.includes(id)) || ids.slice(0, session.progress.current).some(id => !session.progress.checkpoints[id])) throw new Error("Saved checkpoints do not match the lab");
  }
  session(key: string): Session | undefined {
    const row = this.db.prepare("SELECT session FROM runs WHERE lab_key=?").get(key) as any;
    if (!row) return;
    const session = sessionSchema.parse(JSON.parse(row.session));
    if (session.labKey !== key) throw new Error("Saved run belongs to another lab");
    this.validateSession(session);
    return session;
  }
  private writeSession(session: Session) {
    this.db.prepare("INSERT INTO runs VALUES (?,?,?) ON CONFLICT(lab_key) DO UPDATE SET number=excluded.number, session=excluded.session").run(session.labKey, session.version, JSON.stringify(session));
    this.db.prepare("DELETE FROM checkpoints WHERE lab_key=?").run(session.labKey);
    for (const [id, checkpoint] of Object.entries(session.progress.checkpoints)) this.db.prepare("INSERT INTO checkpoints VALUES (?,?,?)").run(session.labKey, id, JSON.stringify(checkpoint));
  }
  saveSession(key: string, session?: Session) {
    if (session) { if (session.labKey !== key) throw new Error("Run identity mismatch"); this.validateSession(session); }
    transaction(this.db, () => {
      if (session) this.writeSession(session);
      else this.db.prepare("DELETE FROM runs WHERE lab_key=?").run(key);
    });
  }
  library(): LibraryLab[] {
    const labs = new Map<string, LibraryLab>();
    for (const row of this.db.prepare("SELECT * FROM catalogs ORDER BY source").all() as any[]) {
      const catalog = catalogSchema.parse(JSON.parse(row.document));
      for (const lab of catalog.labs) {
        const key = labKey(row.source, lab.id);
        labs.set(key, { ...lab, key, source: row.source, topic: catalog.topics.find(t => t.id === lab.topicId)!.title, completed: 0, hasRun: false });
      }
    }
    for (const row of this.db.prepare("SELECT lab_key,MAX(number) AS number,source FROM downloads GROUP BY lab_key").all() as any[]) {
      const publication = this.publication(row.lab_key, row.number), doc = publication.document.definition;
      const lab = labs.get(row.lab_key) ?? { id: publication.labId, key: row.lab_key, source: row.source, topic: "Downloaded", topicId: "downloaded", title: doc.title, description: doc.description, archived: true, total: doc.steps.length, completed: 0, hasRun: false };
      lab.downloadedVersion = row.number;
      const session = this.session(row.lab_key);
      if (session) { lab.hasRun = true; lab.runVersion = session.version; lab.completed = Object.keys(session.progress.checkpoints).length; lab.total = this.publication(row.lab_key, session.version).document.definition.steps.length; }
      labs.set(row.lab_key, lab);
    }
    return [...labs.values()];
  }
}
