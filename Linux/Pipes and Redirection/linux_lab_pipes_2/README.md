# Linux Lab - Pipes with | (Part 2)

---

## Installation Instructions

### Method 1: Download with curl (Recommended)

```bash
curl -L -o lab.tar.gz https://github.com/IITC-College/DevOps-Materials/releases/download/v5.0-pipes-redirection/linux_lab_pipes_2.tar.gz
tar -xzf lab.tar.gz
cd linux_lab_pipes_2
```

### Method 2: Clone the repository

```bash
git clone https://github.com/IITC-College/DevOps-Materials.git
cd DevOps-Materials/Linux/Pipes\ and\ Redirection/linux_lab_pipes_2
```

---

## Theme: Pipes in Practice — Real-World Data Processing

---

## Prerequisite

Complete **Linux Lab - Pipes with | (Part 1)** before starting this lab.
You should be comfortable with:
- The basic pipe operator `|`
- `grep`, `sort`, `uniq`, `wc -l` in pipelines
- The concept of left-to-right data flow

---

## What You Will Learn in Part 2

Part 1 introduced the fundamentals. Part 2 applies pipes to real-world
scenarios that DevOps engineers and system administrators face daily:

- **Process monitoring** with `ps aux | grep`
- **Selective viewing** with `head` and `tail` in pipelines
- **Column extraction** with `cut` for CSV processing
- **Text transformation** with `tr` for case conversion
- **Frequency analysis** with `cut | sort | uniq -c | sort -rn`
- **Output splitting** with `tee` (write to screen AND file simultaneously)
- **Combining pipes with redirection** (`>`, `>>`) for saved reports

---

## Lab Objectives

By the end of this lab you will be able to:

- Use `ps aux | grep` to find and monitor specific processes
- Use `head` and `tail` to slice specific sections of output
- Use `cut` with pipes to extract CSV columns
- Build multi-step text transformation pipelines with `tr`
- Find top-N entries from any dataset using `uniq -c | sort -rn | head`
- Use `tee` to simultaneously display and save pipeline output
- Combine pipes and redirection in a single command
- Generate a full web access log report using only pipes

---

## Lab Structure

```
linux_lab_pipes_2/
├── README.md               <- You are here
├── start_here.txt          <- Start here for orientation
├── clues/
│   ├── level1/
│   │   ├── clue1.txt       <- Process Search: ps aux | grep
│   │   ├── clue2.txt       <- Head and Tail via Pipes
│   │   └── clue3.txt       <- Column Extraction: pipe with cut
│   ├── level2/
│   │   ├── clue1.txt       <- Multi-Step Text Processing
│   │   ├── clue2.txt       <- Find Top Entries: Access Log Analysis
│   │   └── clue3.txt       <- tee: Split Output to Both Screen and File
│   └── level3/
│       ├── clue1.txt       <- Combine Pipe with Redirection
│       ├── clue2.txt       <- Process Monitoring: Top Resource Users
│       └── clue3.txt       <- Final Challenge: Full Web Log Analysis
├── data/
│   ├── server.log          <- Application log (same as Part 1)
│   ├── big_file.txt        <- 50-line numbered file for head/tail practice
│   ├── employees.csv       <- CSV file with name, department, salary
│   ├── mixed.txt           <- Words in mixed case for tr practice
│   └── web_access.log      <- Web server access log (80 entries)
└── .answers/
    └── solutions.txt       <- Instructor solutions (check after completing)
```

---

## New Commands in This Lab

| Command              | Purpose                                                    |
|----------------------|------------------------------------------------------------|
| `head -N`            | Show only the first N lines of input                       |
| `tail -N`            | Show only the last N lines of input                        |
| `tail -n +N`         | Skip the first N-1 lines (start from line N)              |
| `cut -d',' -f2`      | Extract field 2 from comma-delimited input                 |
| `tr 'a-z' 'A-Z'`     | Translate (replace) lowercase letters with uppercase       |
| `tee filename`       | Write stdin to both stdout and a file simultaneously       |
| `tee -a filename`    | Like tee but appends to the file instead of overwriting    |
| `sort -k3 -rn`       | Sort by column 3, numerically, largest first               |
| `awk '$3 > 0.1'`     | Print lines where column 3 is greater than 0.1            |

---

## How to Start

```bash
cd linux_lab_pipes_2
cat start_here.txt
```

---

## Saving Your Answers

```bash
echo "your answer here" >> ../../my_answers.txt
```

---

Good luck! Build on what you learned in Part 1.
