import { DatabaseSync } from "node:sqlite";
import { mkdir, chmod } from "node:fs/promises";
import { join } from "node:path";
export function transaction<T>(db: DatabaseSync, fn: () => T): T {
  db.exec("BEGIN IMMEDIATE");
  try { const result = fn(); db.exec("COMMIT"); return result; }
  catch (error) { db.exec("ROLLBACK"); throw error; }
}
export async function openDatabase(root: string, name: string, schema: string) {
  await mkdir(root, { recursive: true, mode: 0o700 });
  const path = join(root, name), db = new DatabaseSync(path);
  try {
    await chmod(path, 0o600);
    db.exec("PRAGMA foreign_keys=ON; PRAGMA journal_mode=WAL; PRAGMA busy_timeout=5000;");
    const version = (db.prepare("PRAGMA user_version").get() as { user_version: number }).user_version;
    if (version > 1) throw new Error("This database requires a newer application");
    if (!version) transaction(db, () => db.exec(schema + "\nPRAGMA user_version=1;"));
    return db;
  } catch (error) { db.close(); throw error; }
}
