import { spawn } from "node:child_process";

export type Command = (
  bin: string,
  args: string[],
  options?: {
    env?: NodeJS.ProcessEnv;
    timeout?: number;
    input?: string;
    signal?: AbortSignal;
  },
) => Promise<string>;
export const command: Command = (bin, args, options = {}) =>
  new Promise((resolve, reject) => {
    const child = spawn(bin, args, {
      env: { ...process.env, ...options.env },
      stdio: ["pipe", "pipe", "pipe"],
    });
    let output = "",
      errors = "";
    const timer = setTimeout(() => {
      child.kill("SIGTERM");
    }, options.timeout ?? 30_000);
    const abort = () => child.kill("SIGTERM");
    options.signal?.addEventListener("abort", abort, { once: true });
    if (options.signal?.aborted) abort();
    child.stdout.on("data", (data) => {
      output += data;
      if (output.length > 8_000_000) child.kill();
    });
    child.stderr.on("data", (data) => {
      errors = (errors + data).slice(-16000);
    });
    child.on("error", (error) => {
      clearTimeout(timer);
      reject(error);
    });
    child.on("close", (code, signal) => {
      clearTimeout(timer);
      options.signal?.removeEventListener("abort", abort);
      if (code === 0) resolve(output.trim());
      else
        reject(
          new Error(
            `${bin} ${args.slice(0, 2).join(" ")} failed (${signal ?? code}): ${errors || output.slice(-2000)}`,
          ),
        );
    });
    child.stdin.end(options.input);
  });
export const sleep = (ms: number) =>
  new Promise((resolve) => setTimeout(resolve, ms));
