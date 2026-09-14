import type { Lab, Progress, CheckResult, Variables } from "./lab.js";
export type Status =
  | "idle"
  | "starting"
  | "ready"
  | "checking"
  | "stopped"
  | "resumable"
  | "error"
  | "completed";
export interface Snapshot {
  lab: Lab;
  instructions: Record<string, string>;
  status: Status;
  busy: boolean;
  runId?: string;
  profile?: string;
  progress: Progress;
  variables: Variables;
  results: CheckResult[];
  logs: string[];
  error?: string;
}
export interface WorkspaceFile {
  path: string;
  content: string;
  revision: string;
}
export interface LabAPI {
  snapshot(): Promise<Snapshot>;
  start(): Promise<void>;
  stop(): Promise<void>;
  resume(): Promise<void>;
  reset(): Promise<void>;
  check(stepId: string): Promise<void>;
  cancelCheck(): Promise<void>;
  next(): Promise<void>;
  files(): Promise<string[]>;
  readFile(path: string): Promise<WorkspaceFile>;
  saveFile(
    path: string,
    content: string,
    revision: string | null,
  ): Promise<WorkspaceFile>;
  terminalOpen(): Promise<void>;
  terminalWrite(text: string): Promise<void>;
  terminalResize(cols: number, rows: number): Promise<void>;
  onSnapshot(callback: (snapshot: Snapshot) => void): () => void;
  onTerminal(callback: (text: string) => void): () => void;
}
declare global {
  interface Window {
    lab: LabAPI;
  }
}
