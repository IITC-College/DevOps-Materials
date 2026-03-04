# Linux Lab - Output Redirection with >> (Part 2)

---

## Installation Instructions

### Method 1: Download with curl (Recommended)

```bash
curl -L -o lab.tar.gz https://github.com/IITC-College/DevOps-Materials/releases/download/v5.0-pipes-redirection/linux_lab_redir_output_append_2.tar.gz
tar -xzf lab.tar.gz
cd linux_lab_redir_output_append_2
```

### Method 2: Clone the repository

```bash
git clone https://github.com/IITC-College/DevOps-Materials.git
cd DevOps-Materials/Linux/Pipes\ and\ Redirection/linux_lab_redir_output_append_2
```

---


## Theme: Append in Practice — Real-World Scenarios

This is **Part 2** of the Output Redirection lab series. Part 1 must be completed before starting this lab.

---

## Overview

In Part 1 you learned the mechanics of `>>` vs `>`. In Part 2 you apply those skills to real-world scenarios: building changelogs, collecting logs with grep, generating system reports, fixing bugs in scripts, simulating cron jobs, and writing rolling timestamped logs.

---

## Learning Objectives

By the end of this lab, you will be able to:

1. Append multiple command outputs to a single file, building it line by line
2. Watch a file grow with `wc -l` after each append operation
3. Build a professional changelog using a mix of `>` and `>>`
4. Use `grep` with `>>` for cumulative log collection and understand duplicate risks
5. Add formatted section headers to structure multi-section reports
6. Work with provided data files (inventory, server logs) and extend them with `>>`
7. Identify and fix the overwrite bug (`>` used where `>>` was needed)
8. Simulate cron job log entries using repeated `>>` appends
9. Build a rolling timestamped log with realistic log-format entries

---

## Lab Structure

```
linux_lab_redir_output_append_2/
├── README.md                  ← You are here
├── start_here.txt             ← Start here before opening any clue
├── clues/
│   ├── level1/
│   │   ├── clue1.txt          ← Exercise 1: Append Multiple Commands to One File
│   │   ├── clue2.txt          ← Exercise 2: Watching a File Grow with wc -l
│   │   └── clue3.txt          ← Exercise 3: Create a Changelog
│   ├── level2/
│   │   ├── clue1.txt          ← Exercise 4: Append with grep: Cumulative Warning Collection
│   │   ├── clue2.txt          ← Exercise 5: Adding Headers Between Sections
│   │   └── clue3.txt          ← Exercise 6: Given File + Append (data/inventory.txt)
│   └── level3/
│       ├── clue1.txt          ← Exercise 7: Spot the Bug: > Where >> Was Needed
│       ├── clue2.txt          ← Exercise 8: Simulated Cron Job: Hourly Log Entries
│       └── clue3.txt          ← Exercise 9: Final Challenge: Rolling Log with Timestamps
├── data/
│   ├── server.log             ← Provided: 30-line server log with 6 WARN entries
│   ├── inventory.txt          ← Provided: 20-item CSV inventory file
│   └── broken_append_script.sh← Provided: Buggy script using > instead of >>
└── .answers/
    └── solutions.txt          ← Instructor solutions (do not open until finished)
```

---

## Exercise List

| # | Level | File | Title |
|---|-------|------|-------|
| 1 | 1 | clues/level1/clue1.txt | Append Multiple Commands to One File |
| 2 | 1 | clues/level1/clue2.txt | Watching a File Grow: wc -l After Each Append |
| 3 | 1 | clues/level1/clue3.txt | Create a Changelog: Building Version History |
| 4 | 2 | clues/level2/clue1.txt | Append with grep: Cumulative Warning Collection |
| 5 | 2 | clues/level2/clue2.txt | Adding Headers Between Sections |
| 6 | 2 | clues/level2/clue3.txt | Given File + Append: Adding to data/inventory.txt |
| 7 | 3 | clues/level3/clue1.txt | Spot the Bug: > Where >> Was Needed |
| 8 | 3 | clues/level3/clue2.txt | Simulated Cron Job: Hourly Log Entries |
| 9 | 3 | clues/level3/clue3.txt | Final Challenge: Rolling Log with Timestamps |

---

## Prerequisites

- Completion of Linux Lab - Output Redirection with >> (Part 1)
- Basic familiarity with: `echo`, `cat`, `grep`, `wc`, `date`, `df`, `free`, `hostname`, `whoami`
- Understanding that `>` overwrites and `>>` appends

---

## Estimated Time

60-75 minutes

---

## How to Start

```bash
cd "c:/DevOps/DevOps-Jan26/Linux/Pipes and Redirection/linux_lab_redir_output_append_2"
cat start_here.txt
```

---

## Grading

- Level 1 (Exercises 1-3): 3 points
- Level 2 (Exercises 4-6): 3 points
- Level 3 (Exercises 7-9): 3 points
- **Total: 9 points**
