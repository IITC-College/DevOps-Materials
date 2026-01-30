# Linux Lab - Understanding sudo: When and Why

Welcome to your Linux sudo practice lab!

## Installation Instructions

### Method 1: Download with curl (Recommended)

```bash
curl -L -o lab.tar.gz https://github.com/IITC-College/DevOps-Jan26/releases/download/v2.8/linux_lab9_sudo_mindset.tar.gz
tar -xzf lab.tar.gz
cd linux_lab9_sudo_mindset
```

## Instructor Setup (Required Before Lab)

**IMPORTANT**: Before students start the lab, instructors must run the environment setup script:

```bash
sudo ./setup_environment.sh
```

This script will:
- Set up protected system files owned by root (to demonstrate when sudo is needed)
- Configure user app files with root ownership (simulating common ownership problems)
- Set up file permissions for all exercises
- Ensure the lab environment is properly configured

**Note**: This lab requires root ownership on some files to demonstrate sudo usage scenarios.

## Lab Objective

In this lab you will learn to use sudo responsibly and understand when it's actually needed:

- **Understanding sudo**: Learning what sudo does and when it's appropriate
- **Breaking Bad Habits**: Not using sudo automatically for every "Permission denied"
- **Critical Thinking**: Analyzing if sudo is truly needed or if it's a design problem
- **Audit Awareness**: Understanding that sudo usage is logged for accountability
- **Alternatives**: Learning to fix root causes (ownership/permissions) instead of working around them

## Important: What This Lab IS

- ✅ **IS** about understanding when sudo is actually needed
- ✅ **IS** about breaking the "sudo all the things" reflex
- ✅ **IS** about learning that sudo is logged and monitored
- ✅ **IS** about finding better solutions than using sudo repeatedly
- ✅ **IS** about developing critical thinking about privilege elevation

## Important: What This Lab Is NOT

- ❌ **NOT** about using sudo for everything
- ❌ **NOT** about bypassing security measures
- ❌ **NOT** about ignoring "Permission denied" errors
- ✅ **IS** about responsible and thoughtful use of sudo

## How to Start?

1. Open the `start_here.txt` file - this is where to begin!
2. Read the instructions carefully
3. Follow the exercises step by step

```bash
cat start_here.txt
```

## Exercise List

### Level 1: Understanding sudo Basics
- Exercise 1: Encountering permission denied and using sudo appropriately
- Exercise 2: Understanding when sudo is actually needed
- Exercise 3: Reading system files that require sudo

### Level 2: Alternatives and Audit
- Exercise 1: Discovering sudo alternatives (fixing ownership/permissions)
- Exercise 2: Understanding sudo logging and audit trails
- Exercise 3: Reading audit logs to see sudo usage

### Level 3: Critical Thinking and Responsibility
- Exercise 1: Decision making - sudo or design problem?
- Exercise 2: Complete sudo audit challenge
- Exercise 3: Final reflection on sudo responsibility

## Commands You'll Use

### Privilege Elevation
- `sudo <command>` - Run command with elevated privileges
- `sudo -l` - List commands you can run with sudo
- `id` - Show your user ID and groups
- `whoami` - Show current username

### Reading Permissions
- `ls -l` - List files with detailed permissions
- `ls -la` - List all files including hidden ones

### Changing Ownership/Permissions
- `sudo chown <user>:<group> <file>` - Change file ownership
- `chmod` - Change file permissions (from previous lab)

### Reading Files
- `cat` - Display file contents
- `less` - View file contents page by page
- `sudo cat` - Read files that require elevated privileges

### Audit Logs
- `sudo cat /var/log/auth.log` - View authentication log (Debian/Ubuntu)
- `sudo cat /var/log/secure` - View authentication log (RHEL/CentOS)
- `grep sudo` - Search for sudo entries in logs

## Important Tips

1. **"Permission denied" ≠ "Use sudo"** - Analyze first, then decide
2. **sudo is for administrative tasks** - Not for working around bad design
3. **sudo is logged** - You are accountable for what you do with elevated privileges
4. **Fix the root cause** - Change ownership/permissions instead of using sudo repeatedly
5. **sudo is powerful** - With great power comes great responsibility
6. **Think before sudo** - Ask yourself: "Is this really an administrative operation?"
7. **Audit trail exists** - Every sudo command is logged for security
8. **Alternatives exist** - Often you can fix permissions/ownership instead

## Safety Rules

- **Think before using sudo** - Analyze if sudo is truly needed
- **Read permissions first** - Use `ls -l` to understand why access is denied
- **Work in the lab directory** - All exercises are safe here
- **Understand what you're doing** - Don't blindly use sudo
- **Remember: sudo is logged** - Your actions are tracked
- **Use sudo to fix, not work around** - Change ownership/permissions when appropriate

## Lab Submission

After completing all exercises:

1. Create a file called `my_answers.txt` in the lab directory
2. Write short answers to each exercise question
3. Include your reflections on what you learned about sudo
4. Answer the final reflection questions from Level 3, Exercise 3
5. Save the file

## Help

If you get stuck:

1. Read the instructions again in the current clue file
2. Check permissions with `ls -l` - understand why access is denied
3. Ask yourself: "Is this really an administrative task?"
4. Consider alternatives: Can you fix ownership/permissions instead?
5. Remember: sudo is logged - think about accountability
6. Read error messages carefully - they explain what went wrong

## Good Luck!

Remember: sudo is a powerful tool that should be used thoughtfully and responsibly. Not every "Permission denied" requires sudo - sometimes the solution is to fix permissions or ownership. And always remember: your sudo usage is logged for security and accountability!

---

**Linux Course - Day 2**  
**Understanding sudo: When and Why Lab**  
**Version**: v2.8
