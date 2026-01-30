# Linux Lab – Troubleshooting Flow (Broken Service Investigation)

A **home lab** that reinforces a **repeating troubleshooting methodology** through simulated failure scenarios. You receive a "broken" service or process, apply the 5-step flow, and **submit a diagnosis** – no code, no fix scripts. Only correct diagnosis: status, relevant log line, action performed, short conclusion.

Each clue has **setup** (run first) and **cleanup** (run when done) so the scenario is realistic and isolated.

## The 5-Step Flow (for the board)

Use this flow for every failure scenario:

1. **What is not working?** (Describe the symptom.)
2. **Is it a process or a service?** (Process = what is running. Service = what systemd manages.)
3. **What is the status?** (e.g. `ps` for process, `systemctl --user status` for service.)
4. **What do the logs say?** (e.g. `data/logs/` or `journalctl --user -u UNIT -n 20`.)
5. **What is the next action?** (Start, restart, kill, fix config, report.)

## Submission (Home Lab Deliverable)

Your deliverable is an **investigation report**, not code. For each scenario (each clue), add **one block** to your report using the template below. Save your report at the lab root as **`investigation_report.txt`**.

**Template (repeat one block per scenario):**

- **Service/Process name**: (e.g. lab-troubleshoot or lab-helper)
- **Status**: (e.g. active (running), failed, inactive, or process not found)
- **Relevant log line**: (one line from journalctl or a log file that explains the problem)
- **Action performed**: (e.g. checked status, read logs, restarted service, reported config error)
- **Short conclusion**: (one sentence: what was wrong and what you did)

A copy-paste template is in `submission_template.txt` at the lab root.

## Pair Practice (Optional)

- Each clue is a **short failure scenario**.
- **One person** analyzes: apply the flow and say what to check (process or service? status? logs?).
- **The other** executes: run the commands.
- **Switch roles** for the next clue.
- The instructor may ask: *"How did you know to check there?"*

## How This Lab Works

- **SETUP**: Before each clue, run the setup script for that clue (from the clue folder: `../../scripts/setup_X_Y.sh`). It creates the failure scenario (e.g. process not running, service stopped).
- **CLEANUP**: When done with a clue, run the cleanup script (`../../scripts/cleanup_X_Y.sh`) so the next clue starts in a clean state.
- **REPORT**: After each scenario, add one block (status, log line, action, conclusion) to your `investigation_report.txt`.

## Direct Entry

Start at the first clue:

```bash
cd clues/level1 && cat clue1.txt
```

(After extracting the lab, run `cd linux_lab_troubleshooting_flow` first.)

## Prerequisites

- Linux with `ps`, `kill`, `systemctl`, `journalctl` (systemd-based distribution)
- Recommended: complete Processes Basics, Process Management (kill), and Process vs Service labs first

## Duration

30–35 minutes

## Learning Objectives

After this lab you will be able to:

- Apply the 5-step troubleshooting flow to any "something is broken" report.
- Decide whether the problem is a **process** or a **service** and check the right place (e.g. `ps` vs `systemctl --user status`).
- Use **status** and **logs** to choose the next action (start, restart, kill, investigate).

## Lab Structure

- **Level 1:** Process-only failure scenarios (not running, high CPU, disappeared).
- **Level 2:** Service (systemd user unit) failure scenarios (stopped, failed, running but error in logs).
- **Level 3:** Combined or "decide from logs" scenarios.

Each clue ends with a **NEXT STEP** pointing to the next clue.

## Tips

Optional hints are in `data/secrets/tips.txt`.

## Version

- **Version:** 1.0
- **Repository:** https://github.com/IITC-College/DevOps-Jan26
