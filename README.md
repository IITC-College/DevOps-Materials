# DevOps-Jan26 Course Materials

## 📚 Overview

This repository contains all lab materials for the DevOps January 2026 course. Each module includes hands-on labs designed for practical learning and skill development.

---

## 🗂️ Repository Structure

```
DevOps-Jan26/
├── README.md                      ← You are here
├── LAB_WORKFLOW.md                ← Complete lab creation workflow
├── LAB_DESIGN_SPEC.md             ← Lab design principles
├── create_and_deploy_lab.sh       ← Automation script
│
└── [Module Name]/
    ├── [lab_name]/                ← Lab content
    ├── [lab_name].tar.gz          ← Distribution archive
    └── STUDENT_COMMAND.txt        ← Download instructions
```

---

## 📦 Available Modules

### Linux Module

Labs are numbered in the order they should be completed, following the course structure.

#### Files and Folders Navigation

| # | Topic | Download |
|---|--------|----------|
| 1 | Navigation Basics (cd, ls, hidden files) | `curl -L https://github.com/IITC-College/DevOps-Jan26/releases/download/v2.0/linux_lab1_navigation_basics.tar.gz &#124; tar -xz && cd linux_lab1_navigation_basics && cat start_here.txt` |
| 2 | File and Directory Management (mkdir, touch, cp, mv, rm) | `curl -L https://github.com/IITC-College/DevOps-Jan26/releases/download/v2.1/linux_lab2_file_management.tar.gz &#124; tar -xz && cd linux_lab2_file_management && cat start_here.txt` |
| 3 | Reading Files (cat, less, head, tail) | `curl -L https://github.com/IITC-College/DevOps-Jan26/releases/download/v2.2/linux_lab3_reading_files.tar.gz &#124; tar -xz && cd linux_lab3_reading_files && cat start_here.txt` |
| 4 | Search Basics (grep, find) | `curl -L https://github.com/IITC-College/DevOps-Jan26/releases/download/v2.3/linux_lab4_search_basics.tar.gz &#124; tar -xz && cd linux_lab4_search_basics && cat start_here.txt` |
| 5 | File System Scavenger Hunt (capstone) | `curl -L https://github.com/IITC-College/DevOps-Jan26/releases/download/v2.4/linux_lab5_scavenger_hunt.tar.gz &#124; tar -xz && cd linux_lab5_scavenger_hunt && cat start_here.txt` |

#### Permissions

| # | Topic | Download |
|---|--------|----------|
| 6 | Permission Encounter (reading permissions) | `curl -L https://github.com/IITC-College/DevOps-Jan26/releases/download/v2.5/linux_lab6_permission_encounter.tar.gz &#124; tar -xz && cd linux_lab6_permission_encounter && cd clues/level1 && cat clue1.txt` |
| 7 | Why Script Doesn't Run (chmod, execute) | `curl -L https://github.com/IITC-College/DevOps-Jan26/releases/download/v2.6/linux_lab7_why_script_doesnt_run.tar.gz &#124; tar -xz && cd linux_lab7_why_script_doesnt_run && cd clues/level1 && cat clue1.txt` |
| 8 | Ownership and Groups (chown, groups) | `curl -L https://github.com/IITC-College/DevOps-Jan26/releases/download/v2.7/linux_lab8_ownership_and_groups.tar.gz &#124; tar -xz && cd linux_lab8_ownership_and_groups && cd clues/level1 && cat clue1.txt` |
| 9 | Understanding sudo | `curl -L https://github.com/IITC-College/DevOps-Jan26/releases/download/v2.8/linux_lab9_sudo_mindset.tar.gz &#124; tar -xz && cd linux_lab9_sudo_mindset && cd clues/level1 && cat clue1.txt` |
| 10 | Default Permissions (umask) | `curl -L https://github.com/IITC-College/DevOps-Jan26/releases/download/v2.10/linux_lab10_default_permissions.tar.gz &#124; tar -xz && cd linux_lab10_default_permissions && cd clues/level1 && cat clue1.txt` |
| 11 | Debug Mindset (permission debugging) | `curl -L https://github.com/IITC-College/DevOps-Jan26/releases/download/v4.1/linux_lab11_debug_mindset.tar.gz &#124; tar -xz && cd linux_lab11_debug_mindset && cd clues/level1 && cat clue1.txt` |

#### Processes and Services

| # | Topic | Download |
|---|--------|----------|
| 12 | Processes Basics (ps, top, htop) | `curl -L https://github.com/IITC-College/DevOps-Jan26/releases/download/v1.1-processes-basics/linux_lab_processes_basics.tar.gz &#124; tar -xz && cd linux_lab_processes_basics && cd clues/level1 && cat clue1.txt` |
| 13 | Process Management (kill, SIGTERM/SIGKILL) | `curl -L https://github.com/IITC-College/DevOps-Jan26/releases/download/v1.0/linux_lab_processes_kill.tar.gz &#124; tar -xz && cd linux_lab_processes_kill && cd clues/level1 && cat clue1.txt` |
| 14 | Process vs Service | `curl -L https://github.com/IITC-College/DevOps-Jan26/releases/download/v1.0/linux_lab_processes_vs_service.tar.gz &#124; tar -xz && cd linux_lab_processes_vs_service && cd clues/level1 && cat clue1.txt` |
| 15 | systemd and Services (systemctl) | `curl -L https://github.com/IITC-College/DevOps-Jan26/releases/download/v1.0/linux_lab_systemd_services.tar.gz &#124; tar -xz && cd linux_lab_systemd_services && cd clues/level1 && cat clue1.txt` |
| 16 | Logs-First (journalctl) | `curl -L https://github.com/IITC-College/DevOps-Jan26/releases/download/v1.1-journalctl-logs/linux_lab_journalctl_logs_first.tar.gz &#124; tar -xz && cd linux_lab_journalctl_logs_first && cd clues/level1 && cat clue1.txt` |
| 17 | Troubleshooting Flow (5-step method) | `curl -L https://github.com/IITC-College/DevOps-Jan26/releases/download/v1.0/linux_lab_troubleshooting_flow.tar.gz &#124; tar -xz && cd linux_lab_troubleshooting_flow && cd clues/level1 && cat clue1.txt` |

#### Shell Scripting

Hands-on bash scripting: **TASKS.md** (requirements, no full code to copy), **HINTS.md** (solutions when stuck), **src/** (starter files). **Hardened format (v1.1)** — [Release notes](https://github.com/IITC-College/DevOps-Jan26/releases/tag/v1.1-shell-scripting-hardened).

| # | Topic | Download |
|---|--------|----------|
| 18 | Script Basics (shebang, chmod, execution) | `curl -L https://github.com/IITC-College/DevOps-Jan26/releases/download/v1.1-script-basics/linux_lab_script_basics.tar.gz &#124; tar -xz && cd linux_lab_script_basics && cat TASKS.md` |
| 19 | Variables (command substitution, timestamps) | `curl -L https://github.com/IITC-College/DevOps-Jan26/releases/download/v1.1-script-variables/linux_lab_script_variables.tar.gz &#124; tar -xz && cd linux_lab_script_variables && cat TASKS.md` |
| 20 | User Input (read, validation) | `curl -L https://github.com/IITC-College/DevOps-Jan26/releases/download/v1.1-script-input/linux_lab_script_input.tar.gz &#124; tar -xz && cd linux_lab_script_input && cat TASKS.md` |
| 21 | Conditionals (if/elif/else, validators) | `curl -L https://github.com/IITC-College/DevOps-Jan26/releases/download/v1.1-script-conditionals/linux_lab_script_conditionals.tar.gz &#124; tar -xz && cd linux_lab_script_conditionals && cat TASKS.md` |
| 22 | Case Statements (menus, pattern matching) | `curl -L https://github.com/IITC-College/DevOps-Jan26/releases/download/v1.1-script-case/linux_lab_script_case.tar.gz &#124; tar -xz && cd linux_lab_script_case && cat TASKS.md` |
| 23 | Loops (for, while, retry, nested) | `curl -L https://github.com/IITC-College/DevOps-Jan26/releases/download/v1.1-script-loops/linux_lab_script_loops.tar.gz &#124; tar -xz && cd linux_lab_script_loops && cat TASKS.md` |
| 24 | Functions (parameters, reusability) | `curl -L https://github.com/IITC-College/DevOps-Jan26/releases/download/v1.1-script-functions/linux_lab_script_functions.tar.gz &#124; tar -xz && cd linux_lab_script_functions && cat TASKS.md` |
| 25 | Exit Codes ($?, && and \|\|, CI/CD) | `curl -L https://github.com/IITC-College/DevOps-Jan26/releases/download/v1.1-script-exit-codes/linux_lab_script_exit_codes.tar.gz &#124; tar -xz && cd linux_lab_script_exit_codes && cat TASKS.md` |
| 26 | Debugging (bash errors, syntax) | `curl -L https://github.com/IITC-College/DevOps-Jan26/releases/download/v1.1-script-debugging/linux_lab_script_debugging.tar.gz &#124; tar -xz && cd linux_lab_script_debugging && cat TASKS.md` |
| 27 | Ops Helper Tool | `curl -L https://github.com/IITC-College/DevOps-Jan26/releases/download/v1.1-script-ops-helper/linux_lab_script_ops_helper.tar.gz &#124; tar -xz && cd linux_lab_script_ops_helper && cat TASKS.md` |
| 28 | Mini DevOps Tool (Capstone) | `curl -L https://github.com/IITC-College/DevOps-Jan26/releases/download/v1.1-script-mini-devops-tool/linux_lab_script_mini_devops_tool.tar.gz &#124; tar -xz && cd linux_lab_script_mini_devops_tool && cat TASKS.md` |
| 29 | Leap Year (arithmetic, conditionals) | `curl -L https://github.com/IITC-College/DevOps-Jan26/releases/download/v1.1-script-leap-year/linux_lab_script_leap_year.tar.gz &#124; tar -xz && cd linux_lab_script_leap_year && cat TASKS.md` |
| 30 | Number Guessing Game | `curl -L https://github.com/IITC-College/DevOps-Jan26/releases/download/v1.1-script-guessing-game/linux_lab_script_guessing_game.tar.gz &#124; tar -xz && cd linux_lab_script_guessing_game && cat TASKS.md` |

#### Networking

| # | Topic | Download |
|---|--------|----------|
| 31 | Network Adapter Debug (interfaces, IP, DNS, firewall) | `curl -L https://github.com/IITC-College/DevOps-Jan26/releases/download/v4.0/linux_networking_lab1_adapter.tar.gz &#124; tar -xz && cd linux_networking_lab1_adapter && cat README.md` |

#### Users and Groups

| # | Topic | Download |
|---|--------|----------|
| 32 | Users and Groups Management | Path: `Linux/Users and Groups/linux_users_groups_management/` — In development; requires instructor setup (see lab README). |

---

### Docker Module

#### Container Basics

| # | Topic | Download |
|---|--------|----------|
| 1 | Docker Container Basics (run, lifecycle, logs, exec) | `curl -L https://github.com/IITC-College/DevOps-Materials/releases/download/v1.0-docker-container-basics/docker_lab_basics.tar.gz &#124; tar -xz && cd docker_lab_basics && cat README.md` |

Open `TASKS.md` to begin the lab.

---

### Python Module

#### Python Basics (28 labs)

Hands-on coding labs with **TASKS.md** (requirements and objectives), **HINTS.md** (syntax tips and solutions). Run scripts with `python3 script_name.py`. Each archive extracts to a folder (e.g. `01_print_basics`); open `TASKS.md` to start.

| # | Topic | Download |
|---|--------|----------|
| 1 | Print, sep, and end | `curl -L https://github.com/IITC-College/DevOps-Materials/releases/download/v1.0-python-labs/python_lab_01_print_basics.tar.gz &#124; tar -xz && cd 01_print_basics && cat TASKS.md` |
| 2 | Literals and Data Types | `curl -L https://github.com/IITC-College/DevOps-Materials/releases/download/v1.0-python-labs/python_lab_02_literals.tar.gz &#124; tar -xz && cd 02_literals && cat TASKS.md` |
| 3 | Arithmetic Operators | `curl -L https://github.com/IITC-College/DevOps-Materials/releases/download/v1.0-python-labs/python_lab_03_operators.tar.gz &#124; tar -xz && cd 03_operators && cat TASKS.md` |
| 4 | Variables | `curl -L https://github.com/IITC-College/DevOps-Materials/releases/download/v1.0-python-labs/python_lab_04_variables.tar.gz &#124; tar -xz && cd 04_variables && cat TASKS.md` |
| 5 | Comments | `curl -L https://github.com/IITC-College/DevOps-Materials/releases/download/v1.0-python-labs/python_lab_05_comments.tar.gz &#124; tar -xz && cd 05_comments && cat TASKS.md` |
| 6 | Shortcut Assignment Operators | `curl -L https://github.com/IITC-College/DevOps-Materials/releases/download/v1.0-python-labs/python_lab_06_shortcuts.tar.gz &#124; tar -xz && cd 06_shortcuts && cat TASKS.md` |
| 7 | Type Casting | `curl -L https://github.com/IITC-College/DevOps-Materials/releases/download/v1.0-python-labs/python_lab_07_type_casting.tar.gz &#124; tar -xz && cd 07_type_casting && cat TASKS.md` |
| 8 | input() and Using What You've Learned | `curl -L https://github.com/IITC-College/DevOps-Materials/releases/download/v1.0-python-labs/python_lab_08_input.tar.gz &#124; tar -xz && cd 08_input && cat TASKS.md` |
| 9 | String Operations (concatenation, repetition, str()) | `curl -L https://github.com/IITC-College/DevOps-Materials/releases/download/v1.0-python-labs/python_lab_09_string_methods.tar.gz &#124; tar -xz && cd 09_string_methods && cat TASKS.md` |
| 10 | Comparison Operators | `curl -L https://github.com/IITC-College/DevOps-Materials/releases/download/v1.0-python-labs/python_lab_10_comparison_operators.tar.gz &#124; tar -xz && cd 10_comparison_operators && cat TASKS.md` |
| 11 | if, elif, else (Conditions) | `curl -L https://github.com/IITC-College/DevOps-Materials/releases/download/v1.0-python-labs/python_lab_11_conditions.tar.gz &#124; tar -xz && cd 11_conditions && cat TASKS.md` |
| 12 | Intermediate Conditions (Input + Variables) | `curl -L https://github.com/IITC-College/DevOps-Materials/releases/download/v1.0-python-labs/python_lab_12_conditions_intermediate.tar.gz &#124; tar -xz && cd 12_conditions_intermediate && cat TASKS.md` |
| 13 | while Loops | `curl -L https://github.com/IITC-College/DevOps-Materials/releases/download/v1.0-python-labs/python_lab_13_while_loops.tar.gz &#124; tar -xz && cd 13_while_loops && cat TASKS.md` |
| 14 | for Loops and range() | `curl -L https://github.com/IITC-College/DevOps-Materials/releases/download/v1.0-python-labs/python_lab_14_for_loops.tar.gz &#124; tar -xz && cd 14_for_loops && cat TASKS.md` |
| 15 | break and continue in for Loops | `curl -L https://github.com/IITC-College/DevOps-Materials/releases/download/v1.0-python-labs/python_lab_15_break_continue.tar.gz &#124; tar -xz && cd 15_break_continue && cat TASKS.md` |
| 16 | Logical Operators (and, or, not) | `curl -L https://github.com/IITC-College/DevOps-Materials/releases/download/v1.0-python-labs/python_lab_16_logical_operators.tar.gz &#124; tar -xz && cd 16_logical_operators && cat TASKS.md` |
| 17 | Combined Real-World (Everything So Far) | `curl -L https://github.com/IITC-College/DevOps-Materials/releases/download/v1.0-python-labs/python_lab_17_combined_real_world.tar.gz &#124; tar -xz && cd 17_combined_real_world && cat TASKS.md` |
| 18 | Lists in Python | `curl -L https://github.com/IITC-College/DevOps-Materials/releases/download/v1.0-python-labs/python_lab_18_lists.tar.gz &#124; tar -xz && cd 18_lists && cat TASKS.md` |
| 19 | List Methods (insert, append, swap, sort, reverse) | `curl -L https://github.com/IITC-College/DevOps-Materials/releases/download/v1.0-python-labs/python_lab_19_lists_methods.tar.gz &#124; tar -xz && cd 19_lists_methods && cat TASKS.md` |
| 20 | Variables vs Lists, Slicing, Real Copies | `curl -L https://github.com/IITC-College/DevOps-Materials/releases/download/v1.0-python-labs/python_lab_20_lists_variables_copies.tar.gz &#124; tar -xz && cd 20_lists_variables_copies && cat TASKS.md` |
| 21 | in and not in, Combined | `curl -L https://github.com/IITC-College/DevOps-Materials/releases/download/v1.0-python-labs/python_lab_21_in_notin_combined.tar.gz &#124; tar -xz && cd 21_in_notin_combined && cat TASKS.md` |
| 22 | 2D and 3D Lists (Nested Lists) | `curl -L https://github.com/IITC-College/DevOps-Materials/releases/download/v1.0-python-labs/python_lab_22_lists_2d_3d.tar.gz &#124; tar -xz && cd 22_lists_2d_3d && cat TASKS.md` |
| 23 | Lists Intermediate | `curl -L https://github.com/IITC-College/DevOps-Materials/releases/download/v1.0-python-labs/python_lab_23_lists_intermediate.tar.gz &#124; tar -xz && cd 23_lists_intermediate && cat TASKS.md` |
| 24 | Functions Basics | `curl -L https://github.com/IITC-College/DevOps-Materials/releases/download/v1.0-python-labs/python_lab_24_functions_basics.tar.gz &#124; tar -xz && cd 24_functions_basics && cat TASKS.md` |
| 25 | Parameters in Python | `curl -L https://github.com/IITC-College/DevOps-Materials/releases/download/v1.0-python-labs/python_lab_25_parameters.tar.gz &#124; tar -xz && cd 25_parameters && cat TASKS.md` |
| 26 | return Statement | `curl -L https://github.com/IITC-College/DevOps-Materials/releases/download/v1.0-python-labs/python_lab_26_return.tar.gz &#124; tar -xz && cd 26_return && cat TASKS.md` |
| 27 | List as Argument to a Function | `curl -L https://github.com/IITC-College/DevOps-Materials/releases/download/v1.0-python-labs/python_lab_27_list_as_argument.tar.gz &#124; tar -xz && cd 27_list_as_argument && cat TASKS.md` |
| 28 | Scopes in Python | `curl -L https://github.com/IITC-College/DevOps-Materials/releases/download/v1.0-python-labs/python_lab_28_scopes.tar.gz &#124; tar -xz && cd 28_scopes && cat TASKS.md` |

- **Version**: v1.0
- **Release**: [v1.0-python-labs](https://github.com/IITC-College/DevOps-Materials/releases/tag/v1.0-python-labs)

---

## 👨‍🎓 For Students

### How to Use This Repository

1. **Find Your Module**: Navigate to the relevant module directory
2. **Get Download Command**: Open `STUDENT_COMMAND.txt` in that module
3. **Run the Command**: Copy and paste into your terminal
4. **Start Learning**: Follow the instructions in the lab

### Example
```bash
# For Linux Module
curl -L https://github.com/IITC-College/DevOps-Jan26/releases/download/v1.0/linux_scavenger_hunt.tar.gz | tar -xz && cd linux_scavenger_hunt && cat start_here.txt
```

---

## 👨‍🏫 For Instructors

### Quick Start

To create and deploy a new lab:

```bash
./create_and_deploy_lab.sh "lab_name" "Module Name" "v1.0" "Description"
```

### Documentation

- **[LAB_WORKFLOW.md](LAB_WORKFLOW.md)** - Complete workflow guide
  - Design → Create → Test → Package → Deploy
  - Step-by-step instructions
  - Troubleshooting guide

- **[LAB_DESIGN_SPEC.md](LAB_DESIGN_SPEC.md)** - Design principles
  - Structure templates
  - Content patterns
  - Best practices
  - Quality checklist

- **[create_and_deploy_lab.sh](create_and_deploy_lab.sh)** - Automation script
  - Archive creation
  - Git operations
  - GitHub release creation
  - Full automation

### Manual Workflow

If you prefer manual control:

```bash
# 1. Create lab content (manual)
mkdir -p "Module Name/lab_name"
# ... create files ...

# 2. Package
cd "Module Name"
tar -czf lab_name.tar.gz lab_name/

# 3. Deploy
cd ..
git add "Module Name/"
git commit -m "Add lab_name"
git push

# 4. Create release
gh release create v1.0 \
  "Module Name/lab_name.tar.gz" \
  --title "Lab Name v1.0" \
  --notes "Description" \
  --repo IITC-College/DevOps-Jan26
```

---

## 🎯 Lab Design Principles

All labs follow these core principles:

1. **Progressive Learning**: Start simple, increase complexity
2. **Learning by Doing**: Exploration over lectures
3. **Real-World Simulation**: Authentic scenarios and files
4. **Hidden Information**: Scattered clues, treasure hunt style (where applicable)
5. **Self-Contained**: No external dependencies
6. **Shell Scripting (Labs 18–30)**: Instruction-based — students implement from requirements; solutions in `HINTS.md` when stuck

---

## 🛠️ Prerequisites

### For Instructors
- Git installed and configured
- GitHub CLI (`gh`) authenticated
- Bash shell
- Text editor

### For Students
- Linux environment (native, WSL, VM, or cloud)
- Terminal access
- `curl` and `tar` (usually pre-installed)

---

## 📋 Quality Standards

Every lab must meet these criteria:

- ✅ Clear entry point (`start_here.txt` or `TASKS.md` for Shell Scripting)
- ✅ Progressive difficulty (3+ levels)
- ✅ Complete solutions (`.answers/solutions.txt` or **Solutions** in `HINTS.md` for Shell Scripting)
- ✅ Tested end-to-end
- ✅ One-command download works
- ✅ Documentation complete

---

## 🔄 Version Control

### Lab Versions
- `v1.0` - Initial release
- `v1.x` - Minor updates, fixes
- `v2.0` - Major content changes

### Recent Releases
- **v1.1-shell-scripting-hardened** — Shell Scripting labs (19–30) hardened: requirements-based tasks, solutions in `HINTS.md`. [Release](https://github.com/IITC-College/DevOps-Jan26/releases/tag/v1.1-shell-scripting-hardened)

### Release Process
1. Create and test lab
2. Run automation script OR manual deployment
3. Verify download command works
4. Update module documentation

---

## 📞 Support

### For Students
- Follow instructions in each lab's README
- Check `start_here.txt` for getting started
- Solutions available after completion (ask instructor)

### For Instructors
- See [LAB_WORKFLOW.md](LAB_WORKFLOW.md) for detailed guidance
- Contact repository maintainer for access issues
- Report bugs via GitHub issues

---

## 🌟 Contributing

### Adding New Labs

1. Follow [LAB_DESIGN_SPEC.md](LAB_DESIGN_SPEC.md) for structure
2. Test thoroughly before deployment
3. Use automation script for consistency
4. Document download command

### Updating Existing Labs

1. Make changes in lab directory
2. Update version number (v1.x → v1.y)
3. Recreate archive
4. Create new release
5. Update STUDENT_COMMAND.txt

---

## 📊 Lab Statistics

| Module          | Category              | Labs | Total Files | Total Size |
|-----------------|-----------------------|------|-------------|------------|
| Linux           | Files & Navigation    | 5    | 150+        | ~50KB      |
| Linux           | Permissions           | 6    | 200+        | ~80KB      |
| Linux           | Processes & Services  | 6    | 150+        | ~70KB      |
| Linux           | Shell Scripting       | 13   | 140+        | ~50KB      |
| Linux           | Networking            | 1    | 50+         | ~20KB      |
| Linux           | Users & Groups        | 1    | 30+         | ~10KB      |
| **Total Linux** |                       | **32** | **720+**    | **~280KB** |
| Docker          | Container Basics      | 1    | 10+         | ~75KB      |
| Python          | Python Basics         | 28   | 85+         | ~25KB      |
| K8s             | -                     | -    | -           | -          |

---

## 🔗 Links

- **Repository**: https://github.com/IITC-College/DevOps-Materials
- **Releases**: https://github.com/IITC-College/DevOps-Materials/releases
- **Issues**: https://github.com/IITC-College/DevOps-Materials/issues

---

## 📜 License

Course materials © 2026 IITC College. For educational use only.

---

**Last Updated**: 2026-02-13  
**Repository**: IITC-College/DevOps-Materials  
**Maintainer**: Course Instructor
