import { app, BrowserWindow, ipcMain, dialog } from "electron";
import { join } from "node:path";
import { z } from "zod";
import { loadLab } from "./lab-loader.js";
import { Manager } from "./manager.js";
import { FakeRuntime } from "./fake-runtime.js";
import { command } from "./command.js";
import type { IPty } from "node-pty";
import { spawn } from "node-pty";

// Finder-launched apps do not inherit a login shell PATH.
process.env.PATH = [
  process.env.PATH,
  "/opt/homebrew/bin",
  "/usr/local/bin",
  `${app.getPath("home")}/.docker/bin`,
  "/usr/bin",
  "/bin",
]
  .filter(Boolean)
  .join(":");
const testMode = !app.isPackaged && process.env.KLAB_FAKE === "1";
if (process.env.KLAB_DATA_DIR)
  app.setPath("userData", process.env.KLAB_DATA_DIR);
if (!app.requestSingleInstanceLock()) app.quit();
else void boot();
async function boot() {
  await app.whenReady();
  const base = app.isPackaged ? process.resourcesPath : app.getAppPath();
  const manager = new Manager(
    app.getPath("userData"),
    await loadLab(join(base, "labs/manual-scheduling")),
    join(base, "runtime"),
    testMode
      ? (run, config, log) => new FakeRuntime(run, config, command, log)
      : undefined,
  );
  await manager.init();
  let win: BrowserWindow | null = null,
    terminal: IPty | undefined;
  const closeTerminal = () => {
    try {
      terminal?.kill();
    } catch {}
    terminal = undefined;
  };
  const send = (channel: string, data: unknown) => {
    if (win && !win.isDestroyed()) win.webContents.send(channel, data);
  };
  manager.on("snapshot", (state) => send("lab:snapshot", state));
  manager.on("terminal-close", closeTerminal);
  function handle(
    name: string,
    schema: z.ZodType,
    fn: (...args: any[]) => unknown,
  ) {
    ipcMain.handle(`lab:${name}`, async (event, ...args) => {
      if (
        !win ||
        event.sender !== win.webContents ||
        event.senderFrame !== win.webContents.mainFrame
      )
        throw new Error("Untrusted app request");
      const parsed = schema.parse(args) as unknown[];
      return fn(...parsed);
    });
  }
  const none = z.tuple([]),
    path = z.string().min(1).max(240);
  handle("snapshot", none, () => manager.snapshot);
  handle("start", none, () => manager.start());
  handle("stop", none, () => manager.stop());
  handle("resume", none, () => manager.resume());
  handle("reset", none, async () => {
    const result = await dialog.showMessageBox(win!, {
      type: "warning",
      buttons: ["Cancel", "Reset Lab"],
      defaultId: 0,
      cancelId: 0,
      message: "Reset this lab?",
      detail:
        "This deletes only this app-owned cluster and toolbox. Your lab files and checkpoints will be replaced with a fresh run.",
    });
    if (result.response === 1) await manager.reset();
  });
  handle("check", z.tuple([z.string().regex(/^[a-z0-9-]+$/)]), (id) =>
    manager.check(id),
  );
  handle("cancelCheck", none, () => manager.cancelCheck());
  handle("next", none, () => manager.next());
  handle("files", none, () => manager.files());
  handle("readFile", z.tuple([path]), (p) => manager.readFile(p));
  handle(
    "saveFile",
    z.tuple([path, z.string().max(2_000_000), z.string().max(64).nullable()]),
    (p, c, r) => manager.saveFile(p, c, r),
  );
  handle("terminalOpen", none, () => {
    manager.requireReady();
    if (terminal) return;
    const runtime = manager.runtime!;
    const bin = testMode ? "/bin/bash" : "docker";
    const args = testMode
      ? ["--noprofile", "--norc"]
      : ["exec", "-it", runtime.run.toolbox, "bash", "--noprofile", "--norc"];
    const env = {
      ...process.env,
      TERM: "xterm-256color",
      PS1: "\\[\\e[32m\\]lab\\[\\e[0m\\]:\\w\\$ ",
    };
    terminal = spawn(bin, args, {
      name: "xterm-256color",
      cols: 100,
      rows: 24,
      cwd: runtime.workspace,
      env,
    });
    const current = terminal;
    current.onData((data) => send("lab:terminal", data));
    current.onExit(() => {
      if (terminal === current) {
        terminal = undefined;
        send(
          "lab:terminal",
          "\r\n[Terminal disconnected. Use Reconnect terminal.]\r\n",
        );
      }
    });
  });
  handle("terminalWrite", z.tuple([z.string().max(65536)]), (text) => {
    manager.requireReady();
    if (!terminal) throw new Error("Open the terminal first");
    terminal.write(text);
  });
  handle(
    "terminalResize",
    z.tuple([
      z.number().int().min(2).max(500),
      z.number().int().min(2).max(200),
    ]),
    (cols, rows) => terminal?.resize(cols, rows),
  );
  const createWindow = () => {
    win = new BrowserWindow({
      width: 1440,
      height: 960,
      minWidth: 1050,
      minHeight: 720,
      title: "Kubernetes Lab",
      backgroundColor: "#10171e",
      webPreferences: {
        preload: join(__dirname, "preload.cjs"),
        contextIsolation: true,
        nodeIntegration: false,
        sandbox: true,
      },
    });
    win.setMenuBarVisibility(false);
    win.webContents.setWindowOpenHandler(() => ({ action: "deny" }));
    win.webContents.on("will-navigate", (event) => event.preventDefault());
    win.webContents.session.setPermissionRequestHandler(
      (_contents, _permission, callback) => callback(false),
    );
    void win.loadFile(join(__dirname, "../renderer/index.html"));
    win.on("closed", () => {
      closeTerminal();
      win = null;
    });
  };
  app.on("second-instance", () => {
    win?.show();
    win?.focus();
  });
  app.on("activate", () => {
    if (!win) createWindow();
  });
  app.on("before-quit", () => {
    manager.cancelCheck();
    closeTerminal();
  });
  app.on("window-all-closed", () => app.quit());
  createWindow();
}
process.on("unhandledRejection", (error) => {
  console.error(error);
  void dialog.showErrorBox("Kubernetes Lab", String(error));
});
