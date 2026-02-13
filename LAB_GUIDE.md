# Lab Design & Workflow Guide

One unified guide for designing, creating, testing, and deploying labs in this repository.

---

## 1. Lab types

This repo uses two lab styles. Choose one per lab.

### Task-based labs (recommended for most topics)

- **Use for:** Docker, scripting, tools, step-by-step tutorials.
- **Structure:** `README.md` + `TASKS.md` + `HINTS.md` + optional `src/`.
- **Flow:** Student opens `TASKS.md`, does tasks in order, uses `HINTS.md` if stuck.
- **Example:** `Docker/docker_lab_basics/`, `Linux/Shell Scripting/linux_lab_script_basics/`.

```
lab_name/
├── README.md       # Overview, learning objectives, duration, prerequisites
├── TASKS.md        # Numbered tasks: Objective, Instructions, Expected Output
├── HINTS.md        # Per-task hints and troubleshooting
├── src/            # Optional: sample files, scripts, commands
└── [lab_name].tar.gz   # Distribution (created when packaging)
```

**TASKS.md conventions:**

- Each task: **Objective**, **Instructions** (numbered), **Expected Output**.
- **Always put a blank line** between the **Instructions:** heading and the first numbered item (1. …).
- Put commands in single code blocks. Prefer one-line commands so copy-paste works (avoid `\` line continuations when possible).
- Close code blocks with ` ``` ` only (no language name on the closing fence).
- Keep notes (e.g. “-e sets environment variables”) outside the code block, after the block.

### Clue-based labs (scavenger / exploration)

- **Use for:** Linux navigation, search, discovery, multi-step challenges.
- **Structure:** `README.md` + `clues/level1..level3` + `data/` + optional `scripts/`, `.answers/`.
- **Flow:** Student runs entry command from README, then follows clues; each clue ends with a clear **NEXT STEP**.
- **Example:** File system scavenger hunt, permissions labs.

```
lab_name/
├── README.md           # Must include: cd clues/level1 && cat clue1.txt
├── clues/
│   ├── level1/         # Basic (e.g. clue1.txt, clue2.txt, clue3.txt)
│   ├── level2/         # Intermediate
│   └── level3/         # Advanced
├── data/               # logs/, archives/, secrets/, etc.
├── projects/           # Optional realistic dirs
├── scripts/            # Optional: setup_X_Y.sh, cleanup_X_Y.sh
├── .answers/
│   └── solutions.txt
└── [lab_name].tar.gz
```

**Clue conventions:**

- Every clue ends with **NEXT STEP**: exact command(s) to reach the next clue (e.g. `cat clue2.txt` or `cd ../level2 && cat clue1.txt`).
- Each clue teaches one **distinct** skill; avoid repeating the same command.
- If the lab has setup/cleanup scripts, paths in clues must be **relative to the clue directory** (e.g. `../../scripts/setup_1_1.sh` from `clues/level1/`).

---

## 2. Design principles

- **Progressive:** Start simple, increase difficulty. In task-based labs: Task 1 → Task N. In clue-based: Level 1 → Level 2 → Level 3.
- **Learning by doing:** Instructions and hints, not long lectures. Students run commands and see results.
- **Clear entry and flow:** Task-based: “Open TASKS.md.” Clue-based: README gives one entry command; every clue gives the next step.
- **Copy-paste friendly:** Prefer single-line commands in TASKS.md; avoid multi-line `\` when it breaks pasting.
- **Realistic:** Use real commands, real paths, and (for clue-based) realistic file names and content.

---

## 3. Workflow

### Phase 1: Design

- Define **learning objectives** and **duration**.
- Choose **lab type** (task-based vs clue-based).
- For task-based: list tasks and what each teaches. For clue-based: plan levels and what each clue teaches (no repetition).

### Phase 2: Create content

**Task-based:**

- Write `README.md` (overview, objectives, prerequisites).
- Write `TASKS.md` (objective, instructions, expected output per task; code in single blocks).
- Write `HINTS.md` (per-task hints, common errors).
- Add `src/` only if you need sample files or scripts.

**Clue-based:**

- README with entry command: `cd clues/level1 && cat clue1.txt`.
- Clues in `clues/levelN/clueN.txt`; each ends with NEXT STEP.
- Data files under `data/`, optional `projects/`, `scripts/`.
- `.answers/solutions.txt` for instructors.

**Scripts (when used):**

- Use **Unix line endings (LF)**. If edited on Windows, run: `sed -i 's/\r$//' scripts/*.sh`.
- Executable: `chmod +x scripts/*.sh`.
- Paths in clues: relative to clue folder (e.g. `../../scripts/setup_1_1.sh`).
- Setup scripts: idempotent. Cleanup scripts: handle missing PIDs/resources.

### Phase 3: Test

- **Task-based:** Do every task from a clean state; copy-paste commands from the doc.
- **Clue-based:** Follow README entry, then every NEXT STEP; confirm all paths and commands work.
- Check: no wrong code-block closing (` ```bash ` at end of block), no broken multi-line paste.

### Phase 4: Package

```bash
cd "Module Name"
tar -czf lab_name.tar.gz lab_name/
# If lab has scripts, use: tar --mode='a+x' -czf lab_name.tar.gz lab_name/
```

### Phase 5: Deploy (when using Git + releases)

- Commit and push. If you use a deploy script (e.g. `create_and_deploy_lab.sh`), run it from repo root.
- Attach `lab_name.tar.gz` to the release.
- Document the one-line download + entry for students (e.g. `curl -L ... | tar -xz && cd lab_name && ...`).

---

## 4. Quick reference

**Create archive (from module dir):**

```bash
cd "Module Name"
tar --mode='a+x' -czf lab_name.tar.gz lab_name/
```

**Fix script line endings (before packaging):**

```bash
cd lab_name/scripts
sed -i 's/\r$//' *.sh
chmod +x *.sh
```

**Student entry examples:**

- Task-based: extract, then open `TASKS.md` (or `README.md` first).
- Clue-based:  
  `curl -L [URL] | tar -xz && cd lab_name && cd clues/level1 && cat clue1.txt`

**Optional: PDF from TASKS.md (task-based labs):**

- In the lab folder, use a script that converts `TASKS.md` to PDF (e.g. `convert_github_pdf.sh` in `Docker/docker_lab_basics/`). Script should clean code-block language labels so the PDF shows plain code blocks.

---

## 5. Quality checklist

**Content**

- [ ] Each task or clue teaches something **new** (no repeated objectives).
- [ ] All commands and paths are correct and tested.
- [ ] Code blocks are single blocks; copy-paste works (single-line commands where it matters).
- [ ] Expected output or NEXT STEP is clear.

**Task-based**

- [ ] README has objectives, duration, prerequisites.
- [ ] TASKS.md has Objective, Instructions, Expected Output per task.
- [ ] Code blocks closed with ` ``` ` only.

**Clue-based**

- [ ] README includes exact entry command.
- [ ] Every clue ends with NEXT STEP; flow tested start to finish.
- [ ] Script paths in clues are relative to clue directory.

**Scripts / packaging**

- [ ] Scripts: LF line endings, executable; paths in clues correct.
- [ ] Archive: `tar --mode='a+x'` if the lab has scripts.

---

## 6. Troubleshooting

**“cannot execute: required file not found” (scripts):**  
Scripts have CRLF line endings. Fix: `cd lab_name/scripts && sed -i 's/\r$//' *.sh`. Verify with `file script.sh` (should not show CRLF).

**Copy-paste breaks long commands:**  
In TASKS.md, use a single line for the command (no `\` continuations) so students can paste one block.

**Wrong code block in PDF:**  
Use a converter that strips language tags from fenced blocks (e.g. `convert_github_pdf.sh`) so the PDF shows one unified block per command.

---

## 7. Repository layout (reference)

```
DevOps-Materials/
├── LAB_GUIDE.md           ← This file (unified lab design & workflow)
├── README.md              ← Course/module overview and lab list
│
├── Linux/
│   ├── Shell Scripting/
│   │   ├── linux_lab_script_basics/   # Task-based example
│   │   └── ...
│   ├── [other topics]/
│   └── ...
├── Docker/
│   └── docker_lab_basics/              # Task-based example
└── Python/
    └── ...
```

---

**Summary:** Use **task-based** labs (README + TASKS + HINTS) for most new labs; use **clue-based** when you want exploration and discovery. Keep one clear entry point, progressive difficulty, and copy-paste-friendly commands. Package with `tar` (and `--mode='a+x'` when there are scripts); fix line endings before packaging.

**Last updated:** 2026-02-13
