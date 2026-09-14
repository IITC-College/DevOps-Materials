import { readdir, readFile, mkdir, writeFile } from "node:fs/promises";
import { join, dirname } from "node:path";
import { safePath } from "./files.js";
import { validatePublication, type LabDocument } from "../shared/catalog.js";
import type { LoadedLab } from "./lab-loader.js";
export async function bundleDocument(lab: LoadedLab): Promise<LabDocument> {
  const root = join(lab.directory, "starter"), starterFiles: Record<string, string> = {};
  async function walk(relative: string) {
    for (const entry of await readdir(join(root, relative), { withFileTypes: true })) {
      const path = relative ? `${relative}/${entry.name}` : entry.name;
      if (entry.isSymbolicLink()) throw new Error("Starter symlinks are not supported");
      if (entry.isDirectory()) await walk(path);
      else starterFiles[path] = await readFile(await safePath(root, path), "utf8");
    }
  }
  await walk("");
  return validatePublication({ definition: lab.definition, instructions: lab.instructions, starterFiles });
}
export async function materializeLab(input: LabDocument, directory: string): Promise<LoadedLab> {
  const document = validatePublication(input);
  const starter = join(directory, "starter");
  await mkdir(starter, { recursive: true });
  for (const [path, content] of Object.entries(document.starterFiles)) {
    const target = await safePath(starter, path, true);
    await mkdir(dirname(target), { recursive: true });
    await writeFile(target, content);
  }
  return { definition: document.definition, instructions: document.instructions, directory };
}
