# Linux Lab - Ownership and Groups

Welcome to your Linux ownership and groups practice lab!

## Installation Instructions

### Method 1: Download with curl (Recommended)

```bash
curl -L -o lab.tar.gz https://github.com/IITC-College/DevOps-Jan26/releases/download/v2.7/linux_lab8_ownership_and_groups.tar.gz
tar -xzf lab.tar.gz
cd linux_lab8_ownership_and_groups
```

## Instructor Setup (Required Before Lab)

**CRITICAL**: This lab **REQUIRES** environment setup before students can start. Instructors must run:

```bash
sudo ./setup_environment.sh
```

This script will:
- Create the `developers` group (if it doesn't exist)
- Add the student user to the `developers` group
- Create/verify service users (`www-data`, `mysql`) if needed
- Set up file ownership for all exercises:
  - `data/files/root_file.txt` → owned by root
  - `data/files/user_file.txt` → owned by student user
  - `data/files/group_file.txt` → owned by student:developers
  - `projects/web_app/*` → owned by www-data:www-data
  - `projects/database/*` → owned by mysql:mysql
  - `projects/shared_team/*` → owned by student:developers

**Important Notes**:
- The script identifies the student user from `$SUDO_USER` (who ran sudo)
- Students may need to log out and back in (or run `newgrp developers`) for group membership to take effect
- Students can verify group membership with: `groups`

**Without running this setup script, the lab exercises will not work correctly!**

## Lab Objective

In this lab you will learn about file ownership and groups in Linux:

- **Understanding Identity**: Learning who you are with `whoami`, `id`, and `groups`
- **Reading Ownership**: Identifying file owners and groups with `ls -l`
- **Understanding Access Control**: Learning when owner, group, or other permissions apply
- **Changing Ownership**: Using `chown` to change file ownership (with sudo)
- **Real-World Scenarios**: Understanding ownership in web servers, databases, and team projects

## Important: What This Lab IS

- ✅ **IS** about understanding your identity in Linux
- ✅ **IS** about reading file ownership from `ls -l` output
- ✅ **IS** about understanding when ownership blocks access
- ✅ **IS** about using `chown` to change ownership
- ✅ **IS** about connecting ownership to real DevOps scenarios

## How to Start?

1. Open the `start_here.txt` file - this is where to begin!
2. Read the instructions carefully
3. Follow the exercises step by step

```bash
cat start_here.txt
```

## Exercise List

### Level 1: Discovery - Who Am I?
- Exercise 1: Discovering your identity (whoami, id, groups)
- Exercise 2: Reading file ownership from ls -l
- Exercise 3: Understanding owner vs group vs other permissions

### Level 2: Understanding Blocks
- Exercise 1: When ownership blocks access
- Exercise 2: How group membership affects access
- Exercise 3: Changing ownership with chown

### Level 3: Real-World Application
- Exercise 1: Web server file ownership
- Exercise 2: Team projects and shared groups
- Exercise 3: Complete ownership challenge

## Commands You'll Use

### Identity Commands
- `whoami` - Show your username
- `id` - Show your user ID, group ID, and group memberships
- `groups` - List groups you belong to

### Reading Ownership
- `ls -l` - List files with detailed permissions and ownership
- `ls -la` - List all files including hidden ones, with ownership

### Changing Ownership
- `chown user:group file` - Change file ownership (requires sudo)
- `sudo chown user:user file` - Change ownership to yourself
- `sudo chown user:group file` - Change both owner and group

### Navigation
- `cd <directory>` - Change directory
- `pwd` - Show current location

## Important Tips

1. **Know yourself first** - Always check `whoami` and `id` to understand your identity
2. **Read ownership** - Use `ls -l` to see who owns files before trying to access them
3. **Ownership matters** - Even with `rwx` permissions, ownership determines access
4. **chown requires sudo** - Only root can change file ownership (security!)
5. **Groups enable sharing** - Files owned by your group are accessible if group permissions allow

## Safety Rules

- **Understand before changing** - Always check ownership with `ls -l` first
- **Work in the lab directory** - All exercises are safe here
- **Use sudo carefully** - Only use `sudo chown` on lab files, understand why it's needed
- **Verify changes** - Use `ls -l` after `chown` to confirm ownership changed

## Lab Submission

After completing all exercises:

1. Create a file called `my_answers.txt` in the lab directory
2. Write short answers to each exercise question
3. Include your reflections on what you learned about ownership
4. Save the file

## Help

If you get stuck:

1. Read the instructions again in the current clue file
2. Check your identity with `whoami` and `id`
3. Check file ownership with `ls -l` - look for the owner:group pattern
4. Remember: Ownership determines which permission set applies (owner/group/other)
5. Use `groups` to see if you're a member of a file's group

## Good Luck!

Remember: Permissions tell you WHAT you can do, but ownership tells you WHO you are. Understanding both is essential for Linux mastery!

---

**Linux Course - Day 2, Part 3**  
**Ownership and Groups Lab**  
**Version**: v2.7
