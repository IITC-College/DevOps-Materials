import { _electron as electron, expect } from "@playwright/test";
import { resolve, join } from "node:path";
import { readFile, writeFile, mkdir } from "node:fs/promises";
import assert from "node:assert/strict";
const root = resolve(".state/integration");
const env: Record<string, string> = {
  ...(process.env as Record<string, string>),
  KLAB_DATA_DIR: root,
};
delete env.ELECTRON_RUN_AS_NODE;
delete env.KLAB_FAKE;
const application = await electron.launch({
  executablePath: resolve(
    "release/mac-arm64/Kubernetes Lab.app/Contents/MacOS/Kubernetes Lab",
  ),
  env,
  timeout: 60_000,
});
try {
  const page = await application.firstWindow();
  await expect(
    page.getByRole("heading", { name: "Manual scheduling", exact: true }),
  ).toBeVisible();
  await page.getByRole("button", { name: "Resume", exact: true }).click();
  await expect(
    page.getByRole("button", { name: "Check", exact: true }),
  ).toBeEnabled({ timeout: 180_000 });
  await expect(page.locator(".monaco-editor")).toBeVisible();
  await page.evaluate(() => window.lab.terminalOpen());
  const state = await page.evaluate(() => window.lab.snapshot());
  const session = JSON.parse(
    await readFile(join(root, "session.json"), "utf8"),
  );
  await page.evaluate(() =>
    window.lab.terminalWrite("printf packaged-terminal > terminal-proof.txt\r"),
  );
  await expect
    .poll(
      () =>
        readFile(
          join(session.run.directory, "workspace/terminal-proof.txt"),
          "utf8",
        ).catch(() => ""),
      { timeout: 10_000 },
    )
    .toBe("packaged-terminal");
  console.log(
    "PASS: packaged app launches its native terminal inside the real toolbox",
  );
  const terminal = async (text: string) =>
    page.evaluate((text) => window.lab.terminalWrite(text + "\r"), text);
  const check = async (step: number) => {
    await page.getByRole("button", { name: "Check", exact: true }).click();
    await expect(
      page.getByText(`${step} / 4 complete`, { exact: true }),
    ).toBeVisible({ timeout: 90_000 });
    console.log(`PASS: packaged app validates real step ${step}`);
    if (step < 4)
      await page.getByRole("button", { name: "Next →", exact: true }).click();
  };
  await terminal("kubectl create -f nginx.yaml");
  await check(1);
  await terminal(
    "kubectl get pod nginx -n default -o json > diagnostics/pod.json && kubectl get pods -n kube-system -o json > diagnostics/system-pods.json",
  );
  await check(2);
  for (const [index, node] of [
    state.variables.worker,
    state.variables.controlPlane,
  ].entries()) {
    const file = await page.evaluate(() => window.lab.readFile("nginx.yaml"));
    const pod = {
      apiVersion: "v1",
      kind: "Pod",
      metadata: { name: "nginx", namespace: "default" },
      spec: {
        nodeName: node,
        containers: [
          {
            name: "nginx",
            image: state.lab.runtime.nginxImage,
            imagePullPolicy: "IfNotPresent",
          },
        ],
      },
    };
    await page.evaluate(
      ({ content, revision }) =>
        window.lab.saveFile("nginx.yaml", content, revision),
      { content: JSON.stringify(pod, null, 2), revision: file.revision },
    );
    await terminal(
      "kubectl delete pod nginx --wait=true --grace-period=1 && kubectl create -f nginx.yaml",
    );
    await check(index + 3);
  }
  await expect(
    page.getByText("Lab complete. All four checkpoints passed.", {
      exact: true,
    }),
  ).toBeVisible();
  await page.locator(".lesson").evaluate((element) => (element.scrollTop = 0));
  await mkdir("docs", { recursive: true });
  await page.screenshot({ path: "docs/app-screenshot.png" });
  const completed = await page.evaluate(() => window.lab.snapshot());
  assert.equal(completed.status, "completed");
  await writeFile(
    join(root, "packaged-result.json"),
    JSON.stringify(
      {
        passed: true,
        at: new Date().toISOString(),
        profile: completed.profile,
        checkpoints: completed.progress.checkpoints,
      },
      null,
      2,
    ),
  );
  await page.getByRole("button", { name: "Stop", exact: true }).click();
  await expect
    .poll(
      async () => (await page.evaluate(() => window.lab.snapshot())).status,
      { timeout: 180_000 },
    )
    .toBe("stopped");
  console.log("PASS: packaged app completed all steps and stopped its cluster");
} finally {
  await application.close();
}
