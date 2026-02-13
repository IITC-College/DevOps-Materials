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

- **Lab 1**: Navigation Basics
  - **Version**: v2.0
  - **Lab ID**: `linux_lab1_navigation_basics`
  - **Focus**: Basic navigation (cd, ls, error messages, hidden files)
  - **Duration**: 60-90 minutes
  - **Download**:
    ```bash
    curl -L https://github.com/IITC-College/DevOps-Jan26/releases/download/v2.0/linux_lab1_navigation_basics.tar.gz | tar -xz && cd linux_lab1_navigation_basics && cat start_here.txt
    ```

- **Lab 2**: File and Directory Management
  - **Version**: v2.1
  - **Lab ID**: `linux_lab2_file_management`
  - **Focus**: File and directory management (mkdir, touch, cp, mv, rm, rmdir)
  - **Duration**: 75-90 minutes
  - **Download**:
    ```bash
    curl -L https://github.com/IITC-College/DevOps-Jan26/releases/download/v2.1/linux_lab2_file_management.tar.gz | tar -xz && cd linux_lab2_file_management && cat start_here.txt
    ```

- **Lab 3**: Reading Files
  - **Version**: v2.2
  - **Lab ID**: `linux_lab3_reading_files`
  - **Focus**: Reading files (cat, less, head, tail)
  - **Duration**: 60-75 minutes
  - **Download**:
    ```bash
    curl -L https://github.com/IITC-College/DevOps-Jan26/releases/download/v2.2/linux_lab3_reading_files.tar.gz | tar -xz && cd linux_lab3_reading_files && cat start_here.txt
    ```

- **Lab 4**: Search Basics
  - **Version**: v2.3
  - **Lab ID**: `linux_lab4_search_basics`
  - **Focus**: Searching with grep and find
  - **Duration**: 60-75 minutes
  - **Download**:
    ```bash
    curl -L https://github.com/IITC-College/DevOps-Jan26/releases/download/v2.3/linux_lab4_search_basics.tar.gz | tar -xz && cd linux_lab4_search_basics && cat start_here.txt
    ```

- **Lab 5**: File System Scavenger Hunt
  - **Version**: v2.4
  - **Lab ID**: `linux_lab5_scavenger_hunt`
  - **Focus**: Comprehensive CLI practice - Final lab combining all skills
  - **Duration**: 1-2 hours
  - **Download**:
    ```bash
    curl -L https://github.com/IITC-College/DevOps-Jan26/releases/download/v2.4/linux_lab5_scavenger_hunt.tar.gz | tar -xz && cd linux_lab5_scavenger_hunt && cat start_here.txt
    ```

#### Permissions

- **Lab 6**: Permission Encounter
  - **Version**: v2.5
  - **Lab ID**: `linux_lab6_permission_encounter`
  - **Focus**: Introduction to Linux permissions - Reading and understanding permissions
  - **Duration**: 60-75 minutes
  - **Download**:
    ```bash
    curl -L https://github.com/IITC-College/DevOps-Jan26/releases/download/v2.5/linux_lab6_permission_encounter.tar.gz | tar -xz && cd linux_lab6_permission_encounter && cd clues/level1 && cat clue1.txt
    ```

- **Lab 7**: Why Script Doesn't Run
  - **Version**: v2.6
  - **Lab ID**: `linux_lab7_why_script_doesnt_run`
  - **Focus**: Understanding chmod and execute permissions - Fixing scripts that won't run
  - **Duration**: 60-75 minutes
  - **Download**:
    ```bash
    curl -L https://github.com/IITC-College/DevOps-Jan26/releases/download/v2.6/linux_lab7_why_script_doesnt_run.tar.gz | tar -xz && cd linux_lab7_why_script_doesnt_run && cd clues/level1 && cat clue1.txt
    ```

- **Lab 8**: Ownership and Groups
  - **Version**: v2.7
  - **Lab ID**: `linux_lab8_ownership_and_groups`
  - **Focus**: Understanding ownership and groups - chown and group permissions
  - **Duration**: 60-75 minutes
  - **Download**:
    ```bash
    curl -L https://github.com/IITC-College/DevOps-Jan26/releases/download/v2.7/linux_lab8_ownership_and_groups.tar.gz | tar -xz && cd linux_lab8_ownership_and_groups && cd clues/level1 && cat clue1.txt
    ```

- **Lab 9**: Understanding sudo
  - **Version**: v2.8
  - **Lab ID**: `linux_lab9_sudo_mindset`
  - **Focus**: Understanding sudo - When to use it, when not to, and understanding audit logging
  - **Duration**: 60-75 minutes
  - **Download**:
    ```bash
    curl -L https://github.com/IITC-College/DevOps-Jan26/releases/download/v2.8/linux_lab9_sudo_mindset.tar.gz | tar -xz && cd linux_lab9_sudo_mindset && cd clues/level1 && cat clue1.txt
    ```

- **Lab 10**: Default Permissions (umask)
  - **Version**: v2.10
  - **Lab ID**: `linux_lab10_default_permissions`
  - **Focus**: Understanding umask and default permissions
  - **Duration**: 60-75 minutes
  - **Download**:
    ```bash
    curl -L https://github.com/IITC-College/DevOps-Jan26/releases/download/v2.10/linux_lab10_default_permissions.tar.gz | tar -xz && cd linux_lab10_default_permissions && cd clues/level1 && cat clue1.txt
    ```

- **Lab 11**: Debug Mindset
  - **Version**: v4.1
  - **Lab ID**: `linux_lab11_debug_mindset`
  - **Focus**: Systematic debugging approach for permission issues
  - **Duration**: 60-75 minutes
  - **Download**:
    ```bash
    curl -L https://github.com/IITC-College/DevOps-Jan26/releases/download/v4.1/linux_lab11_debug_mindset.tar.gz | tar -xz && cd linux_lab11_debug_mindset && cd clues/level1 && cat clue1.txt
    ```

#### Processes and Services

- **Lab 12**: Processes Basics
  - **Version**: v1.1
  - **Lab ID**: `linux_lab_processes_basics`
  - **Focus**: Understanding what a process is, using ps, top, htop
  - **Duration**: 40-45 minutes
  - **Download**:
    ```bash
    curl -L https://github.com/IITC-College/DevOps-Jan26/releases/download/v1.1-processes-basics/linux_lab_processes_basics.tar.gz | tar -xz && cd linux_lab_processes_basics && cd clues/level1 && cat clue1.txt
    ```

- **Lab 13**: Process Management (kill)
  - **Version**: v1.0
  - **Lab ID**: `linux_lab_processes_kill`
  - **Focus**: Understanding kill, SIGTERM vs SIGKILL
  - **Duration**: 20-25 minutes
  - **Download**:
    ```bash
    curl -L https://github.com/IITC-College/DevOps-Jan26/releases/download/v1.0/linux_lab_processes_kill.tar.gz | tar -xz && cd linux_lab_processes_kill && cd clues/level1 && cat clue1.txt
    ```

- **Lab 14**: Process vs Service
  - **Version**: v1.0
  - **Lab ID**: `linux_lab_processes_vs_service`
  - **Focus**: Understanding the difference between processes and services
  - **Duration**: 20-25 minutes
  - **Download**:
    ```bash
    curl -L https://github.com/IITC-College/DevOps-Jan26/releases/download/v1.0/linux_lab_processes_vs_service.tar.gz | tar -xz && cd linux_lab_processes_vs_service && cd clues/level1 && cat clue1.txt
    ```

- **Lab 15**: systemd and Services
  - **Version**: v1.0
  - **Lab ID**: `linux_lab_systemd_services`
  - **Focus**: Managing services with systemctl (status, start, stop, restart)
  - **Duration**: 45-50 minutes
  - **Download**:
    ```bash
    curl -L https://github.com/IITC-College/DevOps-Jan26/releases/download/v1.0/linux_lab_systemd_services.tar.gz | tar -xz && cd linux_lab_systemd_services && cd clues/level1 && cat clue1.txt
    ```

- **Lab 16**: Logs-First (journalctl)
  - **Version**: v1.1
  - **Lab ID**: `linux_lab_journalctl_logs_first`
  - **Focus**: Using journalctl to view and filter system logs
  - **Duration**: 45-50 minutes
  - **Download**:
    ```bash
    curl -L https://github.com/IITC-College/DevOps-Jan26/releases/download/v1.1-journalctl-logs/linux_lab_journalctl_logs_first.tar.gz | tar -xz && cd linux_lab_journalctl_logs_first && cd clues/level1 && cat clue1.txt
    ```

- **Lab 17**: Troubleshooting Flow
  - **Version**: v1.0
  - **Lab ID**: `linux_lab_troubleshooting_flow`
  - **Focus**: Applying a 5-step troubleshooting methodology
  - **Duration**: 30-35 minutes
  - **Download**:
    ```bash
    curl -L https://github.com/IITC-College/DevOps-Jan26/releases/download/v1.0/linux_lab_troubleshooting_flow.tar.gz | tar -xz && cd linux_lab_troubleshooting_flow && cd clues/level1 && cat clue1.txt
    ```

#### Shell Scripting

Hands-on coding exercises for mastering bash scripting. Each lab is a self-contained exercise with tasks, hints, and starter files.

**Hardened format (v1.1)** — [Release notes](https://github.com/IITC-College/DevOps-Jan26/releases/tag/v1.1-shell-scripting-hardened): Labs are instruction-based so students **write code** instead of copying.

| Item | Description |
|------|-------------|
| `TASKS.md` | Requirements, objectives, expected output, and testing steps (no full code to copy) |
| `HINTS.md` | Syntax tips and a **Solutions** section at the end (use when stuck) |
| `src/` | Starter files and data (configs, logs, broken scripts for debugging lab) |

- **Lab 18 (Basics)** keeps full examples for first-time learners.
- **Labs 19–30** use progressive difficulty: more guidance in early tasks, less in later tasks.

- **Lab 18**: Script Basics
  - **Version**: v1.0
  - **Lab ID**: `linux_lab_script_basics`
  - **Focus**: Creating scripts, shebangs, permissions, chmod, execution methods
  - **Duration**: 20-30 minutes
  - **Download**:
    ```bash
    curl -L https://github.com/IITC-College/DevOps-Jan26/releases/download/v1.1-script-basics/linux_lab_script_basics.tar.gz | tar -xz && cd linux_lab_script_basics && cat TASKS.md
    ```

- **Lab 19**: Variables
  - **Version**: v1.1
  - **Lab ID**: `linux_lab_script_variables`
  - **Focus**: Variables, command substitution, timestamps, dynamic values
  - **Duration**: 25-35 minutes
  - **Download**:
    ```bash
    curl -L https://github.com/IITC-College/DevOps-Jan26/releases/download/v1.1-script-variables/linux_lab_script_variables.tar.gz | tar -xz && cd linux_lab_script_variables && cat TASKS.md
    ```

- **Lab 20**: User Input
  - **Version**: v1.1
  - **Lab ID**: `linux_lab_script_input`
  - **Focus**: Reading input with read, validation importance, empty input handling
  - **Duration**: 20-30 minutes
  - **Download**:
    ```bash
    curl -L https://github.com/IITC-College/DevOps-Jan26/releases/download/v1.1-script-input/linux_lab_script_input.tar.gz | tar -xz && cd linux_lab_script_input && cat TASKS.md
    ```

- **Lab 21**: Conditionals
  - **Version**: v1.1
  - **Lab ID**: `linux_lab_script_conditionals`
  - **Focus**: File/directory checks, input validation, if/elif/else, building validators
  - **Duration**: 25-35 minutes
  - **Download**:
    ```bash
    curl -L https://github.com/IITC-College/DevOps-Jan26/releases/download/v1.1-script-conditionals/linux_lab_script_conditionals.tar.gz | tar -xz && cd linux_lab_script_conditionals && cat TASKS.md
    ```

- **Lab 22**: Case Statements
  - **Version**: v1.1
  - **Lab ID**: `linux_lab_script_case`
  - **Focus**: Case syntax, menu systems, pattern matching, default branches (no functions)
  - **Duration**: 20-30 minutes
  - **Download**:
    ```bash
    curl -L https://github.com/IITC-College/DevOps-Jan26/releases/download/v1.1-script-case/linux_lab_script_case.tar.gz | tar -xz && cd linux_lab_script_case && cat TASKS.md
    ```

- **Lab 23**: Loops
  - **Version**: v1.1
  - **Lab ID**: `linux_lab_script_loops`
  - **Focus**: For loops, while loops, retry patterns, nested loops
  - **Duration**: 25-35 minutes
  - **Download**:
    ```bash
    curl -L https://github.com/IITC-College/DevOps-Jan26/releases/download/v1.1-script-loops/linux_lab_script_loops.tar.gz | tar -xz && cd linux_lab_script_loops && cat TASKS.md
    ```

- **Lab 24**: Functions
  - **Version**: v1.1
  - **Lab ID**: `linux_lab_script_functions`
  - **Focus**: Defining functions, parameters, loops, case+functions menu, reusability
  - **Duration**: 30-40 minutes
  - **Download**:
    ```bash
    curl -L https://github.com/IITC-College/DevOps-Jan26/releases/download/v1.1-script-functions/linux_lab_script_functions.tar.gz | tar -xz && cd linux_lab_script_functions && cat TASKS.md
    ```

- **Lab 25**: Exit Codes
  - **Version**: v1.1
  - **Lab ID**: `linux_lab_script_exit_codes`
  - **Focus**: Exit codes, $?, chaining with && and ||, fail-fast patterns, CI/CD integration
  - **Duration**: 25-35 minutes
  - **Download**:
    ```bash
    curl -L https://github.com/IITC-College/DevOps-Jan26/releases/download/v1.1-script-exit-codes/linux_lab_script_exit_codes.tar.gz | tar -xz && cd linux_lab_script_exit_codes && cat TASKS.md
    ```

- **Lab 26**: Debugging
  - **Version**: v1.1
  - **Lab ID**: `linux_lab_script_debugging`
  - **Focus**: Finding and fixing common bash errors, syntax debugging, error messages
  - **Duration**: 25-35 minutes
  - **Download**:
    ```bash
    curl -L https://github.com/IITC-College/DevOps-Jan26/releases/download/v1.1-script-debugging/linux_lab_script_debugging.tar.gz | tar -xz && cd linux_lab_script_debugging && cat TASKS.md
    ```

- **Lab 27**: Ops Helper Tool
  - **Version**: v1.1
  - **Lab ID**: `linux_lab_script_ops_helper`
  - **Focus**: Building a practical ops tool combining all concepts
  - **Duration**: 25-35 minutes
  - **Download**:
    ```bash
    curl -L https://github.com/IITC-College/DevOps-Jan26/releases/download/v1.1-script-ops-helper/linux_lab_script_ops_helper.tar.gz | tar -xz && cd linux_lab_script_ops_helper && cat TASKS.md
    ```

- **Lab 28**: Mini DevOps Tool (Capstone)
  - **Version**: v1.1
  - **Lab ID**: `linux_lab_script_mini_devops_tool`
  - **Focus**: Comprehensive capstone project - menu-driven tool with health checks, status, backups, and CI/CD pipeline
  - **Duration**: 35-45 minutes
  - **Download**:
    ```bash
    curl -L https://github.com/IITC-College/DevOps-Jan26/releases/download/v1.1-script-mini-devops-tool/linux_lab_script_mini_devops_tool.tar.gz | tar -xz && cd linux_lab_script_mini_devops_tool && cat TASKS.md
    ```

- **Lab 29**: Leap Year
  - **Version**: v1.1
  - **Lab ID**: `linux_lab_script_leap_year`
  - **Focus**: Arithmetic, conditionals, user input – build a leap-year checker (divisible by 4, 100, 400)
  - **Duration**: 20-30 minutes
  - **Download**:
    ```bash
    curl -L https://github.com/IITC-College/DevOps-Jan26/releases/download/v1.1-script-leap-year/linux_lab_script_leap_year.tar.gz | tar -xz && cd linux_lab_script_leap_year && cat TASKS.md
    ```

- **Lab 30**: Number Guessing Game
  - **Version**: v1.1
  - **Lab ID**: `linux_lab_script_guessing_game`
  - **Focus**: Random numbers, read, conditionals, while loop – guess until correct, count attempts
  - **Duration**: 25-35 minutes
  - **Download**:
    ```bash
    curl -L https://github.com/IITC-College/DevOps-Jan26/releases/download/v1.1-script-guessing-game/linux_lab_script_guessing_game.tar.gz | tar -xz && cd linux_lab_script_guessing_game && cat TASKS.md
    ```

#### Networking

- **Lab 31**: Network Adapter Debug
  - **Version**: v4.0
  - **Lab ID**: `linux_networking_lab1_adapter`
  - **Focus**: Diagnosing and fixing real-world networking issues (interfaces, IP, gateway, DNS, firewall, MTU, routing)
  - **Duration**: 90-120 minutes
  - **Download**:
    ```bash
    curl -L https://github.com/IITC-College/DevOps-Jan26/releases/download/v4.0/linux_networking_lab1_adapter.tar.gz | tar -xz && cd linux_networking_lab1_adapter && cat README.md
    ```

#### Users and Groups

- **Lab 32**: Users and Groups Management
  - **Version**: In Development
  - **Lab ID**: `linux_users_groups_management`
  - **Focus**: Creating users, managing groups, understanding user permissions
  - **Duration**: 60-90 minutes
  - **Path**: `Linux/Users and Groups/linux_users_groups_management/`
  - **Note**: Requires instructor setup - see lab README

---

### Docker Module

#### Container Basics

- **Lab 1**: Docker Container Basics
  - **Version**: v1.0
  - **Lab ID**: `docker_lab_basics`
  - **Focus**: Run containers (hello-world, nginx, PostgreSQL), manage lifecycle, view logs, exec into containers
  - **Duration**: 30-40 minutes
  - **Download**:
    ```bash
    curl -L https://github.com/IITC-College/DevOps-Materials/releases/download/v1.0/docker_lab_basics.tar.gz | tar -xz && cd docker_lab_basics && cat README.md
    ```
  - **Start**: Open `TASKS.md` to begin the lab

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
