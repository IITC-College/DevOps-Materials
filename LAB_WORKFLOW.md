# Lab Development & Deployment Workflow

## Overview
This document describes the complete, automated workflow for creating and deploying Linux CLI labs to GitHub. Follow this process for all future labs.

---

## 📋 Prerequisites

### Required Tools
- Git installed and configured
- GitHub CLI (`gh`) installed and authenticated
- Bash shell access
- Text editor

### Repository Structure
```
DevOps-Jan26/                    ← Main repository
├── LAB_WORKFLOW.md              ← This file
├── LAB_DESIGN_SPEC.md           ← Design principles
├── create_and_deploy_lab.sh     ← Automation script
│
└── [Module Name]/               ← Module directory
    ├── [lab_name]/              ← Lab content
    ├── [lab_name].tar.gz        ← Distribution archive
    └── STUDENT_COMMAND.txt      ← Download instructions
```

---

## 🔄 Complete Workflow

### Phase 1: Design (Manual)

1. **Define Learning Objectives**
   - Which commands to teach?
   - What skills to develop?
   - Expected duration?

2. **Choose Theme & Context**
   - Real-world scenario
   - Student-relevant context
   - Engaging narrative (optional)

3. **Plan Information Distribution**
   - What information to hide?
   - Where to place clues?
   - How to combine multiple sources?

**Output**: Design notes (use `LAB_DESIGN_SPEC.md` as guide)

---

### Phase 2: Create Lab Structure (Automated)

Use the automation script or create manually:

```bash
# Manual structure creation
mkdir -p lab_name/{clues/{level1,level2,level3},data/{logs,archives,secrets},projects,hidden,.answers}
```

**Required Files**:
- `README.md` - Lab overview and instructions
- `start_here.txt` - Critical first entry point
- `clues/levelN/clueN.txt` - Progressive challenges
- Data files (logs, configs, secrets)
- `.answers/solutions.txt` - Complete solutions

---

### Phase 3: Create Content (Manual)

#### 3.1 Write Entry Point
**File**: `start_here.txt`
```
Welcome message
Quick overview
First command to run
Where to go next
```

#### 3.2 Write Clues (Progressive Difficulty)

**Level 1** - Basic navigation and reading
```
- Clear paths provided
- Single commands
- Direct outcomes
```

**Level 2** - Searching and managing
```
- Partial hints
- 2-3 command sequences
- Some exploration needed
```

**Level 3** - Synthesis and problem-solving
```
- Minimal guidance
- Multiple steps
- Combine all learned skills
```

#### 3.3 Create Data Files

**Log Files**:
- Realistic timestamps
- Mix INFO/WARNING/ERROR
- Hide clues in normal entries
- 20-50 lines each

**Configuration Files**:
- Use real formats (YAML, JSON, ENV)
- Include comments with hints
- Professional structure

**Project Files**:
- Represent real tech stacks
- Multiple languages
- READMEs with setup info
- Working config syntax

#### 3.4 Hide Information
- Scatter clues across files
- Use hidden files (`.filename`)
- Embed in comments
- Split answers into parts

#### 3.5 Write Solutions
**File**: `.answers/solutions.txt`
- Complete answer list
- File locations
- Commands used
- Expected outputs

---

### Phase 4: Test Lab (Critical)

```bash
# Navigate to lab directory
cd lab_name

# Follow student path exactly
cat start_here.txt
# Execute each clue step-by-step
# Verify all files exist
# Confirm all commands work
# Check all answers are findable
```

**Checklist**:
- [ ] All paths in clues are correct
- [ ] All grep patterns have matches
- [ ] All find targets exist
- [ ] Hidden files are properly hidden
- [ ] Solutions are complete and accurate
- [ ] End-to-end flow is smooth

---

### Phase 5: Package Lab (Automated)

```bash
# Create compressed archive
tar -czf lab_name.tar.gz lab_name/

# Verify archive
tar -tzf lab_name.tar.gz | head
```

**Result**: `lab_name.tar.gz` ready for distribution

---

### Phase 6: Deploy to GitHub (Automated)

#### 6.1 Verify Repository Location
```bash
# CRITICAL: Must be in main repository root
cd /path/to/DevOps-Jan26

# Verify git repository
git status
git remote -v
```

#### 6.2 Add and Commit
```bash
# Add module directory
git add "Module Name/"

# Commit with descriptive message
git commit -m "Add [Lab Name] - [Brief Description]

- Progressive difficulty (3 levels)
- [Number] files
- Commands: [list key commands]
- Duration: [estimated time]"
```

#### 6.3 Push to GitHub
```bash
git push -u origin main
```

#### 6.4 Create Release
```bash
gh release create v[X.Y] \
  "Module Name/lab_name.tar.gz" \
  --title "[Lab Name] v[X.Y]" \
  --notes "Lab description here

## Download Instructions

\`\`\`bash
curl -L https://github.com/IITC-College/DevOps-Jan26/releases/download/v[X.Y]/lab_name.tar.gz | tar -xz && cd lab_name && cat start_here.txt
\`\`\`

## What's Included
- List features
- Learning objectives
- Estimated duration" \
  --repo IITC-College/DevOps-Jan26
```

---

### Phase 7: Document Distribution

Create `STUDENT_COMMAND.txt`:
```
========================================================
              Student Download Command
========================================================

Copy and paste this command:

curl -L https://github.com/IITC-College/DevOps-Jan26/releases/download/v[X.Y]/lab_name.tar.gz | tar -xz && cd lab_name && cat start_here.txt

========================================================

Repository: https://github.com/IITC-College/DevOps-Jan26
Release: https://github.com/IITC-College/DevOps-Jan26/releases/tag/v[X.Y]

========================================================
```

---

## 🤖 Automated Workflow Script

For fully automated deployment, use:

```bash
./create_and_deploy_lab.sh "Lab Name" "Module Name" "v1.0" "Brief description"
```

This script handles:
- ✅ Archive creation
- ✅ Git add/commit/push
- ✅ GitHub release creation
- ✅ Student command generation

---

## 📝 Best Practices

### Repository Organization
```
DevOps-Jan26/
├── Linux Module/
│   ├── linux_scavenger_hunt/
│   ├── linux_scavenger_hunt.tar.gz
│   └── STUDENT_COMMAND.txt
│
├── Docker Module/
│   ├── docker_basics_lab/
│   ├── docker_basics_lab.tar.gz
│   └── STUDENT_COMMAND.txt
│
└── Kubernetes Module/
    ├── k8s_deployment_lab/
    ├── k8s_deployment_lab.tar.gz
    └── STUDENT_COMMAND.txt
```

### Version Numbering
- `v1.0` - Initial release
- `v1.1` - Minor fixes/updates
- `v2.0` - Major content changes

### Release Naming
- Format: `[Lab Name] v[X.Y] - [One-line Description]`
- Example: `Linux Lab v1.0 - File System Scavenger Hunt`

### Commit Messages
```
Add [Lab Name] - [Brief Description]

- [Number] files
- [Difficulty] levels
- Commands covered: [list]
- Estimated duration: [time]
```

---

## 🔧 Troubleshooting

### Wrong Repository Location
**Problem**: Git repository in subdirectory instead of root

**Solution**:
```bash
# Remove incorrect git repo
cd wrong_directory
rm -rf .git

# Work from correct root
cd /path/to/DevOps-Jan26
git add .
git commit -m "Your message"
git push
```

### Release Already Exists
**Problem**: Tag/release version conflict

**Solution**:
```bash
# Delete existing release
gh release delete v1.0 --yes --repo IITC-College/DevOps-Jan26

# Create new release
gh release create v1.0 [files...] --repo IITC-College/DevOps-Jan26
```

### Archive Issues
**Problem**: tar.gz doesn't extract properly

**Solution**:
```bash
# Recreate with correct options
tar -czf lab_name.tar.gz lab_name/

# Test extraction
tar -tzf lab_name.tar.gz
```

---

## 📊 Quality Gates

Before deployment, verify:

### Content Quality
- [ ] All learning objectives covered
- [ ] Progressive difficulty maintained
- [ ] Real-world relevance
- [ ] Engaging and clear

### Technical Quality
- [ ] All files present
- [ ] Correct file structure
- [ ] Archive extracts properly
- [ ] No binary files

### Testing Quality
- [ ] End-to-end tested
- [ ] All commands work
- [ ] All answers findable
- [ ] Completion time verified

### Documentation Quality
- [ ] README.md clear
- [ ] start_here.txt effective
- [ ] Solutions complete
- [ ] Download command tested

---

## 🎯 Success Criteria

A successfully deployed lab should have:

1. **Clear Entry Point**: Students know where to start
2. **Progressive Flow**: Each step builds on previous
3. **Complete Documentation**: README, solutions, commands
4. **Working Distribution**: One-command download works
5. **GitHub Integration**: Release created, file attached
6. **Student Instructions**: Clear command provided

---

## 📚 Reference Documents

- **Design Principles**: See `LAB_DESIGN_SPEC.md`
- **Automation Script**: See `create_and_deploy_lab.sh`
- **Example Lab**: See `Linux Module/linux_scavenger_hunt/`

---

## 🔄 Quick Reference

### Complete Workflow (One-liner)
```bash
# Design → Create → Test → Package → Deploy
./create_and_deploy_lab.sh "Lab Name" "Module Name" "v1.0" "Description"
```

### Manual Workflow Steps
```bash
# 1. Create structure
mkdir -p lab_name/{clues,data,projects,hidden,.answers}

# 2. Create content (manual)

# 3. Test (manual)

# 4. Package
tar -czf lab_name.tar.gz lab_name/

# 5. Deploy
cd /path/to/repo-root
git add "Module Name/"
git commit -m "Add lab"
git push
gh release create vX.Y "Module Name/lab_name.tar.gz" --title "..." --notes "..."
```

---

**Version**: 1.0  
**Created**: 2026-01-26  
**Repository**: https://github.com/IITC-College/DevOps-Jan26
