import {
  readFile,
  writeFile,
  mkdir,
  readdir,
  lstat,
  realpath,
  rename,
} from "node:fs/promises";
import { resolve, relative, dirname, join, sep } from "node:path";
import { createHash, randomUUID } from "node:crypto";

export async function safePath(
  root: string,
  path: string,
  allowNew = false,
): Promise<string> {
  if (
    !path ||
    path.includes("\0") ||
    path.startsWith("/") ||
    path.split(/[\\/]/).includes("..")
  )
    throw new Error("Invalid workspace path");
  const base = await realpath(root);
  const target = resolve(base, path);
  if (!target.startsWith(base + sep)) throw new Error("Path escapes workspace");
  let part = base;
  for (const segment of relative(base, target).split(sep)) {
    part = join(part, segment);
    try {
      if ((await lstat(part)).isSymbolicLink())
        throw new Error("Symbolic links are not allowed in lab files");
    } catch (error) {
      if ((error as NodeJS.ErrnoException).code === "ENOENT" && allowNew) break;
      throw error;
    }
  }
  return target;
}
export const revision = (text: string) =>
  createHash("sha256").update(text).digest("hex");
export async function readWorkspace(root: string, path: string) {
  const target = await safePath(root, path);
  const stat = await lstat(target);
  if (!stat.isFile() || stat.size > 2_000_000)
    throw new Error("Choose a text file smaller than 2 MB");
  const content = await readFile(target, "utf8");
  return { path, content, revision: revision(content) };
}
export async function saveWorkspace(
  root: string,
  path: string,
  content: string,
  expected: string | null,
) {
  if (Buffer.byteLength(content) > 2_000_000)
    throw new Error("File exceeds 2 MB");
  const target = await safePath(root, path, true);
  let current: string | null = null;
  try {
    current = revision(await readFile(target, "utf8"));
  } catch (e) {
    if ((e as NodeJS.ErrnoException).code !== "ENOENT") throw e;
  }
  if (current !== expected)
    throw new Error(
      "FILE_CONFLICT: This file changed outside the editor. Reload it before saving.",
    );
  await mkdir(dirname(target), { recursive: true });
  await writeFile(target, content);
  return { path, content, revision: revision(content) };
}
export async function listWorkspace(root: string): Promise<string[]> {
  const result: string[] = [];
  async function walk(dir: string, depth: number) {
    if (depth > 5 || result.length > 200) return;
    for (const entry of await readdir(dir, { withFileTypes: true })) {
      if (entry.isSymbolicLink() || entry.name.startsWith(".")) continue;
      const path = join(dir, entry.name);
      if (entry.isDirectory()) await walk(path, depth + 1);
      else if (entry.isFile()) result.push(relative(root, path));
    }
  }
  await walk(root, 0);
  return result.sort();
}
export async function atomicJSON(path: string, value: unknown) {
  await mkdir(dirname(path), { recursive: true, mode: 0o700 });
  const tmp = `${path}.${randomUUID()}.tmp`;
  await writeFile(tmp, JSON.stringify(value, null, 2), { mode: 0o600 });
  await rename(tmp, path);
}
