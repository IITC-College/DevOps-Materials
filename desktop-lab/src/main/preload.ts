import { contextBridge, ipcRenderer } from "electron";
import type { LabAPI } from "../shared/api.js";
const invoke = (name: string, ...args: unknown[]) =>
  ipcRenderer.invoke(`lab:${name}`, ...args);
const listen = (channel: string, callback: (value: any) => void) => {
  const handler = (_event: unknown, value: unknown) => callback(value);
  ipcRenderer.on(channel, handler);
  return () => ipcRenderer.removeListener(channel, handler);
};
const api: LabAPI = {
  snapshot: () => invoke("snapshot"),
  start: () => invoke("start"),
  stop: () => invoke("stop"),
  resume: () => invoke("resume"),
  reset: () => invoke("reset"),
  check: (id) => invoke("check", id),
  cancelCheck: () => invoke("cancelCheck"),
  next: () => invoke("next"),
  files: () => invoke("files"),
  readFile: (path) => invoke("readFile", path),
  saveFile: (path, content, revision) =>
    invoke("saveFile", path, content, revision),
  terminalOpen: () => invoke("terminalOpen"),
  terminalWrite: (text) => invoke("terminalWrite", text),
  terminalResize: (cols, rows) => invoke("terminalResize", cols, rows),
  onSnapshot: (callback) => listen("lab:snapshot", callback),
  onTerminal: (callback) => listen("lab:terminal", callback),
};
contextBridge.exposeInMainWorld("lab", api);
