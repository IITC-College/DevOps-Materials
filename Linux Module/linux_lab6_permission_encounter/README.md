# Linux Lab - Permission Encounter

Welcome to your first Linux permissions practice lab!

## Installation Instructions

### Method 1: Download with curl (Recommended)

```bash
curl -L -o lab.tar.gz https://github.com/IITC-College/DevOps-Jan26/releases/download/v2.5/linux_lab6_permission_encounter.tar.gz
tar -xzf lab.tar.gz
cd linux_lab6_permission_encounter
```

## Instructor Setup (Required Before Lab)

**IMPORTANT**: Before students start the lab, instructors must run the environment setup script:

```bash
sudo ./setup_environment.sh
```

This script will:
- Set up file permissions for all exercises
- Ensure the lab environment is properly configured

**Note**: This lab does not require special users or groups - it works with any user.

## Lab Objective

In this lab you will encounter Linux permissions for the first time and learn to understand them **without fixing anything**:

- **Permission Denied**: Understanding that "Permission denied" is normal, not a bug
- **Reading Permissions**: Using `ls -l` to read file permissions, owners, and groups
- **Understanding Access**: Learning why you can or cannot access certain files
- **System Files**: Exploring real system files and their permission patterns

## Important: What This Lab Is NOT

- ❌ **NOT** about fixing permissions (that comes in later labs)
- ❌ **NOT** about using `chmod` or `sudo`
- ✅ **IS** about understanding and reading permissions
- ✅ **IS** about developing the habit of checking permissions before acting

## How to Start?

1. Open the `start_here.txt` file - this is where to begin!
2. Read the instructions carefully
3. Follow the exercises step by step

```bash
cat start_here.txt
```

## Exercise List

### Level 1: First Encounter with Permissions
- Exercise 1: Encounter "Permission denied" with system files
- Exercise 2: Understanding `ls -l` output format
- Exercise 3: Identifying file owners and groups

### Level 2: Reading Permissions
- Exercise 1: Decoding permission strings (rwx patterns)
- Exercise 2: Understanding why access is denied
- Exercise 3: Practice reading permissions before acting

### Level 3: Connecting Permissions to Reality
- Exercise 1: Detective challenge - finding accessible files
- Exercise 2: Exploring system files and their permissions
- Exercise 3: Final reflection and understanding

## Commands You'll Use

### Reading Permissions
- `ls -l` - List files with detailed permissions
- `ls -la` - List all files including hidden ones
- `id` - Show your user ID and groups
- `groups` - Show groups you belong to

### Reading Files
- `cat` - Display file contents
- `less` - View file contents page by page

### Navigation
- `cd` - Change directory
- `pwd` - Show current location
- `ls` - List directory contents

## Important Tips

1. **Permission denied is normal** - It's a security feature, not a bug!
2. **Read before acting** - Always use `ls -l` first to check permissions
3. **Understand, don't fix** - In this lab, you're learning to read permissions, not change them
4. **System files are protected** - That's why you can't read `/etc/shadow` - it's by design!
5. **Owner vs Group vs Others** - Learn to identify who has what permissions

## Safety Rules

- **Don't try to fix permissions** - This lab is about understanding, not changing
- **Don't use sudo** - You're learning what happens without it
- **Work in the lab directory** - All exercises are safe here
- **Read error messages** - They tell you exactly why access was denied

## Lab Submission

After completing all exercises:

1. Create a file called `my_answers.txt` in the lab directory
2. Write short answers to each exercise question
3. Include your reflections on what you learned
4. Save the file

## Help

If you get stuck:

1. Read the instructions again in the current clue file
2. Check the `ls -l` output - it contains all the information you need
3. Remember: Permission denied is **expected** for protected files
4. Use `id` and `groups` to see who you are in the system
5. Read error messages carefully - they explain what went wrong

## Good Luck!

Remember: Linux permissions are there to protect the system. Learning to read them is the first step to understanding Linux security. Don't be frustrated by "Permission denied" - it's working as designed!

---

**Linux Course - Day 2**  
**Permission Encounter Lab**  
**Version**: v2.5
