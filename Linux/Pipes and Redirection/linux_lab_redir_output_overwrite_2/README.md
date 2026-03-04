# Linux Lab - Output Redirection with `>` (Part 2)

## Lab Overview

**Topic:** Output Redirection — The `>` Operator
**Theme:** "Redirecting in Context — Practical Scenarios"
**Difficulty:** Intermediate

This lab builds on Part 1. You already know what `>` does — now you will apply
it in more realistic scenarios: creating config-like files, filtering logs,
building reports, and fixing real bugs.

---

## Installation Instructions

### Method 1: Download with curl (Recommended)

```bash
curl -L -o lab.tar.gz https://github.com/IITC-College/DevOps-Materials/releases/download/v5.0-pipes-redirection/linux_lab_redir_output_overwrite_2.tar.gz
tar -xzf lab.tar.gz
cd linux_lab_redir_output_overwrite_2
```

### Method 2: Clone the repository

```bash
git clone https://github.com/IITC-College/DevOps-Materials.git
cd DevOps-Materials/Linux/Pipes\ and\ Redirection/linux_lab_redir_output_overwrite_2
```

---

---

## Lab Objective

By the end of this lab you will be able to:

- Use `>` to write configuration-like files with `echo`
- Understand and predict overwrite behavior with confidence
- Use `cat` + `>` to copy/transform file contents
- Redirect output into subdirectories
- Filter log files with `grep` and save results with `>`
- Create a complete system snapshot that intentionally replaces old data

---

## Lab Structure

```
clues/
├── level1/       ← Creating files with echo and working with backups
├── level2/       ← Redirecting to paths, building reports, field extraction
└── level3/       ← Bug fixing, filtering, and final snapshot challenge
```

---

## Exercise List

### Level 1 — Building Files with Echo
1. **clue1.txt** — Redirect echo to create a config-like file
2. **clue2.txt** — Overwrite test: see and confirm the behavior
3. **clue3.txt** — Redirect cat output to copy a file

### Level 2 — Paths and Reports
4. **clue1.txt** — Redirect to a specific subdirectory path
5. **clue2.txt** — Multiple echo redirects: only one survives
6. **clue3.txt** — Build a system report (overwrite challenge)

### Level 3 — Debugging and Filtering
7. **clue1.txt** — Fix the overwrite bug in a provided script
8. **clue2.txt** — Filter logs with grep and save with `>`
9. **clue3.txt** — Final challenge: complete system snapshot

---

## Getting Started

```bash
cat start_here.txt
cd clues/level1
cat clue1.txt
```
