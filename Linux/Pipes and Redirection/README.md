# Pipes and Redirection Labs

Hands-on labs for Linux input/output redirection and pipes. Each topic has two progressive labs with 3 levels × 3 exercises each (9 exercises per lab).

---

## Labs

| Lab | Operator | Theme |
|-----|----------|-------|
| [linux_lab_redir_output_overwrite_1](linux_lab_redir_output_overwrite_1/) | `>` | Your First Redirected Output |
| [linux_lab_redir_output_overwrite_2](linux_lab_redir_output_overwrite_2/) | `>` | Redirecting in Context |
| [linux_lab_redir_output_append_1](linux_lab_redir_output_append_1/) | `>>` | Building Files Over Time |
| [linux_lab_redir_output_append_2](linux_lab_redir_output_append_2/) | `>>` | Append in Practice |
| [linux_lab_redir_input_1](linux_lab_redir_input_1/) | `<` | Feeding Files to Commands |
| [linux_lab_redir_input_2](linux_lab_redir_input_2/) | `<` | Input Redirection in Practice |
| [linux_lab_redir_heredoc_1](linux_lab_redir_heredoc_1/) | `<<` | Writing Multi-line Input Inline |
| [linux_lab_redir_heredoc_2](linux_lab_redir_heredoc_2/) | `<<` | Heredoc in Real Scenarios |
| [linux_lab_pipes_1](linux_lab_pipes_1/) | `\|` | Connecting Commands |
| [linux_lab_pipes_2](linux_lab_pipes_2/) | `\|` | Pipes in Practice |

---

## Recommended Order

```
> (overwrite) → >> (append) → < (input) → << (heredoc) → | (pipes)
```

Each topic's Lab 1 teaches the concept, Lab 2 applies it in realistic scenarios.

---

## Getting Started (any lab)

```bash
cd linux_lab_redir_output_overwrite_1
cat start_here.txt
cd clues/level1
cat clue1.txt
```
