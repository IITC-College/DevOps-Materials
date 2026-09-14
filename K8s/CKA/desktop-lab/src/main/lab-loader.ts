import { readFile } from "node:fs/promises";
import { join } from "node:path";
import { parse } from "yaml";
import { labSchema, type Lab } from "../shared/lab.js";
import { safePath } from "./files.js";
export interface LoadedLab {
  definition: Lab;
  instructions: Record<string, string>;
  directory: string;
}
export async function loadLab(directory: string): Promise<LoadedLab> {
  const definition = labSchema.parse(
    parse(await readFile(join(directory, "lab.yaml"), "utf8"), {
      maxAliasCount: 100,
    }),
  );
  const instructions: Record<string, string> = {};
  for (const step of definition.steps)
    instructions[step.id] = await readFile(
      await safePath(directory, step.instructions),
      "utf8",
    );
  return { definition, instructions, directory };
}
