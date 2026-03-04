# Pipes and Redirection Labs

Hands-on labs for Linux input/output redirection and pipes. Each topic has two progressive labs with 3 levels × 3 exercises each (9 exercises per lab).

---

## Labs

| Lab | Operator | Theme | Download |
|-----|----------|-------|----------|
| [linux_lab_redir_output_overwrite_1](linux_lab_redir_output_overwrite_1/) | `>` | Your First Redirected Output | [↓ tar.gz](https://github.com/IITC-College/DevOps-Materials/releases/download/v5.0-pipes-redirection/linux_lab_redir_output_overwrite_1.tar.gz) |
| [linux_lab_redir_output_overwrite_2](linux_lab_redir_output_overwrite_2/) | `>` | Redirecting in Context | [↓ tar.gz](https://github.com/IITC-College/DevOps-Materials/releases/download/v5.0-pipes-redirection/linux_lab_redir_output_overwrite_2.tar.gz) |
| [linux_lab_redir_output_append_1](linux_lab_redir_output_append_1/) | `>>` | Building Files Over Time | [↓ tar.gz](https://github.com/IITC-College/DevOps-Materials/releases/download/v5.0-pipes-redirection/linux_lab_redir_output_append_1.tar.gz) |
| [linux_lab_redir_output_append_2](linux_lab_redir_output_append_2/) | `>>` | Append in Practice | [↓ tar.gz](https://github.com/IITC-College/DevOps-Materials/releases/download/v5.0-pipes-redirection/linux_lab_redir_output_append_2.tar.gz) |
| [linux_lab_redir_input_1](linux_lab_redir_input_1/) | `<` | Feeding Files to Commands | [↓ tar.gz](https://github.com/IITC-College/DevOps-Materials/releases/download/v5.0-pipes-redirection/linux_lab_redir_input_1.tar.gz) |
| [linux_lab_redir_input_2](linux_lab_redir_input_2/) | `<` | Input Redirection in Practice | [↓ tar.gz](https://github.com/IITC-College/DevOps-Materials/releases/download/v5.0-pipes-redirection/linux_lab_redir_input_2.tar.gz) |
| [linux_lab_redir_heredoc_1](linux_lab_redir_heredoc_1/) | `<<` | Writing Multi-line Input Inline | [↓ tar.gz](https://github.com/IITC-College/DevOps-Materials/releases/download/v5.0-pipes-redirection/linux_lab_redir_heredoc_1.tar.gz) |
| [linux_lab_redir_heredoc_2](linux_lab_redir_heredoc_2/) | `<<` | Heredoc in Real Scenarios | [↓ tar.gz](https://github.com/IITC-College/DevOps-Materials/releases/download/v5.0-pipes-redirection/linux_lab_redir_heredoc_2.tar.gz) |
| [linux_lab_pipes_1](linux_lab_pipes_1/) | `\|` | Connecting Commands | [↓ tar.gz](https://github.com/IITC-College/DevOps-Materials/releases/download/v5.0-pipes-redirection/linux_lab_pipes_1.tar.gz) |
| [linux_lab_pipes_2](linux_lab_pipes_2/) | `\|` | Pipes in Practice | [↓ tar.gz](https://github.com/IITC-College/DevOps-Materials/releases/download/v5.0-pipes-redirection/linux_lab_pipes_2.tar.gz) |

---

## Recommended Order

```
> (overwrite) → >> (append) → < (input) → << (heredoc) → | (pipes)
```

Each topic's Lab 1 teaches the concept, Lab 2 applies it in realistic scenarios.

---

## Quick Start

```bash
# Download a single lab
curl -L -o lab.tar.gz https://github.com/IITC-College/DevOps-Materials/releases/download/v5.0-pipes-redirection/linux_lab_redir_output_overwrite_1.tar.gz
tar -xzf lab.tar.gz
cd linux_lab_redir_output_overwrite_1
cat start_here.txt
```

---

## Lab Structure (all labs)

```
lab_name/
├── README.md
├── start_here.txt
├── clues/
│   ├── level1/  clue1.txt  clue2.txt  clue3.txt
│   ├── level2/  clue1.txt  clue2.txt  clue3.txt
│   └── level3/  clue1.txt  clue2.txt  clue3.txt
├── data/        (provided sample files)
└── .answers/    solutions.txt  (instructor only)
```
