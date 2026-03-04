# Linux Lab - Output Redirection with `>` (Part 1)

## Lab Overview

**Topic:** Output Redirection — The `>` Operator
**Theme:** "Your First Redirected Output"
**Difficulty:** Beginner → Intermediate

In this lab you will discover how to redirect the output of commands into files instead of the terminal screen. You will learn what stdout is, how `>` works, and — crucially — its most important gotcha: it overwrites existing content.

---

## Installation Instructions

### Method 1: Download with curl (Recommended)

```bash
curl -L -o lab.tar.gz https://github.com/IITC-College/DevOps-Materials/releases/download/v5.0-pipes-redirection/linux_lab_redir_output_overwrite_1.tar.gz
tar -xzf lab.tar.gz
cd linux_lab_redir_output_overwrite_1
```

### Method 2: Clone the repository

```bash
git clone https://github.com/IITC-College/DevOps-Materials.git
cd DevOps-Materials/Linux/Pipes\ and\ Redirection/linux_lab_redir_output_overwrite_1
```

---

---

## Lab Objective

By the end of this lab you will be able to:

- Explain what **stdout** is and where it normally goes
- Use `>` to redirect command output into a file
- Understand that `>` **overwrites** the destination file
- Distinguish between stdout and stderr when redirecting
- Save real command output to files for later use

---

## Lab Structure

```
clues/
├── level1/       ← Foundations: understanding stdout and basic redirection
│   ├── clue1.txt
│   ├── clue2.txt
│   └── clue3.txt
├── level2/       ← Application: overwrite behavior and stderr vs stdout
│   ├── clue1.txt
│   ├── clue2.txt
│   └── clue3.txt
└── level3/       ← Mastery: real-world report building and debugging
    ├── clue1.txt
    ├── clue2.txt
    └── clue3.txt
```

---

## Exercise List

### Level 1 — Foundations
1. **clue1.txt** — What is stdout? First redirection
2. **clue2.txt** — Redirect a command's output to a file
3. **clue3.txt** — Redirect `date` and `whoami` to separate files

### Level 2 — Application
4. **clue1.txt** — The overwrite danger: losing data with `>`
5. **clue2.txt** — stdout vs stderr: what `>` does NOT capture
6. **clue3.txt** — Saving real system info to log files

### Level 3 — Mastery
7. **clue1.txt** — Multi-step snapshot builder
8. **clue2.txt** — Working with provided data files
9. **clue3.txt** — Spot the bug: overwrite in a loop

---

## Getting Started

```bash
cat start_here.txt
cd clues/level1
cat clue1.txt
```

---

## Data Files

The `data/` directory contains:
- `app.log` — Sample application log with INFO, WARN, and ERROR lines
- `names.txt` — A list of names for redirection exercises

---

## Tips

- Use `cat <filename>` after every redirection to verify the file was created
- Keep a terminal window open to track which files you have created
- Write your answers and observations in `my_answers.txt` at the lab root
