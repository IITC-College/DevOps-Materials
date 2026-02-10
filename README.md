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

Labs are numbered in the order they should be completed, following the course structure:

- **Lab 1**: Navigation Basics
  - **Version**: v2.0
  - **Lab ID**: `linux_lab1_navigation_basics`
  - **Focus**: Basic navigation (cd, ls, error messages, hidden files)
  - **Duration**: 60-90 minutes
  - **Download**: See `Linux Module/STUDENT_COMMAND.txt`

- **Lab 2**: File and Directory Management
  - **Version**: v2.1
  - **Lab ID**: `linux_lab2_file_management`
  - **Focus**: File and directory management (mkdir, touch, cp, mv, rm, rmdir)
  - **Duration**: 75-90 minutes
  - **Download**: See `Linux Module/STUDENT_COMMAND.txt`

- **Lab 3**: Reading Files
  - **Version**: v2.2
  - **Lab ID**: `linux_lab3_reading_files`
  - **Focus**: Reading files (cat, less, head, tail)
  - **Duration**: 60-75 minutes
  - **Download**: See `Linux Module/STUDENT_COMMAND.txt`

- **Lab 4**: Search Basics
  - **Version**: v2.3
  - **Lab ID**: `linux_lab4_search_basics`
  - **Focus**: Searching with grep and find
  - **Duration**: 60-75 minutes
  - **Download**: See `Linux Module/STUDENT_COMMAND.txt`

- **Lab 5**: File System Scavenger Hunt
  - **Version**: v2.4
  - **Lab ID**: `linux_lab5_scavenger_hunt`
  - **Focus**: Comprehensive CLI practice - Final lab combining all skills
  - **Duration**: 1-2 hours
  - **Download**: See `Linux Module/STUDENT_COMMAND.txt`

- **Lab 6**: Permission Encounter
  - **Version**: v2.5
  - **Lab ID**: `linux_lab6_permission_encounter`
  - **Focus**: Introduction to Linux permissions - Reading and understanding permissions
  - **Duration**: 60-75 minutes
  - **Download**: See `Linux Module/STUDENT_COMMAND.txt`

- **Lab 7**: Why Script Doesn't Run
  - **Version**: v2.6
  - **Lab ID**: `linux_lab7_why_script_doesnt_run`
  - **Focus**: Understanding chmod and execute permissions - Fixing scripts that won't run
  - **Duration**: 60-75 minutes
  - **Download**: See `Linux Module/STUDENT_COMMAND.txt`

- **Lab 8**: Ownership and Groups
  - **Version**: v2.7
  - **Lab ID**: `linux_lab8_ownership_and_groups`
  - **Focus**: Understanding ownership and groups - chown and group permissions
  - **Duration**: 60-75 minutes
  - **Download**: See `Linux Module/STUDENT_COMMAND.txt`

- **Lab 9**: Understanding sudo - When and Why
  - **Version**: v2.8
  - **Lab ID**: `linux_lab9_sudo_mindset`
  - **Focus**: Understanding sudo - When to use it, when not to, and understanding audit logging
  - **Duration**: 60-75 minutes
  - **Download**: See `Linux Module/STUDENT_COMMAND.txt`

- **Lab 10**: Processes Basics
  - **Version**: v1.0
  - **Lab ID**: `linux_lab_processes_basics`
  - **Focus**: Understanding what a process is, using ps, top, htop, and identifying process resources
  - **Duration**: 40-45 minutes
  - **Download**:
    ```bash
    curl -L https://github.com/IITC-College/DevOps-Jan26/releases/download/v1.0/linux_lab_processes_basics.tar.gz | tar -xz && cd linux_lab_processes_basics && cd clues/level1 && cat clue1.txt
    ```

- **Lab 11**: Process Management (kill)
  - **Version**: v1.0
  - **Lab ID**: `linux_lab_processes_kill`
  - **Focus**: Understanding the kill command, SIGTERM vs SIGKILL, and controlled process termination
  - **Duration**: 20-25 minutes
  - **Download**:
    ```bash
    curl -L https://github.com/IITC-College/DevOps-Jan26/releases/download/v1.0/linux_lab_processes_kill.tar.gz | tar -xz && cd linux_lab_processes_kill && cd clues/level1 && cat clue1.txt
    ```

- **Lab 12**: Process vs Service
  - **Version**: v1.0
  - **Lab ID**: `linux_lab_processes_vs_service`
  - **Focus**: Understanding the difference between processes and services, systemd concepts
  - **Duration**: 20-25 minutes
  - **Download**:
    ```bash
    curl -L https://github.com/IITC-College/DevOps-Jan26/releases/download/v1.0/linux_lab_processes_vs_service.tar.gz | tar -xz && cd linux_lab_processes_vs_service && cd clues/level1 && cat clue1.txt
    ```

- **Lab 13**: systemd and Services
  - **Version**: v1.0
  - **Lab ID**: `linux_lab_systemd_services`
  - **Focus**: Managing services with systemctl (status, start, stop, restart)
  - **Duration**: 45-50 minutes
  - **Download**:
    ```bash
    curl -L https://github.com/IITC-College/DevOps-Jan26/releases/download/v1.0/linux_lab_systemd_services.tar.gz | tar -xz && cd linux_lab_systemd_services && cd clues/level1 && cat clue1.txt
    ```

- **Lab 14**: Logs-First: journalctl
  - **Version**: v1.0
  - **Lab ID**: `linux_lab_journalctl_logs_first`
  - **Focus**: Using journalctl to view and filter system logs, finding errors, and describing problems professionally
  - **Duration**: 45-50 minutes
  - **Download**:
    ```bash
    curl -L https://github.com/IITC-College/DevOps-Jan26/releases/download/v1.0/linux_lab_journalctl_logs_first.tar.gz | tar -xz && cd linux_lab_journalctl_logs_first && cd clues/level1 && cat clue1.txt
    ```

- **Lab 15**: Troubleshooting Flow
  - **Version**: v1.0
  - **Lab ID**: `linux_lab_troubleshooting_flow`
  - **Focus**: Applying a 5-step troubleshooting methodology to diagnose broken services and processes
  - **Duration**: 30-35 minutes
  - **Download**:
    ```bash
    curl -L https://github.com/IITC-College/DevOps-Jan26/releases/download/v1.0/linux_lab_troubleshooting_flow.tar.gz | tar -xz && cd linux_lab_troubleshooting_flow && cd clues/level1 && cat clue1.txt
    ```

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
4. **Hidden Information**: Scattered clues, treasure hunt style
5. **Self-Contained**: No external dependencies

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

- ✅ Clear entry point (`start_here.txt`)
- ✅ Progressive difficulty (3+ levels)
- ✅ Complete solutions (`.answers/solutions.txt`)
- ✅ Tested end-to-end
- ✅ One-command download works
- ✅ Documentation complete

---

## 🔄 Version Control

### Lab Versions
- `v1.0` - Initial release
- `v1.x` - Minor updates, fixes
- `v2.0` - Major content changes

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

| Module | Labs | Total Files | Total Size |
|--------|------|-------------|------------|
| Linux  | 15   | 400+        | ~200KB     |
| Docker | -    | -           | -          |
| K8s    | -    | -           | -          |

---

## 🔗 Links

- **Repository**: https://github.com/IITC-College/DevOps-Jan26
- **Releases**: https://github.com/IITC-College/DevOps-Jan26/releases
- **Issues**: https://github.com/IITC-College/DevOps-Jan26/issues

---

## 📜 License

Course materials © 2026 IITC College. For educational use only.

---

**Last Updated**: 2026-01-26  
**Repository**: IITC-College/DevOps-Jan26  
**Maintainer**: Course Instructor
