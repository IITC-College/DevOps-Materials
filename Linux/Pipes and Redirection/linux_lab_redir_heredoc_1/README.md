# Linux Lab - Here-Document with << (Part 1)

---

## Installation Instructions

### Method 1: Download with curl (Recommended)

```bash
curl -L -o lab.tar.gz https://github.com/IITC-College/DevOps-Materials/releases/download/v5.0-pipes-redirection/linux_lab_redir_heredoc_1.tar.gz
tar -xzf lab.tar.gz
cd linux_lab_redir_heredoc_1
```

### Method 2: Clone the repository

```bash
git clone https://github.com/IITC-College/DevOps-Materials.git
cd DevOps-Materials/Linux/Pipes\ and\ Redirection/linux_lab_redir_heredoc_1
```

---

## Theme: Writing Multi-line Input Inline

---

## What is a Heredoc?

The `<<` operator is a special form of **input redirection** that lets you type (or write)
multi-line input **directly in a command**, ending with a delimiter word (usually `EOF`).

Instead of `<` which reads from a **file**, `<<` lets you write the content **inline** in
the command itself. The content ends when the delimiter (`EOF` by default) appears on its
own line with no leading or trailing spaces.

Basic syntax:

```bash
cat << EOF
line one
line two
EOF
```

Everything between `<< EOF` and the closing `EOF` is sent as input to the command.

---

## Objectives

By the end of this lab you will be able to:

1. Understand what a heredoc is and how `<<` works
2. Use `cat << EOF` to produce multi-line output
3. Redirect a heredoc to a file with `<< >`
4. Use variables and command substitutions inside heredocs
5. Use a **quoted heredoc** (`<< 'EOF'`) to suppress variable expansion
6. Use custom delimiters instead of `EOF`
7. Create configuration files using heredoc
8. Write a script body using heredoc
9. Generate HTML files using heredoc

---

## Exercise List

| Level | Exercise | Title |
|-------|----------|-------|
| 1 | 1 | What is a Heredoc? cat << EOF |
| 1 | 2 | Heredoc to a File: << with > |
| 1 | 3 | Variables in Heredocs: Dynamic Content |
| 2 | 1 | Write a Script Body with Heredoc |
| 2 | 2 | Custom Delimiter: Not Just EOF |
| 2 | 3 | Suppress Variable Expansion: Quoted Heredoc |
| 3 | 1 | Write a Config File with Heredoc |
| 3 | 2 | Heredoc in a Script: Generate a Report Template |
| 3 | 3 | Final Challenge: Generate HTML with Variables |

---

## How to Start

```bash
cat start_here.txt
```
