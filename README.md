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
- **Lab 1**: Navigation Basics
  - **Version**: v1.1
  - **Focus**: Basic navigation (cd, ls, error messages, hidden files)
  - **Duration**: 60-90 minutes
  - **Download**: See `Linux Module/STUDENT_COMMAND.txt`
- **Lab 2**: File and Directory Management
  - **Version**: v1.2
  - **Focus**: File and directory management (mkdir, touch, cp, mv, rm, rmdir)
  - **Duration**: 75-90 minutes
  - **Download**: See `Linux Module/STUDENT_COMMAND.txt`
- **Lab 3**: Reading Files
  - **Version**: v1.3
  - **Focus**: Reading files (cat, less, head, tail)
  - **Duration**: 60-75 minutes
  - **Download**: See `Linux Module/STUDENT_COMMAND.txt`
- **Lab 4**: Search Basics
  - **Version**: v1.4
  - **Focus**: Searching with grep and find
  - **Duration**: 60-75 minutes
  - **Download**: See `Linux Module/STUDENT_COMMAND.txt`
- **Lab 5**: File System Scavenger Hunt
  - **Version**: v1.0
  - **Focus**: Comprehensive CLI practice - Final lab combining all skills
  - **Duration**: 1-2 hours
  - **Download**: See `Linux Module/STUDENT_COMMAND.txt`

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
| Linux  | 5    | 109         | ~60KB      |
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
