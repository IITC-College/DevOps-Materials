# How to Build a Lab (Python Module)

This document describes how labs are structured in this repository, based on the **Shell Scripting** module, and how to build equivalent **Python** labs. Use it as the single source of truth when creating new Python labs.

---

## 1. Two Lab Layers (From Shell Scripting)

The Shell Scripting module uses **two complementary structures**:

### 1.1 Instructor Content (In-Class Teaching)

**Location (Shell):** `Instructor Content/Linux/Shell Scripting/`  
**Location (Python):** `Instructor Content/Python/` (e.g. `Python Basics/`, `CLI-Tools/`)

**Purpose:** Short, focused topics used during instruction. Each topic is one lesson building block.

**Structure per topic:**

| Item | Shell Scripting | Python (to use) |
|------|-----------------|-----------------|
| **Folder name** | `NN-topic-name` (e.g. `04-script-structure-shebang`) | `NN_topic_name` (e.g. `04_variables`) |
| **Demo/step file** | `with_shebang.sh`, `deploy.sh`, `check.sh` | `step_NN.py`, `demo_*.py` |
| **Instructor notes** | `commands.md` (commands to run) | `commands.md` (e.g. `python3 step_04.py`, `python3 demo_*.py`) |

**Instructor topic contents:**

- **Scripts / code:** Small runnable examples that demonstrate one concept (e.g. shebang, variables, conditionals).
- **commands.md:** Short list of commands the instructor runs (e.g. `python3 step_04.py`, `python3 deploy.py`). No long prose.

**Naming conventions:**

- **Shell:** `check.sh`, `deploy.sh`, `backup.sh`; sometimes `*_broken.sh` / `*_fixed.sh` for debugging labs.
- **Python:** `step_NN.py` (main example for topic NN), `demo_<concept>.py` (focused demos).

---

### 1.2 Student Labs (Self-Paced / Homework)

**Location (Shell):** `Linux/Shell Scripting/`  
**Location (Python):** Use a dedicated folder, e.g. `Python/` or `Python Basics/` at repo root (same level as `Linux/`), or under `Instructor Content/Python/` depending on repo convention.

**Purpose:** Standalone, downloadable labs. Students get a folder (or tarball) and work through tasks on their own.

**Naming (Shell):** `linux_lab_script_<topic>` (e.g. `linux_lab_script_basics`, `linux_lab_script_variables`).  
**Naming (Python):** `python_lab_<topic>` (e.g. `python_lab_basics`, `python_lab_variables`).

**Standard files in every student lab:**

| File | Purpose |
|------|--------|
| **README.md** | Lab title, learning objectives, “Open TASKS.md to begin”, duration, prerequisites, what the student will create/build. |
| **TASKS.md** | Goal, prerequisites, then numbered **Tasks**. Each task: Objective, Instructions (steps), Expected Output, deliverable name (e.g. script/file name). |
| **HINTS.md** | Per-task hints + general tips (editor, running code, common errors). |
| **src/** (optional) | Starter code, templates, or data files (e.g. `data/logs/app.log`, `config.json`) for students to use. |

**Packaging (Shell):** `linux_lab_script_<topic>.tar.gz`.  
**Packaging (Python):** `python_lab_<topic>.tar.gz`.

---

## 2. Student Lab File Specifications

### 2.1 README.md

- **Title:** Clear lab name (e.g. “Python Lab – Print and Output”).
- **Learning objectives:** Bullet list of “After this lab you will be able to: …”.
- **Getting started:** One line: “Open `TASKS.md` to begin the lab exercises.”
- **Duration:** Estimated time (e.g. 20–30 minutes).
- **Prerequisites:** Previous labs or skills (e.g. “Script Basics” or “Basic command line”).
- **What you’ll create/build:** Short list of deliverables (e.g. “welcome.py”, “deploy.py”, “status.py”).

Keep README short; detail lives in TASKS.md.

---

### 2.2 TASKS.md

- **Goal:** One short paragraph describing the lab goal.
- **Prerequisites:** Same as README (can be one line).
- **Tasks:** Numbered sections. For each task:

  - **Objective:** One sentence.
  - **Instructions:** Numbered steps. Include exact code snippets where appropriate (e.g. first few lines of a script).
  - **Expected output:** Copy-pastable sample output (or “You’ll get an error – we fix this in the next task”).
  - **Deliverable:** Script/file name (e.g. “Script Name: `welcome.py`”).

- **Completion:** Short “Congratulations” plus “Key concepts learned” and “Next steps” (optional link to next lab).

Design so each task teaches **one new concept or skill**; avoid repeating the same step.

---

### 2.3 HINTS.md

- **Per-task hints:** Section per task (e.g. “## Task 1 – Welcome script”) with:
  - How to create/run the file (e.g. `nano welcome.py`, `python3 welcome.py`).
  - Syntax reminders (e.g. shebang, `print()`, `chmod +x` for shell; for Python: `#!/usr/bin/env python3`, `print()`).
  - What to expect (e.g. “Permission denied is normal here”).
- **General tips:** Editor usage (nano/vim/VS Code), running Python (`python3 script.py`), virtualenv if used.
- **Common errors:** One-line explanations (e.g. “NameError: check spelling of variable”, “IndentationError: use spaces”).

Hints should guide without giving the full solution.

---

### 2.4 src/ (Optional)

- **When to use:** When the lab needs starter code, templates, or data files.
- **Contents:**
  - **Templates:** e.g. `welcome_template.py`, `ops_tool_template.py` (incomplete for students to finish).
  - **Data:** e.g. `data/logs/app.log`, `data/configs/config.json` for read/write or parsing tasks.
- **Naming:** Descriptive and consistent (e.g. `*_template.py`, `config.json`).

Do not put solutions in `src/`; those stay in instructor-only material if needed.

---

## 3. Instructor Topic (In-Class) Structure

For each **instructor topic** (one concept per folder):

1. **Folder:** `NN_topic_name` under the right track (e.g. `Python Basics/`, `CLI-Tools/`).
2. **Step file:** `step_NN.py` – one small script that demonstrates the topic (run as `python3 step_NN.py`).
3. **Demos (optional):** `demo_<concept>.py` – minimal examples (e.g. `demo_print_sep.py`, `demo_if_else.py`).
4. **commands.md:** Only the commands to run, e.g.:
   ```bash
   python3 step_04.py
   python3 demo_assignment.py
   python3 demo_reassignment.py
   ```

No long narrative in `commands.md`; it’s a quick reference for the instructor.

---

## 4. Task Design Principles (From Shell Scripting)

- **Progressive:** Each task builds on the previous one; later tasks use skills from earlier tasks.
- **One concept per task:** Avoid multiple new ideas in a single task.
- **Clear outcome:** Every task has a well-defined deliverable and, where relevant, expected output.
- **Real-world relevance:** Prefer scenarios that mirror real use (e.g. “backup script”, “status report”, “config parser”) so students see why the concept matters.
- **Balance:** Instructions should be specific enough to succeed but not so long that students skip reading; use hints for edge cases.

---

## 5. Python-Specific Conventions

- **Interpreter:** Use `python3` in instructions and `commands.md` (e.g. `python3 script.py`).
- **Shebang (optional):** `#!/usr/bin/env python3` for runnable scripts; mention in hints if you want students to make scripts executable and run with `./script.py`.
- **Naming:**
  - Scripts: `snake_case.py` (e.g. `welcome.py`, `deploy.py`, `backup_step1.py`).
  - Instructor step/demo: `step_NN.py`, `demo_<concept>.py`.
- **Line endings:** Use LF (Unix) for all `.py` and `.md` files so scripts run correctly on Linux and WSL.
- **No solutions in student repo:** Keep solution scripts or answer keys in instructor-only content or `.answers/` if you adopt the same pattern as the Linux scavenger labs.

---

## 6. Checklist for Building a New Python Lab

**Before writing:**

- [ ] Decide: **Instructor topic** (in-class) vs **Student lab** (self-paced). Optionally both (topic + matching lab).
- [ ] Choose a **single theme** (e.g. “print and output”, “variables”, “conditionals”, “file reading”).
- [ ] List **learning objectives** (one per main concept).
- [ ] Outline **tasks** so each teaches one new thing and builds on the previous.

**For instructor topic:**

- [ ] Create folder `NN_topic_name` under the right Python track.
- [ ] Add `step_NN.py` and optional `demo_*.py`.
- [ ] Add `commands.md` with run commands only.

**For student lab:**

- [ ] Create folder `python_lab_<topic>`.
- [ ] Write `README.md` (objectives, duration, prerequisites, “Open TASKS.md”).
- [ ] Write `TASKS.md` (goal, prerequisites, numbered tasks with objective, instructions, expected output, deliverable).
- [ ] Write `HINTS.md` (per-task hints + general tips + common errors).
- [ ] Add `src/` only if needed (templates, data files).
- [ ] Test: follow TASKS.md as a student would; fix any missing steps or unclear instructions.
- [ ] Optionally package as `python_lab_<topic>.tar.gz` for distribution.

**Quality:**

- [ ] No solution code in student-facing files.
- [ ] All code snippets in TASKS.md are accurate and runnable.
- [ ] Expected output in TASKS.md matches the suggested code.
- [ ] HINTS help without giving the full answer.

---

## 7. Summary

| Aspect | Instructor topic (in-class) | Student lab (self-paced) |
|--------|----------------------------|---------------------------|
| **Place** | `Instructor Content/Python/<Track>/NN_topic_name/` | e.g. `Python/python_lab_<topic>/` |
| **Files** | `step_NN.py`, `demo_*.py`, `commands.md` | `README.md`, `TASKS.md`, `HINTS.md`, optional `src/` |
| **Audience** | Instructor running demos | Student working alone |
| **Content** | Minimal runnable examples + run commands | Objectives, tasks, hints, starter/data |

Use this document when you build new Python labs so they stay consistent with the Shell Scripting module and are ready for use in class and as standalone labs.

---

**Version:** 1.0  
**Based on:** Shell Scripting module structure (Instructor Content + Linux/Shell Scripting student labs)  
**Last updated:** 2026-02-12
