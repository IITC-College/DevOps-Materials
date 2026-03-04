# Linux Lab - Here-Document with << (Part 2)

---

## Installation Instructions

### Method 1: Download with curl (Recommended)

```bash
curl -L -o lab.tar.gz https://github.com/IITC-College/DevOps-Materials/releases/download/v5.0-pipes-redirection/linux_lab_redir_heredoc_2.tar.gz
tar -xzf lab.tar.gz
cd linux_lab_redir_heredoc_2
```

### Method 2: Clone the repository

```bash
git clone https://github.com/IITC-College/DevOps-Materials.git
cd DevOps-Materials/Linux/Pipes\ and\ Redirection/linux_lab_redir_heredoc_2
```

---

## Theme: Heredoc in Real Scenarios

---

## Prerequisite

**Part 1 must be completed before starting this lab.**

You should already be comfortable with:
- Basic heredoc syntax (`cat << EOF`)
- Redirecting heredoc to a file (`<< >`)
- Variable expansion in heredocs
- Quoted heredoc to suppress expansion (`<< 'EOF'`)
- Custom delimiters

---

## Objectives

By the end of this lab you will be able to:

1. Replace multiple `echo` commands with a single heredoc
2. Append multi-line blocks to files using `<< >>`
3. Pass a heredoc to commands other than `cat` (sort, wc, tr)
4. Simulate multi-line SQL/query blocks using heredoc
5. Use indented heredoc (`<<-`) to strip leading tabs in scripts
6. Generate deployment notes with dynamic variables
7. Identify and fix common heredoc syntax bugs
8. Generate scripts from scripts using nested heredocs

---

## Exercise List

| Level | Exercise | Title |
|-------|----------|-------|
| 1 | 1 | Review: Basic Heredoc — Quick Practice |
| 1 | 2 | Replace Multiple Echos with One Heredoc |
| 1 | 3 | Heredoc to Append: << >> Combination |
| 2 | 1 | Pass Heredoc to a Command: sort << EOF |
| 2 | 2 | SQL-like Multi-line Commands with Heredoc |
| 2 | 3 | Indented Heredoc: <<- for Cleaner Scripts |
| 3 | 1 | Generate Deployment Notes with Variables |
| 3 | 2 | Fix the Broken Heredoc |
| 3 | 3 | Final: Script Generator — Heredoc Inside a Script |

---

## How to Start

```bash
cat start_here.txt
```
