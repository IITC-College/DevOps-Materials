import {
  test,
  expect,
  _electron as electron,
  type ElectronApplication,
  type Page,
} from "@playwright/test";
import { mkdtemp, readFile, writeFile, rm } from "node:fs/promises";
import { join, resolve } from "node:path";
import { tmpdir } from "node:os";
let application: ElectronApplication, page: Page, root: string;
test.beforeEach(async () => {
  root = await mkdtemp(join(tmpdir(), "klab-ui-"));
  const env: Record<string, string> = {
    ...(process.env as Record<string, string>),
    KLAB_FAKE: "1",
    KLAB_DATA_DIR: root,
  };
  delete env.ELECTRON_RUN_AS_NODE;
  application = await electron.launch({ args: [resolve(".")], env });
  page = await application.firstWindow();
  page.on("console", (message) => {
    if (message.type() === "error") console.log("renderer:", message.text());
  });
});
test.afterEach(async () => {
  await application?.close();
  await rm(root, { recursive: true, force: true });
});
test("terminal, shared editor, failed check and passed checkpoint gating", async () => {
  await expect(
    page.getByRole("heading", { name: "Manual scheduling", exact: true }),
  ).toBeVisible();
  await expect(
    page.getByRole("button", { name: "Next →", exact: true }),
  ).toBeDisabled();
  await page.getByRole("button", { name: "Start lab", exact: true }).click();
  await expect(
    page.getByRole("button", { name: "Check", exact: true }),
  ).toBeEnabled();
  await expect(page.locator(".monaco-editor")).toBeVisible();
  await page.getByRole("button", { name: "Check", exact: true }).click();
  await expect(
    page.getByText("Pod default/nginx exists", { exact: true }),
  ).toBeVisible();
  await expect(
    page.getByRole("button", { name: "Next →", exact: true }),
  ).toBeDisabled();
  await page.getByRole("button", { name: "Cancel check", exact: true }).click();
  await page.evaluate(() =>
    window.lab.terminalWrite("printf terminal-proof > shared.txt\r"),
  );
  const session = JSON.parse(
    await readFile(join(root, "session.json"), "utf8"),
  );
  await expect
    .poll(async () =>
      readFile(
        join(session.run.directory, "workspace/shared.txt"),
        "utf8",
      ).catch(() => ""),
    )
    .toBe("terminal-proof");
  await page.evaluate(() => window.lab.terminalResize(90, 20));
  await page.evaluate(() => {
    (window as any).terminalOutput = "";
    window.lab.onTerminal((text) => ((window as any).terminalOutput += text));
  });
  await page.evaluate(() =>
    window.lab.terminalWrite("printf started > sleeping.txt; sleep 30\r"),
  );
  await expect
    .poll(async () =>
      readFile(
        join(session.run.directory, "workspace/sleeping.txt"),
        "utf8",
      ).catch(() => ""),
    )
    .toBe("started");
  await page.evaluate(() => {
    (window as any).terminalOutput = "";
    return window.lab.terminalWrite("\x03");
  });
  await expect
    .poll(() => page.evaluate(() => (window as any).terminalOutput))
    .toContain("lab");
  await page.evaluate(() =>
    window.lab.terminalWrite("printf interrupted > interrupt.txt\r"),
  );
  await expect
    .poll(async () =>
      readFile(
        join(session.run.directory, "workspace/interrupt.txt"),
        "utf8",
      ).catch(() => ""),
    )
    .toBe("interrupted");
  const state = await page.evaluate(() => window.lab.snapshot());
  const pod = {
    kind: "Pod",
    metadata: { name: "nginx", namespace: "default", uid: "pod-1" },
    spec: {
      containers: [{ name: "nginx", image: state.lab.runtime.nginxImage }],
    },
    status: { phase: "Pending" },
  };
  await writeFile(
    join(session.run.directory, "workspace/.test-pod.json"),
    JSON.stringify(pod),
  );
  await page.getByRole("button", { name: "Check", exact: true }).click();
  await expect(
    page.getByRole("button", { name: "Next →", exact: true }),
  ).toBeEnabled();
  await page.screenshot({ path: "test-results/workspace-passed.png" });
  await page.getByRole("button", { name: "Next →", exact: true }).click();
  await expect(
    page.getByRole("heading", { name: "Capture diagnostics", exact: true }),
  ).toBeVisible();
  await expect(
    page.getByRole("button", { name: "Next →", exact: true }),
  ).toBeDisabled();
  await expect(page.getByText("1 / 4 complete", { exact: true })).toBeVisible();
});
test("editor saves and rejects conflicting terminal changes", async () => {
  await page.getByRole("button", { name: "Start lab", exact: true }).click();
  await expect(page.locator(".monaco-editor")).toBeVisible();
  const editor = page.getByRole("textbox", {
    name: "Editor content",
    exact: true,
  });
  await editor.focus();
  await page.keyboard.press("Meta+End");
  await page.keyboard.type("\n# editor change");
  await page.getByRole("button", { name: "Save •", exact: true }).click();
  const session = JSON.parse(
    await readFile(join(root, "session.json"), "utf8"),
  );
  const path = join(session.run.directory, "workspace/nginx.yaml");
  await expect.poll(() => readFile(path, "utf8")).toContain("# editor change");
  await editor.focus();
  await page.keyboard.press("Meta+End");
  await page.keyboard.type("\n# unsaved");
  await writeFile(path, "# terminal change\n");
  await expect(
    page.getByRole("button", { name: "Reload file", exact: true }),
  ).toBeVisible();
  await expect(
    page.getByRole("button", { name: "Save •", exact: true }),
  ).toBeDisabled();
  page.once("dialog", (dialog) => dialog.accept());
  await page.getByRole("button", { name: "Reload file", exact: true }).click();
  await expect(
    page.getByText("Unsaved changes", { exact: true }),
  ).not.toBeVisible();
});
test("reset requires confirmation and restores a fresh run", async () => {
  await page.getByRole("button", { name: "Start lab", exact: true }).click();
  await expect(
    page.getByRole("button", { name: "Check", exact: true }),
  ).toBeEnabled();
  const first = await page.evaluate(() => window.lab.snapshot());
  await application.evaluate(({ dialog }) => {
    dialog.showMessageBox = async () => ({
      response: 0,
      checkboxChecked: false,
    });
  });
  await page.getByRole("button", { name: "Reset Lab", exact: true }).click();
  expect((await page.evaluate(() => window.lab.snapshot())).runId).toBe(
    first.runId,
  );
  await application.evaluate(({ dialog }) => {
    dialog.showMessageBox = async () => ({
      response: 1,
      checkboxChecked: false,
    });
  });
  await page.getByRole("button", { name: "Reset Lab", exact: true }).click();
  await expect
    .poll(async () => (await page.evaluate(() => window.lab.snapshot())).runId)
    .not.toBe(first.runId);
  await expect(
    page.getByRole("button", { name: "Check", exact: true }),
  ).toBeEnabled();
  await expect(
    page.getByRole("button", { name: "Next →", exact: true }),
  ).toBeDisabled();
  expect(
    (await page.evaluate(() => window.lab.snapshot())).progress.checkpoints,
  ).toEqual({});
});
