import { useEffect, useRef, useState } from "react";
import { Terminal as XTerminal } from "@xterm/xterm";
import { FitAddon } from "@xterm/addon-fit";
import "@xterm/xterm/css/xterm.css";
export function Terminal({
  runId,
  enabled,
}: {
  runId?: string;
  enabled: boolean;
}) {
  const host = useRef<HTMLDivElement>(null);
  const term = useRef<XTerminal | null>(null);
  const [error, setError] = useState("");
  useEffect(() => {
    const terminal = new XTerminal({
      fontFamily: "Menlo, Monaco, monospace",
      fontSize: 13,
      lineHeight: 1.25,
      cursorBlink: true,
      theme: {
        background: "#0b1218",
        foreground: "#d7e2eb",
        cursor: "#63d6bd",
      },
      scrollback: 3000,
    });
    const fit = new FitAddon();
    terminal.loadAddon(fit);
    terminal.open(host.current!);
    term.current = terminal;
    const unsubscribe = window.lab.onTerminal((text) => terminal.write(text));
    const input = terminal.onData((text) => {
      void window.lab.terminalWrite(text).catch((e) => setError(e.message));
    });
    const observer = new ResizeObserver(() => {
      fit.fit();
      void window.lab
        .terminalResize(terminal.cols, terminal.rows)
        .catch(() => {});
    });
    observer.observe(host.current!);
    terminal.writeln("\x1b[38;5;109mKubernetes Lab · Linux workspace\x1b[0m");
    return () => {
      observer.disconnect();
      unsubscribe();
      input.dispose();
      terminal.dispose();
      term.current = null;
    };
  }, [runId]);
  const connect = () => {
    setError("");
    void window.lab
      .terminalOpen()
      .then(() => {
        if (term.current)
          return window.lab.terminalResize(
            term.current.cols,
            term.current.rows,
          );
      })
      .catch((e) => setError(e.message));
  };
  useEffect(() => {
    if (enabled) connect();
  }, [enabled, runId]);
  return (
    <section className="terminal-panel">
      <div className="panel-heading">
        <span>
          <span className="dot" /> Linux terminal <small>/workspace</small>
        </span>
        <button className="text-button" disabled={!enabled} onClick={connect}>
          Reconnect terminal
        </button>
      </div>
      {error && <div className="inline-error">{error}</div>}
      <div ref={host} className="terminal" aria-label="Lab terminal" />
      {!enabled && (
        <div className="terminal-cover">
          Start or resume the lab to connect.
        </div>
      )}
    </section>
  );
}
