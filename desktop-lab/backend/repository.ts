import { DatabaseSync } from "node:sqlite";
import { openDatabase, transaction } from "../src/main/database.js";
import { documentSchema, validatePublication, type LabDocument, type Catalog, type Draft, type Topic } from "../src/shared/catalog.js";

export class CatalogRepository {
  constructor(public db: DatabaseSync) {}
  static async open(root: string, template: LabDocument) {
    const db = await openDatabase(root, "catalog.sqlite", `
      CREATE TABLE topics (id TEXT PRIMARY KEY, title TEXT NOT NULL, position INTEGER NOT NULL);
      CREATE TABLE labs (id TEXT PRIMARY KEY, topic_id TEXT NOT NULL REFERENCES topics(id), archived INTEGER NOT NULL DEFAULT 0);
      CREATE TABLE drafts (lab_id TEXT PRIMARY KEY REFERENCES labs(id), revision INTEGER NOT NULL, document TEXT NOT NULL);
      CREATE TABLE versions (id INTEGER PRIMARY KEY, lab_id TEXT NOT NULL REFERENCES labs(id), number INTEGER NOT NULL, document TEXT NOT NULL, UNIQUE(lab_id, number));
      CREATE TABLE settings (key TEXT PRIMARY KEY, value TEXT NOT NULL);
      CREATE TRIGGER immutable_versions_update BEFORE UPDATE ON versions BEGIN SELECT RAISE(ABORT, 'Published versions are immutable'); END;
      CREATE TRIGGER immutable_versions_delete BEFORE DELETE ON versions BEGIN SELECT RAISE(ABORT, 'Published versions are immutable'); END;
    `);
    const repo = new CatalogRepository(db);
    if (!db.prepare("SELECT value FROM settings WHERE key='seeded'").get()) repo.transaction(() => {
      const doc = validatePublication(template);
      repo.saveTopic({ id: "scheduling", title: "Scheduling", position: 0 });
      repo.insertLab(doc.definition.id, "scheduling", doc);
      repo.publishUnchecked(doc.definition.id, doc);
      db.prepare("INSERT INTO settings VALUES ('seeded','1')").run();
    });
    return repo;
  }
  close() { this.db.close(); }
  transaction<T>(fn: () => T) { return transaction(this.db, fn); }
  saveTopic(topic: Topic) {
    this.db.prepare("INSERT INTO topics VALUES (?,?,?) ON CONFLICT(id) DO UPDATE SET title=excluded.title, position=excluded.position").run(topic.id, topic.title, topic.position);
  }
  private insertLab(id: string, topicId: string, document: LabDocument) {
    this.db.prepare("INSERT INTO labs(id,topic_id) VALUES (?,?)").run(id, topicId);
    this.db.prepare("INSERT INTO drafts VALUES (?,1,?)").run(id, JSON.stringify(document));
  }
  create(id: string, topicId: string, template: LabDocument) {
    const doc = structuredClone(template);
    doc.definition.id = id; doc.definition.title = "Untitled lab"; doc.definition.version = "1";
    this.transaction(() => this.insertLab(id, topicId, doc));
    return this.draft(id);
  }
  duplicate(source: string, id: string) {
    const draft = this.draft(source);
    const doc = structuredClone(draft.document);
    doc.definition.id = id; doc.definition.title += " (copy)"; doc.definition.version = "1";
    this.transaction(() => this.insertLab(id, draft.topicId, doc));
    return this.draft(id);
  }
  draft(id: string): Draft {
    const row = this.db.prepare("SELECT d.*, l.topic_id FROM drafts d JOIN labs l ON l.id=d.lab_id WHERE d.lab_id=?").get(id) as any;
    if (!row) throw new Error("Lab not found");
    return { labId: id, topicId: row.topic_id, revision: row.revision, document: documentSchema.parse(JSON.parse(row.document)) };
  }
  saveDraft(draft: Draft): Draft {
    const doc = documentSchema.parse(draft.document);
    if (doc.definition.id !== draft.labId) throw new Error("Lab identity cannot change");
    this.transaction(() => {
      const result = this.db.prepare("UPDATE drafts SET document=?, revision=revision+1 WHERE lab_id=? AND revision=?").run(JSON.stringify(doc), draft.labId, draft.revision);
      if (!result.changes) throw new Error("DRAFT_CONFLICT: Reload the draft before saving");
      this.db.prepare("UPDATE labs SET topic_id=? WHERE id=?").run(draft.topicId, draft.labId);
    });
    return this.draft(draft.labId);
  }
  private publishUnchecked(id: string, document: LabDocument) {
    const number = (this.latest(id)?.number ?? 0) + 1;
    // Database revision is separate from the original bundle version for legacy migration.
    this.db.prepare("INSERT INTO versions(lab_id,number,document) VALUES (?,?,?)").run(id, number, JSON.stringify(document));
    return number;
  }
  publish(id: string, revision: number) {
    return this.transaction(() => {
      const draft = this.draft(id);
      if (draft.revision !== revision) throw new Error("DRAFT_CONFLICT: Reload the draft before publishing");
      if ((this.db.prepare("SELECT archived FROM labs WHERE id=?").get(id) as any).archived) throw new Error("Restore the lab before publishing");
      return this.publishUnchecked(id, validatePublication(draft.document));
    });
  }
  archive(id: string, archived: boolean) {
    if (!this.db.prepare("UPDATE labs SET archived=? WHERE id=?").run(Number(archived), id).changes) throw new Error("Lab not found");
  }
  latest(id: string) {
    const row = this.db.prepare("SELECT * FROM versions WHERE lab_id=? ORDER BY number DESC LIMIT 1").get(id) as any;
    return row ? { id: row.id as number, number: row.number as number, document: validatePublication(JSON.parse(row.document)) } : undefined;
  }
  version(id: number) {
    const row = this.db.prepare("SELECT * FROM versions WHERE id=?").get(id) as any;
    if (!row) throw new Error("Published version not found");
    return { id: row.id as number, number: row.number as number, document: validatePublication(JSON.parse(row.document)) };
  }
  publication(labId: string, number: number) {
    const row = this.db.prepare("SELECT v.document FROM versions v JOIN labs l ON l.id=v.lab_id WHERE v.lab_id=? AND v.number=? AND l.archived=0").get(labId, number) as { document: string } | undefined;
    if (!row) throw new Error("Published lab not found");
    return { labId, number, document: validatePublication(JSON.parse(row.document)) };
  }
  catalog(admin = false): Catalog {
    const topics = this.db.prepare("SELECT * FROM topics ORDER BY position,title,id").all() as unknown as Topic[];
    const labs = (this.db.prepare("SELECT * FROM labs ORDER BY id").all() as any[]).flatMap(row => {
      const latest = this.latest(row.id);
      if (!admin && (row.archived || !latest)) return [];
      const doc = admin ? this.draft(row.id).document : latest!.document;
      return [{ id: row.id, title: doc.definition.title, description: doc.definition.description,
        topicId: row.topic_id, archived: !!row.archived, publishedVersion: latest?.number,
        total: doc.definition.steps.length }];
    });
    return { topics, labs };
  }
}
