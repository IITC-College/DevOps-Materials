# Linux Lab - Default Permissions (umask)

Welcome to your Linux umask practice lab!

## Installation Instructions

### Method 1: Download with curl (Recommended)

```bash
curl -L -o lab.tar.gz https://github.com/IITC-College/DevOps-Jan26/releases/download/v2.9/linux_lab10_default_permissions.tar.gz
tar -xzf lab.tar.gz
cd linux_lab10_default_permissions
```

## Instructor Setup (Required Before Lab)

**IMPORTANT**: Before students start the lab, instructors must run the environment setup script:

```bash
sudo ./setup_environment.sh
```

This script will:
- Set up example files with permissions matching different umask values:
  - `umask_022/example_file.txt` → 644 (rw-r--r--)
  - `umask_027/example_file.txt` → 640 (rw-r-----)
  - `umask_077/example_file.txt` → 600 (rw-------)
- Set up directory permissions to match umask values
- Ensure the lab environment is properly configured

**Note**: This lab does not require special users or groups - it focuses on umask and default permissions.

## Lab Objective

In this lab you will learn about umask and default file permissions:

- **Understanding umask**: Learning how Linux determines default permissions for new files
- **The Formula**: Understanding 666 - umask for files, 777 - umask for directories
- **Comparing Values**: Analyzing different umask values and their security implications
- **Modifying umask**: Changing umask and observing the impact on new files
- **Real-World Scenarios**: Understanding when to use different umask values

## Important: What This Lab IS

- ✅ **IS** about understanding default permissions
- ✅ **IS** about learning the umask command
- ✅ **IS** about making informed decisions about file security
- ✅ **IS** about understanding that defaults are intentional, not random

## How to Start?

1. Open the `start_here.txt` file - this is where to begin!
2. Read the instructions carefully
3. Follow the exercises step by step

```bash
cat start_here.txt
```

## Exercise List

### Level 1: Understanding Current umask
- Exercise 1: Check current umask value
- Exercise 2: Create file and observe default permissions
- Exercise 3: Create directory and observe default permissions

### Level 2: Comparing Different umask Values
- Exercise 1: Analyze files created with different umasks
- Exercise 2: Calculate expected permissions from umask values
- Exercise 3: Understand security implications of different umasks

### Level 3: Modifying umask and Real-World Scenarios
- Exercise 1: Change umask temporarily
- Exercise 2: Create files with different umask values
- Exercise 3: Solve real-world scenarios requiring specific umask values

## Commands You'll Use

### Checking umask
- `umask` - Show current umask value (octal)
- `umask -S` - Show umask in symbolic format

### Creating Files and Directories
- `touch <file>` - Create empty file
- `mkdir <dir>` - Create directory

### Checking Permissions
- `ls -l` - List files with detailed permissions
- `ls -ld <dir>` - List directory with permissions

### Changing umask
- `umask <value>` - Change umask for current session (e.g., `umask 027`)

## Key Concepts

### The umask Formula

**For Files:**
- Default maximum: 666 (rw-rw-rw-)
- Formula: 666 - umask = resulting permissions
- Example: 666 - 022 = 644 (rw-r--r--)

**For Directories:**
- Default maximum: 777 (rwxrwxrwx)
- Formula: 777 - umask = resulting permissions
- Example: 777 - 022 = 755 (rwxr-xr-x)

### Common umask Values

- **022**: Others can read (common default, less secure)
  - Files: 644 (rw-r--r--)
  - Directories: 755 (rwxr-xr-x)

- **027**: Group can work, others nothing (team environments)
  - Files: 640 (rw-r-----)
  - Directories: 750 (rwxr-x---)

- **077**: Only owner has access (maximum security)
  - Files: 600 (rw-------)
  - Directories: 700 (rwx------)

## Important Tips

1. **umask is subtractive** - It removes permissions from the maximum
2. **Files vs Directories** - Different base values (666 vs 777)
3. **Session-specific** - umask changes don't persist unless configured
4. **Plan ahead** - Set umask BEFORE creating files
5. **Security vs Collaboration** - Balance based on your needs

## Safety Rules

- **Work in the lab directory** - All exercises are safe here
- **umask is temporary** - Changes only affect current session
- **Understand the formula** - Know why permissions are what they are
- **Compare scenarios** - See how different umasks affect security

## Lab Submission

After completing all exercises:

1. Create a file called `my_answers.txt` in the lab directory
2. Write short answers to each exercise question
3. Include your calculations and observations
4. Reflect on when you would use different umask values
5. Save the file

## Help

If you get stuck:

1. Read the instructions again in the current clue file
2. Check your umask with `umask`
3. Remember the formula: 666 - umask for files, 777 - umask for directories
4. Look at example files in `data/examples/` for reference
5. Check `data/logs/permissions_history.log` for hints

## Good Luck!

Remember: Default permissions are not random - they are intentional decisions. Understanding umask helps you make informed choices about file security and collaboration!

---

**Linux Course - Day 2, Part 5**  
**Default Permissions Lab (umask)**  
**Version**: v2.9
