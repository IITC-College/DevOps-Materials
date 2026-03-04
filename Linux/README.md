# Linux

Hands-on Linux fundamentals for DevOps. Topics progress from basic navigation to scripting and system administration.

## Sections

| Folder | Topics |
|--------|--------|
| [Files and Folders navigation](Files%20and%20Folders%20navigation/) | Navigation, file management, reading files, searching |
| [Permissions](Permissions/) | File permissions, ownership, groups, sudo, umask |
| [Users and Groups](Users%20and%20Groups/) | Creating and managing users and groups |
| [Processes](Processes/) | Processes, services, systemd, journalctl, troubleshooting |
| [Networking](Networking/) | Network adapters, basic connectivity |
| [Shell Scripting](Shell%20Scripting/) | Bash scripting: variables, conditions, loops, functions |
| [Pipes and Redirection](Pipes%20and%20Redirection/) | `>`, `>>`, `<`, `<<`, `\|` — redirecting and piping data |

---

## Permissions Labs — Download

**Release:** [v6.0-permissions](https://github.com/IITC-College/DevOps-Materials/releases/tag/v6.0-permissions)

```bash
# Lab 6: Permission Encounter — Reading and understanding permissions
curl -L -o lab.tar.gz https://github.com/IITC-College/DevOps-Materials/releases/download/v6.0-permissions/linux_lab6_permission_encounter.tar.gz
tar -xzf lab.tar.gz && cd linux_lab6_permission_encounter

# Lab 7: Why Script Doesn't Run — Diagnosing execute permission issues
curl -L -o lab.tar.gz https://github.com/IITC-College/DevOps-Materials/releases/download/v6.0-permissions/linux_lab7_why_script_doesnt_run.tar.gz
tar -xzf lab.tar.gz && cd linux_lab7_why_script_doesnt_run

# Lab 8: Ownership and Groups — Changing ownership with chown/chgrp
curl -L -o lab.tar.gz https://github.com/IITC-College/DevOps-Materials/releases/download/v6.0-permissions/linux_lab8_ownership_and_groups.tar.gz
tar -xzf lab.tar.gz && cd linux_lab8_ownership_and_groups

# Lab 9: Sudo Mindset — Understanding when and how to use sudo
curl -L -o lab.tar.gz https://github.com/IITC-College/DevOps-Materials/releases/download/v6.0-permissions/linux_lab9_sudo_mindset.tar.gz
tar -xzf lab.tar.gz && cd linux_lab9_sudo_mindset

# Lab 10: Default Permissions — Controlling defaults with umask
curl -L -o lab.tar.gz https://github.com/IITC-College/DevOps-Materials/releases/download/v6.0-permissions/linux_lab10_default_permissions.tar.gz
tar -xzf lab.tar.gz && cd linux_lab10_default_permissions

# Lab 11: Debug Mindset — Debugging mixed permission scenarios
curl -L -o lab.tar.gz https://github.com/IITC-College/DevOps-Materials/releases/download/v6.0-permissions/linux_lab11_debug_mindset.tar.gz
tar -xzf lab.tar.gz && cd linux_lab11_debug_mindset
```

---

## Pipes and Redirection Labs — Download

**Release:** [v5.0-pipes-redirection](https://github.com/IITC-College/DevOps-Materials/releases/tag/v5.0-pipes-redirection)

```bash
# > Output Redirection (Overwrite) — Lab 1
curl -L -o lab.tar.gz https://github.com/IITC-College/DevOps-Materials/releases/download/v5.0-pipes-redirection/linux_lab_redir_output_overwrite_1.tar.gz
tar -xzf lab.tar.gz && cd linux_lab_redir_output_overwrite_1

# > Output Redirection (Overwrite) — Lab 2
curl -L -o lab.tar.gz https://github.com/IITC-College/DevOps-Materials/releases/download/v5.0-pipes-redirection/linux_lab_redir_output_overwrite_2.tar.gz
tar -xzf lab.tar.gz && cd linux_lab_redir_output_overwrite_2

# >> Output Redirection (Append) — Lab 1
curl -L -o lab.tar.gz https://github.com/IITC-College/DevOps-Materials/releases/download/v5.0-pipes-redirection/linux_lab_redir_output_append_1.tar.gz
tar -xzf lab.tar.gz && cd linux_lab_redir_output_append_1

# >> Output Redirection (Append) — Lab 2
curl -L -o lab.tar.gz https://github.com/IITC-College/DevOps-Materials/releases/download/v5.0-pipes-redirection/linux_lab_redir_output_append_2.tar.gz
tar -xzf lab.tar.gz && cd linux_lab_redir_output_append_2

# < Input Redirection — Lab 1
curl -L -o lab.tar.gz https://github.com/IITC-College/DevOps-Materials/releases/download/v5.0-pipes-redirection/linux_lab_redir_input_1.tar.gz
tar -xzf lab.tar.gz && cd linux_lab_redir_input_1

# < Input Redirection — Lab 2
curl -L -o lab.tar.gz https://github.com/IITC-College/DevOps-Materials/releases/download/v5.0-pipes-redirection/linux_lab_redir_input_2.tar.gz
tar -xzf lab.tar.gz && cd linux_lab_redir_input_2

# << Here-Document — Lab 1
curl -L -o lab.tar.gz https://github.com/IITC-College/DevOps-Materials/releases/download/v5.0-pipes-redirection/linux_lab_redir_heredoc_1.tar.gz
tar -xzf lab.tar.gz && cd linux_lab_redir_heredoc_1

# << Here-Document — Lab 2
curl -L -o lab.tar.gz https://github.com/IITC-College/DevOps-Materials/releases/download/v5.0-pipes-redirection/linux_lab_redir_heredoc_2.tar.gz
tar -xzf lab.tar.gz && cd linux_lab_redir_heredoc_2

# | Pipes — Lab 1
curl -L -o lab.tar.gz https://github.com/IITC-College/DevOps-Materials/releases/download/v5.0-pipes-redirection/linux_lab_pipes_1.tar.gz
tar -xzf lab.tar.gz && cd linux_lab_pipes_1

# | Pipes — Lab 2
curl -L -o lab.tar.gz https://github.com/IITC-College/DevOps-Materials/releases/download/v5.0-pipes-redirection/linux_lab_pipes_2.tar.gz
tar -xzf lab.tar.gz && cd linux_lab_pipes_2
```
