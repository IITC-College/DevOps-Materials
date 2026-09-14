import { _electron as electron, expect } from "@playwright/test";
import { resolve } from "node:path";
const env: Record<string, string> = {
  ...(process.env as Record<string, string>),
  KLAB_DATA_DIR: resolve(".state/integration"),
};
delete env.ELECTRON_RUN_AS_NODE;
delete env.KLAB_FAKE;
const app = await electron.launch({
  executablePath: resolve(
    "release/mac-arm64/Kubernetes Lab.app/Contents/MacOS/Kubernetes Lab",
  ),
  env,
});
try {
  const page = await app.firstWindow();
  await expect(page.getByText("4 / 4 complete", { exact: true })).toBeVisible();
  await page.getByRole("button", { name: "Resume", exact: true }).click();
  await expect
    .poll(
      async () => (await page.evaluate(() => window.lab.snapshot())).status,
      { timeout: 180_000 },
    )
    .toBe("completed");
  await page.evaluate(() => window.lab.terminalOpen());
  await page.evaluate(() => {
    (window as any).output = "";
    window.lab.onTerminal((text) => ((window as any).output += text));
  });
  await page.evaluate(() =>
    window.lab.terminalWrite("kubectl get pods -o wide\r"),
  );
  await expect
    .poll(() => page.evaluate(() => (window as any).output))
    .toContain("Running");
  await page.locator(".lesson").evaluate((el) => (el.scrollTop = 0));
  await page.screenshot({ path: "docs/app-screenshot.png" });
  await page.getByRole("button", { name: "Stop", exact: true }).click();
  await expect
    .poll(
      async () => (await page.evaluate(() => window.lab.snapshot())).status,
      { timeout: 180_000 },
    )
    .toBe("stopped");
  console.log(
    "PASS: final release build restores all four checkpoints, runs the real terminal, and stops cleanly",
  );
} finally {
  await app.close();
}
