# Linux Lab - Why Script Doesn't Run

Welcome to your Linux chmod practice lab!

## Installation Instructions

### Method 1: Download with curl (Recommended)

```bash
curl -L -o lab.tar.gz https://github.com/IITC-College/DevOps-Jan26/releases/download/v2.6/linux_lab7_why_script_doesnt_run.tar.gz
tar -xzf lab.tar.gz
cd linux_lab7_why_script_doesnt_run
```

## Instructor Setup (Required Before Lab)

**IMPORTANT**: Before students start the lab, instructors must run the environment setup script:

```bash
sudo ./setup_environment.sh
```

This script will:
- Remove execute permissions from broken scripts (as intended for the lab)
- Set up file permissions for all exercises
- Ensure the lab environment is properly configured

**Note**: This lab does not require special users or groups - it works with any user.

## Lab Objective

In this lab you will learn to fix scripts that won't run by understanding and modifying file permissions:

- **Understanding Execute Permission**: Learning why scripts need the `x` (execute) permission
- **Using chmod**: Fixing permissions with `chmod` command
- **Targeted Changes**: Adding execute permissions to specific users (owner, group, others)
- **Real-World Scenarios**: Fixing broken scripts in actual project environments

## Important: What This Lab IS

- ✅ **IS** about fixing permissions with `chmod`
- ✅ **IS** about understanding why scripts don't run
- ✅ **IS** about adding execute permissions correctly
- ✅ **IS** about reading permissions before changing them

## How to Start?

1. Open the `start_here.txt` file - this is where to begin!
2. Read the instructions carefully
3. Follow the exercises step by step

```bash
cat start_here.txt
```

## Exercise List

### Level 1: First Encounter with chmod
- Exercise 1: Encounter a script that won't run
- Exercise 2: Reading permissions before changing
- Exercise 3: Understanding the x permission

### Level 2: Targeted Permission Changes
- Exercise 1: Adding x to owner only (chmod u+x)
- Exercise 2: Group execute permissions (chmod g+x)
- Exercise 3: Combining permissions

### Level 3: Real-World Scenarios
- Exercise 1: Fixing a broken project
- Exercise 2: Understanding when x is NOT needed
- Exercise 3: Complete fix challenge

## Commands You'll Use

### Reading Permissions
- `ls -l` - List files with detailed permissions
- `ls -la` - List all files including hidden ones

### Changing Permissions
- `chmod +x <file>` - Add execute permission for everyone
- `chmod u+x <file>` - Add execute permission for owner only
- `chmod g+x <file>` - Add execute permission for group only
- `chmod u+x,g+x <file>` - Add execute for owner and group

### Running Scripts
- `./script.sh` - Run a script in current directory
- `bash script.sh` - Run script with bash (doesn't require x)

## Important Tips

1. **Always read first** - Use `ls -l` before using `chmod`
2. **x is required** - Scripts need execute permission to run
3. **Targeted changes** - Use u+x, g+x, or +x based on your needs
4. **Not all files need x** - Only scripts need execute permission
5. **Permission denied means no x** - If you get "Permission denied", check for x

## Safety Rules

- **Read before changing** - Always check permissions with `ls -l` first
- **Work in the lab directory** - All exercises are safe here
- **Understand what you're changing** - Know why you're adding x
- **Test after changes** - Try running the script after fixing permissions

## Lab Submission

After completing all exercises:

1. Create a file called `my_answers.txt` in the lab directory
2. Write short answers to each exercise question
3. Include your reflections on what you learned
4. Save the file

## Help

If you get stuck:

1. Read the instructions again in the current clue file
2. Check permissions with `ls -l` - look for the `x` in permissions
3. Remember: Scripts need `x` to run
4. Use `chmod +x` to add execute permission
5. Try running the script with `./script.sh` after fixing

## Good Luck!

Remember: When a script doesn't run, it's usually because it's missing the execute permission. Learn to read permissions first, then fix them with `chmod`!

---

**Linux Course - Day 2**  
**Why Script Doesn't Run Lab**  
**Version**: v2.6
