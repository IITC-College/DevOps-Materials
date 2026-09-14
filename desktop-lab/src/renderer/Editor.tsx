import { useEffect, useRef, useState } from "react";
import MonacoEditor, { loader } from "@monaco-editor/react";
import * as monaco from "monaco-editor/editor/editor.api.js";
import "monaco-editor/languages/definitions/yaml/register.js";
import EditorWorker from "monaco-editor/editor/editor.worker.js?worker";
import type { WorkspaceFile } from "../shared/api";
self.MonacoEnvironment = { getWorker: () => new EditorWorker() };
loader.config({ monaco });
export function Editor({ runId, busy }: { runId?: string; busy: boolean }) {
  const [files, setFiles] = useState<string[]>([]),
    [file, setFile] = useState<WorkspaceFile | null>(null),
    [content, setContent] = useState(""),
    [error, setError] = useState(""),
    [conflict, setConflict] = useState(false);
  const dirty = !!file && content !== file.content;
  const current = useRef({ file, dirty });
  current.current = { file, dirty };
  const load = async (path: string) => {
    try {
      const loaded = await window.lab.readFile(path);
      setFile(loaded);
      setContent(loaded.content);
      setConflict(false);
      setError("");
    } catch (e) {
      setError((e as Error).message);
    }
  };
  useEffect(() => {
    setFile(null);
    setContent("");
    setFiles([]);
    setConflict(false);
    setError("");
    let active = true;
    const poll = async () => {
      try {
        const list = await window.lab.files();
        if (!active) return;
        setFiles(list);
        const open = current.current.file;
        if (!open && list.includes("nginx.yaml")) {
          const initial = await window.lab.readFile("nginx.yaml");
          if (active) {
            setFile(initial);
            setContent(initial.content);
          }
        } else if (open) {
          const latest = await window.lab.readFile(open.path);
          if (!active) return;
          if (latest.revision !== open.revision) {
            if (current.current.dirty) setConflict(true);
            else {
              setFile(latest);
              setContent(latest.content);
            }
          }
        }
      } catch {
        /* Workspace may not exist yet while starting. */
      }
    };
    void poll();
    const timer = setInterval(poll, 2000);
    return () => {
      active = false;
      clearInterval(timer);
    };
  }, [runId]);
  const select = async (path: string) => {
    if (dirty && !window.confirm("Discard unsaved changes in this editor?"))
      return;
    await load(path);
  };
  const save = async () => {
    if (!file) return;
    try {
      const saved = await window.lab.saveFile(
        file.path,
        content,
        file.revision,
      );
      setFile(saved);
      setConflict(false);
      setError("");
    } catch (e) {
      const message = (e as Error).message;
      setError(message);
      if (message.includes("FILE_CONFLICT")) setConflict(true);
    }
  };
  return (
    <section className="editor-panel">
      <div className="panel-heading">
        <span>
          Workspace <small>Shared with your terminal</small>
        </span>
        <button
          disabled={!dirty || busy || conflict}
          onClick={() => void save()}
        >
          Save{dirty ? " •" : ""}
        </button>
      </div>
      <div className="editor-body">
        <nav className="files" aria-label="Workspace files">
          {files.map((path) => (
            <button
              key={path}
              className={path === file?.path ? "file active" : "file"}
              onClick={() => void select(path)}
            >
              {path.endsWith(".yaml") ? "◇" : "≡"} {path}
            </button>
          ))}
          {!files.length && <p>Starter files appear when the lab begins.</p>}
        </nav>
        <div className="code-area">
          <div className="file-tab">
            {file?.path ?? "No file selected"}
            {dirty && <span>Unsaved changes</span>}
          </div>
          {conflict && (
            <div className="conflict" role="alert">
              This file changed in the terminal. Copy any edits you need, then{" "}
              <button
                onClick={() => {
                  if (
                    window.confirm(
                      "Reload the file and discard unsaved editor changes?",
                    )
                  )
                    void load(file!.path);
                }}
              >
                Reload file
              </button>
              .
            </div>
          )}
          {error && <div className="inline-error">{error}</div>}
          {file ? (
            <MonacoEditor
              height="100%"
              language={file.path.endsWith(".json") ? "json" : "yaml"}
              theme="vs-dark"
              value={content}
              onChange={(value) => setContent(value ?? "")}
              options={{
                readOnly: busy,
                minimap: { enabled: false },
                fontSize: 13,
                fontFamily: "Menlo, Monaco, monospace",
                padding: { top: 16 },
                scrollBeyondLastLine: false,
                automaticLayout: true,
                tabSize: 2,
                wordWrap: "on",
              }}
            />
          ) : (
            <div className="empty-editor">Your manifests, ready to edit.</div>
          )}
        </div>
      </div>
    </section>
  );
}
