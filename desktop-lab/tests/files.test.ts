import { beforeEach, afterEach, it, expect } from "vitest";
import { mkdtemp, writeFile, symlink, rm } from "node:fs/promises";
import { join } from "node:path";
import { tmpdir } from "node:os";
import {
  readWorkspace,
  saveWorkspace,
  listWorkspace,
  atomicJSON,
} from "../src/main/files.js";
let root: string;
beforeEach(async () => {
  root = await mkdtemp(join(tmpdir(), "klab-files-"));
  await writeFile(join(root, "nginx.yaml"), "original");
});
afterEach(() => rm(root, { recursive: true, force: true }));
it("saves files and detects edits from the terminal", async () => {
  const original = await readWorkspace(root, "nginx.yaml");
  await writeFile(join(root, "nginx.yaml"), "terminal change");
  await expect(
    saveWorkspace(root, "nginx.yaml", "editor change", original.revision),
  ).rejects.toThrow("FILE_CONFLICT");
  const current = await readWorkspace(root, "nginx.yaml");
  const saved = await saveWorkspace(
    root,
    "nginx.yaml",
    "new",
    current.revision,
  );
  expect(saved.content).toBe("new");
});
it("rejects traversal and symlinks", async () => {
  await expect(readWorkspace(root, "../private")).rejects.toThrow();
  await symlink("/etc/hosts", join(root, "link"));
  await expect(readWorkspace(root, "link")).rejects.toThrow("Symbolic");
  expect(await listWorkspace(root)).toEqual(["nginx.yaml"]);
});
it("creates new files without overwriting existing ones", async () => {
  await saveWorkspace(root, "diagnostics/pod.json", "{}", null);
  await expect(saveWorkspace(root, "nginx.yaml", "bad", null)).rejects.toThrow(
    "FILE_CONFLICT",
  );
  expect(await listWorkspace(root)).toEqual([
    "diagnostics/pod.json",
    "nginx.yaml",
  ]);
});
it("atomically saves JSON with a readable final state", async () => {
  await atomicJSON(join(root, "state.json"), { passed: true });
  expect(JSON.parse((await readWorkspace(root, "state.json")).content)).toEqual(
    { passed: true },
  );
});
