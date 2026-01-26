# Lab Design Specification - File System Scavenger Hunt

## Purpose
This document defines the structure and design principles for creating interactive Linux CLI labs. Use this as a template for future lab development.

---

## Core Design Principles

### 1. Progressive Learning
- Start simple, gradually increase complexity
- Each level builds on previous skills
- Clear progression: Basic → Intermediate → Advanced

### 2. Learning by Doing
- All knowledge comes from exploration, not lectures
- Clues guide but don't give direct answers
- Students must use commands to discover information

### 3. Real-World Simulation
- Use realistic file structures (projects, logs, configs)
- Authentic scenarios (system logs, application files)
- Professional naming conventions

### 4. Hidden Information Pattern
- Information scattered across multiple files
- Students must combine clues from different sources
- Final challenge requires synthesizing all learned skills

---

## Lab Structure Template

```
lab_name/
├── README.md                  # Entry instructions
├── start_here.txt             # First steps (CRITICAL - clear starting point)
│
├── clues/                     # Guided challenges
│   ├── level1/               # Basic commands (nav, read)
│   │   ├── clue1.txt
│   │   ├── clue2.txt
│   │   └── clue3.txt
│   ├── level2/               # Intermediate (search, manage)
│   │   └── ...
│   └── level3/               # Advanced (combine skills)
│       └── ...
│
├── data/                      # Information sources
│   ├── logs/                 # System/app logs
│   ├── archives/             # Historical data
│   └── secrets/              # Hidden information
│
├── projects/                  # Realistic directories
│   ├── project_alpha/        # Different tech stacks
│   ├── project_beta/         # Various file types
│   └── project_gamma/        # Real configs
│
├── hidden/                    # Hidden files practice
│   └── .hidden_files
│
└── .answers/                  # Instructor solutions
    └── solutions.txt
```

---

## File Naming Conventions

### Clue Files
- Format: `clueN.txt` where N is sequential
- Each clue = one focused task
- 3 clues per level (standard)

### Data Files
- Descriptive names: `system.log`, `application.log`
- Realistic extensions: `.log`, `.txt`, `.json`, `.yaml`
- Follow industry standards

### Hidden Files
- Start with dot: `.hidden_info.txt`
- Use in projects and dedicated `hidden/` folder
- Teach real Linux behavior

---

## Content Design Patterns

### Pattern 1: Treasure Hunt
```
Clue → Location → Information → Next Clue
```
**Example**: "Find password in system.log" → grep → password found → "Now search for code"

### Pattern 2: Assembly Challenge
```
Part1 + Part2 + Part3 + Part4 = Complete Answer
```
**Example**: Master Key split across 4 files, student combines them

### Pattern 3: Discovery Learning
```
Hint → Exploration → Discovery → Understanding
```
**Example**: "Files starting with . are hidden" → ls -a → finds files → learns concept

---

## Command Coverage Framework

### Level 1: Foundation (30%)
**Focus**: Navigation and Reading
- `pwd`, `cd`, `ls`, `ls -la`
- `cat`, `less`
- Basic `grep` (single file)
- Basic `find` (by name)

### Level 2: Skills (40%)
**Focus**: Searching and Managing
- `grep -r`, `grep -rn`
- `find` with patterns
- `head`, `tail`
- `mkdir`, `mkdir -p`
- `cp`, `mv`

### Level 3: Mastery (30%)
**Focus**: Combining Everything
- Multiple commands in sequence
- Information synthesis
- Problem-solving without explicit instructions

---

## Information Distribution Model

### Scattered Information
- **DON'T**: Put all answers in one place
- **DO**: Distribute across multiple files and directories

### Layered Complexity
```
Layer 1: Direct (grep "word" file)
Layer 2: Search (grep -r "word" directory)
Layer 3: Combine (find + read + search + assemble)
```

### Answer Types
1. **Direct Text**: "The password is X"
2. **Code/Number**: "CODE: 1234"
3. **Hidden in Context**: Line in log file
4. **Assembly Required**: Parts from multiple files

---

## File Content Guidelines

### Log Files
- Realistic timestamps: `[YYYY-MM-DD HH:MM:SS]`
- Mix of INFO, WARNING, ERROR
- Hide clues in normal-looking entries
- 20-50 lines (readable but searchable)

### Configuration Files
- Use real formats: YAML, JSON, ENV
- Include comments with clues
- Professional structure
- Working syntax (even if not executed)

### Project Files
- Represent real tech stacks
- Multiple languages/frameworks
- README files with setup instructions
- Config files with actual parameters

---

## Challenge Design Formula

### Clue Structure
```
1. Context (What are we looking for?)
2. Location Hint (Where to look)
3. Method Suggestion (Which command to use)
4. Success Criteria (How to verify)
```

### Example Clue
```
TASK: Find the system password hint

LOCATION: It's in a log file in data/logs/

COMMAND: Use grep to search for "password"

VERIFY: You should find a hint with a year in it
```

---

## Difficulty Progression

### Easy (Level 1)
- Direct paths given
- Single command solves task
- Clear success indicators

### Medium (Level 2)
- Partial paths given
- 2-3 commands needed
- Some ambiguity

### Hard (Level 3)
- Minimal guidance
- Multiple steps required
- Student must plan approach

---

## Student Experience Flow

```
1. Read start_here.txt
   ↓
2. Navigate to level1/
   ↓
3. Read clue1.txt → Execute command → Find answer
   ↓
4. Read clue2.txt → Execute command → Find answer
   ↓
5. Read clue3.txt → Execute command → Find answer
   ↓
6. Progress to level2/ (repeat)
   ↓
7. Progress to level3/ (final challenge)
   ↓
8. Create my_answers.txt
```

---

## Technical Requirements

### File Format
- Plain text only (`.txt`, `.log`, `.md`)
- UTF-8 encoding
- Unix line endings (LF)
- No binary files

### Size Constraints
- Total lab: < 500KB
- Individual files: < 50KB
- Keep it lightweight and fast

### Compatibility
- Works on any Linux distribution
- No dependencies required
- Pure CLI experience

---

## Distribution Model

### Archive Format
```bash
tar -czf lab_name.tar.gz lab_name/
```

### Download Pattern
```bash
curl -L URL | tar -xz
cd lab_name
cat start_here.txt
```

### Installation Script Template
```bash
#!/bin/bash
# 1. Check prerequisites (curl, tar)
# 2. Download archive
# 3. Extract
# 4. Cleanup
# 5. Show next steps
```

---

## Instructor Materials

### Minimum Required
1. **solutions.txt** - Complete answers with locations
2. **Grading rubric** - Point distribution
3. **Expected time** - For planning

### Optional
- Setup instructions
- Common issues list
- Customization guide

---

## Quality Checklist

Before distributing a lab:

- [ ] All clues are accurate and achievable
- [ ] File paths in clues match actual structure
- [ ] All "find" targets exist
- [ ] All "grep" patterns have matches
- [ ] Hidden files are truly hidden (start with .)
- [ ] Solutions file is complete
- [ ] Tested end-to-end by creator
- [ ] Estimated completion time verified

---

## Extension Patterns

### Adding Difficulty
- More levels (level4, level5)
- Longer search paths
- More complex grep patterns
- Less explicit hints

### Adding Scope
- More file types
- Different command families
- Permissions challenges (Day 2+)
- Pipes and redirection

### Adding Context
- Story/narrative theme
- Character-based missions
- Company/project scenarios
- Time-sensitive challenges

---

## Replication Template

To create a new lab using this design:

1. **Define Learning Objectives** (Which commands?)
2. **Choose Theme** (Cybersecurity? DevOps? Data?)
3. **Create Structure** (Use template above)
4. **Write Clues** (3 per level, progressive)
5. **Create Data Files** (Logs, configs, secrets)
6. **Hide Information** (Scatter clues)
7. **Test Complete Flow** (Start to finish)
8. **Document Solutions** (Complete answers)

---

## Success Metrics

A well-designed lab should achieve:

- **80%+ completion rate** (most students finish)
- **Minimal support needed** (self-explanatory)
- **1-2 hours duration** (manageable)
- **Positive feedback** (students feel accomplished)
- **Skills transfer** (students use commands later)

---

## Summary

**Key Elements**:
- Progressive structure (3 levels)
- Scattered information (treasure hunt)
- Realistic content (professional files)
- Clear starting point (start_here.txt)
- Complete solutions (for instructor)

**Core Philosophy**:
> "Students learn by doing. Give them tools, clues, and challenges - not answers."

---

**Version**: 1.0  
**Based on**: Linux Day 1 - File System Scavenger Hunt  
**Last Updated**: 2026-01-26
