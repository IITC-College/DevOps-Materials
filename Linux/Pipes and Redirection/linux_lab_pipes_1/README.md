# Linux Lab - Pipes with | (Part 1)

---

## Installation Instructions

### Method 1: Download with curl (Recommended)

```bash
curl -L -o lab.tar.gz https://github.com/IITC-College/DevOps-Materials/releases/download/v5.0-pipes-redirection/linux_lab_pipes_1.tar.gz
tar -xzf lab.tar.gz
cd linux_lab_pipes_1
```

### Method 2: Clone the repository

```bash
git clone https://github.com/IITC-College/DevOps-Materials.git
cd DevOps-Materials/Linux/Pipes\ and\ Redirection/linux_lab_pipes_1
```

---

## Theme: Connecting Commands

---

## What is a Pipe?

The `|` (pipe) operator connects the **stdout** of one command to the **stdin** of the next.
It creates a pipeline of commands that transform data step by step.

```
command1 | command2 | command3
```

Data flows **left to right**. The output of `command1` becomes the input of `command2`,
and the output of `command2` becomes the input of `command3`.

---

## Why Use Pipes?

Without pipes, you would need temporary files:

```bash
# Without pipes (awkward):
ls > /tmp/listing.txt
wc -l /tmp/listing.txt
rm /tmp/listing.txt

# With pipes (clean and direct):
ls | wc -l
```

Pipes let you compose small, focused commands into powerful one-liners.

---

## Lab Objectives

By the end of this lab you will be able to:

- Understand what a pipe does and why it exists
- Connect two or more commands with `|`
- Understand the left-to-right data flow in a pipeline
- Use `grep`, `sort`, `wc`, `uniq` together with pipes
- Build multi-command pipelines (3+ commands)
- Count and analyze data using pipes
- Extract meaningful information from log files with pipe chains

---

## Lab Structure

```
linux_lab_pipes_1/
├── README.md               <- You are here
├── start_here.txt          <- Start here for orientation
├── clues/
│   ├── level1/
│   │   ├── clue1.txt       <- What is a Pipe? ls | cat
│   │   ├── clue2.txt       <- Paginate Long Output: Pipe to less
│   │   └── clue3.txt       <- Count Files: ls | wc -l
│   ├── level2/
│   │   ├── clue1.txt       <- Filter with grep: Find Specific Lines
│   │   ├── clue2.txt       <- Sort Piped Output: cat | sort
│   │   └── clue3.txt       <- Multi-Pipe Chain: sort | uniq
│   └── level3/
│       ├── clue1.txt       <- Count Unique Values: Full Analytics Pipeline
│       ├── clue2.txt       <- Find and Process: ls -la | grep | wc
│       └── clue3.txt       <- Final Pipeline: Analyze data/access.log
├── data/
│   ├── server.log          <- Application log with INFO/WARN/ERROR entries
│   ├── names.txt           <- List of names (some duplicates)
│   └── access.log          <- Web server access log
└── .answers/
    └── solutions.txt       <- Instructor solutions (check after completing)
```

---

## Quick Reference: Common Pipeline Commands

| Command        | Purpose                                      |
|----------------|----------------------------------------------|
| `grep "text"`  | Filter lines matching a pattern              |
| `sort`         | Sort lines alphabetically                    |
| `sort -r`      | Sort in reverse order                        |
| `sort -n`      | Sort numerically                             |
| `sort -rn`     | Sort numerically in reverse (largest first)  |
| `wc -l`        | Count the number of lines                    |
| `uniq`         | Remove consecutive duplicate lines          |
| `uniq -c`      | Count occurrences of each line               |
| `head -N`      | Show only the first N lines                  |
| `tail -N`      | Show only the last N lines                   |
| `cut -d: -f1`  | Extract column 1 using `:` as delimiter      |
| `less`         | Scroll through long output (q to quit)       |

---

## How to Start

```bash
cd linux_lab_pipes_1
cat start_here.txt
```

Then follow the clues starting from `clues/level1/clue1.txt`.

---

## Saving Your Answers

Throughout the lab you will be asked questions. Save your answers with:

```bash
echo "your answer here" >> ../../my_answers.txt
```

---

Good luck!
