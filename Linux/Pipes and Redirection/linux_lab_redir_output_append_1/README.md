# Linux Lab - Output Redirection with `>>` (Part 1)

## Lab Overview

**Topic:** Output Redirection — The `>>` Operator
**Theme:** "Building Files Over Time"
**Difficulty:** Beginner → Intermediate

In this lab you will discover how `>>` differs from `>`. While `>` replaces a file's contents, `>>` **appends** to the end — making files grow over time without losing existing data.

---

## Installation Instructions

### Method 1: Download with curl (Recommended)

```bash
curl -L -o lab.tar.gz https://github.com/IITC-College/DevOps-Materials/releases/download/v5.0-pipes-redirection/linux_lab_redir_output_append_1.tar.gz
tar -xzf lab.tar.gz
cd linux_lab_redir_output_append_1
```

### Method 2: Clone the repository

```bash
git clone https://github.com/IITC-College/DevOps-Materials.git
cd DevOps-Materials/Linux/Pipes\ and\ Redirection/linux_lab_redir_output_append_1
```

---

---

## Lab Objective

By the end of this lab you will be able to:

- Explain the difference between `>` (overwrite) and `>>` (append)
- Use `>>` to add content to the end of a file without destroying existing data
- Build growing log files by appending command output over time
- Combine `>` and `>>` strategically: `>` to initialize, `>>` to grow
- Use `>>` correctly inside loops

---

## Lab Structure

```
clues/
├── level1/       ← Foundations: > vs >>, building lists, appending command output
├── level2/       ← Application: log rotation, existing files, diary entries
└── level3/       ← Mastery: loops, combining operators, audit trail
```

---

## Exercise List

### Level 1 — Foundations
1. **clue1.txt** — Append vs Overwrite: The Critical Difference
2. **clue2.txt** — Building a List: Append Names One by One
3. **clue3.txt** — Append Command Output: date Grows a Log

### Level 2 — Application
4. **clue1.txt** — Log Rotation Concept: Growing System Logs
5. **clue2.txt** — Append to Existing File: Working with data/existing_log.txt
6. **clue3.txt** — Build a Diary File: Timestamped Entries

### Level 3 — Mastery
7. **clue1.txt** — Append in a Loop: Writing All Iterations
8. **clue2.txt** — Combining > and >>: The Professional Pattern
9. **clue3.txt** — Final Challenge: Audit Trail

---

## Getting Started

```bash
cat start_here.txt
cd clues/level1
cat clue1.txt
```

---

## Data Files

- `data/existing_log.txt` — A pre-existing system log with 10 entries
