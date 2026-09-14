import { useEffect, useState } from "react";
import ReactMarkdown from "react-markdown";
import type { Snapshot } from "../shared/api";
import { interpolate } from "../shared/lab";
import { Editor } from "./Editor";
import { Terminal } from "./Terminal";
const display = (value: unknown) =>
  typeof value === "string" ? value : JSON.stringify(value);
export function App() {
  const [state, setState] = useState<Snapshot | null>(null),
    [error, setError] = useState(""),
    [hint, setHint] = useState(false);
  useEffect(() => {
    const off = window.lab.onSnapshot(setState);
    void window.lab
      .snapshot()
      .then(setState)
      .catch((e) => setError(e.message));
    return off;
  }, []);
  useEffect(() => setHint(false), [state?.progress.current]);
  const action = async (fn: () => Promise<unknown>) => {
    setError("");
    try {
      await fn();
    } catch (e) {
      setError((e as Error).message);
    }
  };
  if (!state)
    return (
      <main className="loading">{error || "Opening Kubernetes Lab…"}</main>
    );
  const step = state.lab.steps[state.progress.current],
    passed = !!state.progress.checkpoints[step.id],
    running =
      ["ready", "checking", "completed"].includes(state.status) && !state.busy;
  const count = Object.keys(state.progress.checkpoints).length,
    checking = state.status === "checking";
  return (
    <div className="app">
      <header className="topbar">
        <div className="brand">
          <span className="brand-symbol">⎈</span>
          <div>
            Kubernetes Lab<small>LOCAL PRACTICE / REAL CLUSTERS</small>
          </div>
        </div>
        <div className="runtime-badge">
          <span className={running ? "dot" : "dot muted"} />
          {state.status === "idle" ? "Environment not started" : state.status}
          <span className="chip">MINIKUBE</span>
        </div>
        <div className="lifecycle">
          {!state.runId ? (
            <button
              className="primary"
              disabled={state.busy}
              onClick={() => void action(() => window.lab.start())}
            >
              Start lab
            </button>
          ) : (
            <>
              {running ? (
                <button
                  disabled={state.busy}
                  onClick={() => void action(() => window.lab.stop())}
                >
                  Stop
                </button>
              ) : (
                <button
                  className="primary"
                  disabled={state.busy}
                  onClick={() => void action(() => window.lab.resume())}
                >
                  Resume
                </button>
              )}
              <button
                disabled={state.busy}
                onClick={() => void action(() => window.lab.reset())}
              >
                Reset Lab
              </button>
            </>
          )}
        </div>
      </header>
      <div className="main-grid">
        <aside className="lesson">
          <div className="eyebrow">CKA / SCHEDULING · LAB 02</div>
          <h1>{state.lab.title}</h1>
          <p className="description">{state.lab.description}</p>
          <div className="progress-heading">
            <span>YOUR PROGRESS</span>
            <strong>
              {count} / {state.lab.steps.length} complete
            </strong>
          </div>
          <div className="progress-track">
            <div
              style={{ width: `${(count / state.lab.steps.length) * 100}%` }}
            />
          </div>
          <ol className="steps">
            {state.lab.steps.map((item, index) => {
              const done = !!state.progress.checkpoints[item.id];
              return (
                <li
                  key={item.id}
                  className={
                    index === state.progress.current
                      ? "current"
                      : done
                        ? "done"
                        : "locked"
                  }
                >
                  <span className="step-number">{done ? "✓" : index + 1}</span>
                  <span>
                    {item.title}
                    <small>
                      {done
                        ? "Passed"
                        : index === state.progress.current
                          ? "Current task"
                          : "Locked"}
                    </small>
                  </span>
                </li>
              );
            })}
          </ol>
          <div className="task">
            <div className="eyebrow">
              STEP {state.progress.current + 1} OF {state.lab.steps.length}
            </div>
            <h2>{step.title}</h2>
            <ReactMarkdown>
              {interpolate(state.instructions[step.id], state.variables)}
            </ReactMarkdown>
            <button
              className="text-button hint-toggle"
              onClick={() => setHint(!hint)}
            >
              {hint ? "Hide hint" : "Show a hint"} <span>↗</span>
            </button>
            {hint && <p className="hint">{step.hint}</p>}
          </div>
          {(error || state.error) && (
            <div className="error-box" role="alert">
              {error || state.error}
            </div>
          )}
          {state.results.length > 0 && (
            <div className="checks" aria-label="Validation results">
              {state.results.map((result) => (
                <div key={result.id} className={`check ${result.status}`}>
                  <span>
                    {result.status === "passed"
                      ? "✓"
                      : result.status === "error"
                        ? "!"
                        : "○"}
                  </span>
                  <div>
                    <span>{result.label}</span>
                    {result.status !== "passed" && (
                      <small>
                        {result.message ??
                          `Expected: ${display(result.expected)} · Observed: ${display(result.observed)}`}
                      </small>
                    )}
                  </div>
                </div>
              ))}
            </div>
          )}
          {state.status === "completed" && (
            <div className="success" role="status">
              Lab complete. All four checkpoints passed.
            </div>
          )}
          <div className="task-actions">
            {checking ? (
              <button
                onClick={() => void action(() => window.lab.cancelCheck())}
              >
                Cancel check
              </button>
            ) : (
              <button
                className="primary"
                disabled={!running || passed}
                onClick={() => void action(() => window.lab.check(step.id))}
              >
                {passed ? "✓ Passed" : "Check"}
              </button>
            )}
            <button
              disabled={
                !passed ||
                checking ||
                !running ||
                state.progress.current === state.lab.steps.length - 1
              }
              onClick={() => void action(() => window.lab.next())}
            >
              Next →
            </button>
          </div>
          <p className="check-note">
            {checking
              ? "Checking live cluster state for up to 60 seconds…"
              : "Every requirement must pass to unlock the next step."}
          </p>
        </aside>
        <main className="workspace">
          <div className="workspace-bar">
            <span>LAB WORKSPACE</span>
            <small>
              {state.profile ??
                "A dedicated cluster will be created for this run."}
            </small>
          </div>
          <Editor runId={state.runId} busy={state.busy} />
          <Terminal runId={state.runId} enabled={running} />
        </main>
      </div>
      <footer>
        <span>
          <span className="dot muted" /> Closing the app keeps the cluster
          running. Use Stop to free resources.
        </span>
        <details>
          <summary>
            Environment activity {state.busy ? "· working…" : ""}
          </summary>
          <div className="activity">
            {state.logs.length
              ? state.logs.map((line, index) => <div key={index}>{line}</div>)
              : "No environment activity yet."}
          </div>
        </details>
      </footer>
      {state.busy && (
        <div className="setup-banner" role="status">
          <span className="spinner" />
          {state.logs.at(-1) ?? "Preparing environment…"}
        </div>
      )}
    </div>
  );
}
