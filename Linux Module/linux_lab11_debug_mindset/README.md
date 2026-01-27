# Linux Lab - Debug Mindset: 4-Step Debug Flow

Welcome to your Linux debugging methodology lab!

## Installation Instructions

### Method 1: Download with curl (Recommended)

```bash
curl -L -o lab.tar.gz https://github.com/IITC-College/DevOps-Jan26/releases/download/v2.8/linux_lab11_debug_mindset.tar.gz
tar -xzf lab.tar.gz
cd linux_lab11_debug_mindset
```

## Instructor Setup (Required Before Lab)

**IMPORTANT**: Before students start the lab, instructors must run the environment setup script:

```bash
sudo ./setup_environment.sh
```

This script will:
- Set up deliberately broken scenarios for students to debug:
  - Scenario 1: Read permission removed
  - Scenario 2: Execute permission missing
  - Scenario 3: Write permission removed from directory
  - Scenario 4: File owned by root (ownership mismatch) - **requires root ownership**
  - Scenario 5: Hidden file with no access
  - Scenario 6: Multiple combined issues
- Set root ownership for `scenario4_ownership_mess/important.txt` (critical for ownership exercise)
- Ensure the lab environment is properly configured

**Note**: The broken scenarios are intentional - students will use the 4-step debug methodology to fix them.

## Lab Objective

In this lab you will learn a **systematic debugging methodology** that applies to ANY Linux problem:

- **4-Step Debug Process**: OBSERVE → INSPECT → DIAGNOSE → RESOLVE
- **Evidence-Based Debugging**: Make decisions based on inspection, not guessing
- **Root Cause Analysis**: Fix the real problem, not just symptoms
- **Methodology Transfer**: Apply this process to any future Linux problem

## Important: What This Lab IS

- ✅ **IS** about learning a systematic debugging methodology
- ✅ **IS** about breaking the trial-and-error habit
- ✅ **IS** about evidence-based problem solving
- ✅ **IS** about fixing root causes, not workarounds
- ✅ **IS** about developing critical thinking skills
- ✅ **IS** about methodology that transfers to all future problems

## Important: What This Lab Is NOT

- ❌ **NOT** about trying random commands until something works
- ❌ **NOT** about memorizing specific commands
- ❌ **NOT** about quick fixes or workarounds
- ❌ **NOT** about guessing what might work
- ✅ **IS** about systematic, methodical problem solving

## How to Start?

1. Open the `start_here.txt` file - this is where to begin!
2. Read the 4-step methodology in `data/logs/debug_methodology.txt`
3. Follow the exercises step by step
4. Apply the 4-step process to EVERY problem

```bash
cat start_here.txt
```

## The 4-Step Debug Methodology

### STEP 1: OBSERVE
- What exactly is the error message?
- What were you trying to do?
- What symptoms do you see?

### STEP 2: INSPECT
- Check current state: `pwd`, `ls -l`, `ls -la`
- Look at permissions: who owns it? what permissions exist?
- Check paths: are you in the right place?

### STEP 3: DIAGNOSE
- Based on evidence from INSPECT, what's the root cause?
- Is it permissions? ownership? wrong path? hidden file?
- Don't guess - use evidence!

### STEP 4: RESOLVE
- Apply the correct fix (not a workaround)
- Use the right command for the root cause
- Verify it worked with INSPECT again

## Exercise List

### Level 1: Single-Issue Debugging
- Exercise 1: Permission denied on file read
- Exercise 2: Script won't execute
- Exercise 3: Can't create file in directory

### Level 2: Ownership and Path Issues
- Exercise 1: Ownership mismatch
- Exercise 2: Lost in wrong directory
- Exercise 3: Hidden file access issues

### Level 3: Complex Mixed Scenarios
- Exercise 1: Chain of issues (multiple problems in sequence)
- Exercise 2: Nested directory permission problem
- Exercise 3: Complete debug challenge (fix everything)

## Commands Organized by Debug Step

### OBSERVE (Step 1)
- Read error messages in terminal
- Note what command failed
- Identify symptom

### INSPECT (Step 2)
- `pwd` - where am I?
- `ls -l` - file permissions and ownership
- `ls -la` - including hidden files
- `ls -ld` - directory itself permissions
- `file <name>` - file type verification
- `whoami` - current username
- `id` - user ID and groups

### DIAGNOSE (Step 3)
- Analyze evidence from INSPECT
- Identify root cause
- Plan fix approach

### RESOLVE (Step 4)
- `chmod <permissions> <file>` - fix permissions
- `sudo chown <user>:<group> <file>` - fix ownership (when appropriate)
- `cd <directory>` - navigate to correct location
- Correct command with proper path

## Important Tips

1. **Follow the 4 steps** - Don't skip any step
2. **OBSERVE first** - Read error messages carefully
3. **INSPECT second** - Gather evidence before making changes
4. **DIAGNOSE third** - Identify root cause based on evidence
5. **RESOLVE last** - Apply correct fix, verify it worked
6. **No trial-and-error** - Use the methodology systematically
7. **Fix root causes** - Not just symptoms or workarounds
8. **Verify your fixes** - Check with INSPECT again after RESOLVE

## Safety Rules

- **Follow the methodology** - Use the 4-step process for every problem
- **Gather evidence first** - Use INSPECT commands before making changes
- **Work in the lab directory** - All exercises are safe here
- **Understand what you're doing** - Don't blindly run commands
- **Fix root causes** - Not just workarounds
- **Verify your fixes** - Check that your fix actually worked

## Lab Submission

After completing all exercises:

1. Create a file called `my_answers.txt` in the lab directory
2. For each exercise, document:
   - What you OBSERVED (error message)
   - What you INSPECTED (commands and output)
   - What you DIAGNOSED (root cause)
   - How you RESOLVED (fix command)
3. Include your reflections on the debugging methodology
4. Answer: How will you apply this methodology to future problems?
5. Save the file

## Help

If you get stuck:

1. Re-read the methodology in `data/logs/debug_methodology.txt`
2. Make sure you followed all 4 steps
3. Check `data/secrets/tips.txt` for hints
4. Verify you're in the right directory with `pwd`
5. Use `ls -la` to see all files including hidden ones
6. Read error messages carefully - they contain clues
7. Remember: No trial-and-error - follow the steps!

## Good Luck!

Remember: This lab is about learning a methodology, not just solving problems. The 4-step process (OBSERVE → INSPECT → DIAGNOSE → RESOLVE) will help you solve ANY Linux problem systematically. Take your time, follow the steps, and develop good debugging habits!

---

**Linux Course - Day 2, Part 6**  
**Debug Mindset: 4-Step Debug Flow Lab**  
**Version**: v2.8