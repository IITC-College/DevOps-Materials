# Linux Lab - Users and Groups Management

Welcome to your Linux users and groups management practice lab!

## Installation Instructions

### Method 1: Download with curl (Recommended)

```bash
curl -L -o lab.tar.gz https://github.com/IITC-College/DevOps-Jan26/releases/download/vX.X/linux_users_groups_management.tar.gz
tar -xzf lab.tar.gz
cd linux_users_groups_management
```

## Instructor Setup (Required Before Lab)

**CRITICAL**: This lab **REQUIRES** environment setup before students can start. Instructors must run:

```bash
sudo ./setup_environment.sh
```

This script will:
- Create the lab directory structure and files (if missing)
- Verify sudo permissions are available for the student
- Set up initial test users and groups for practice
- Create example files for exercises
- Print setup confirmation

**Important Notes**:
- The script identifies the student user from `$SUDO_USER` (who ran sudo)
- Students will create and delete users/groups during exercises
- All operations use sudo and are logged for security
- Students should work only with lab-created test users

**Without running this setup script, the lab exercises will not work correctly!**

## Lab Objective

In this lab you will learn about user and group management in Linux:

- **Creating Users**: Understanding `adduser` vs `useradd` and their differences
- **Discovering Users**: Learning who you are with `whoami`, `id`, and `groups`
- **Viewing Users**: Using `getent passwd` to see all system users
- **Creating Groups**: Using `groupadd` to create groups and `getent group` to view them
- **Managing Groups**: Adding users to primary and secondary groups with `usermod`
- **Password Management**: Setting and changing passwords with `passwd`
- **User Deletion**: Removing users with and without their home directories
- **Group Deletion**: Cleaning up groups properly
- **Real-World Understanding**: Connecting user/group management to system security

## Important: What This Lab IS

- ✅ **IS** about creating and managing users in Linux
- ✅ **IS** about understanding groups and group membership
- ✅ **IS** about learning essential user management commands
- ✅ **IS** about understanding primary vs secondary groups
- ✅ **IS** about responsible user/group management practices

## How to Start?

1. Open the `start_here.txt` file - this is where to begin!
2. Read the instructions carefully
3. Follow the exercises step by step

```bash
cat start_here.txt
```

## Exercise List

### Level 1: Creating and Discovering Users
- Exercise 1: Creating users with adduser vs useradd
- Exercise 2: Discovering user information (id, whoami, groups)
- Exercise 3: Viewing all users with getent passwd

### Level 2: Groups and Management
- Exercise 1: Creating and viewing groups
- Exercise 2: Managing group membership (primary vs secondary)
- Exercise 3: Password management

### Level 3: Advanced Management and Cleanup
- Exercise 1: Replacing all groups for a user (understanding risks)
- Exercise 2: Deleting users properly
- Exercise 3: Cleaning up groups and handling scenarios

## Commands You'll Use

### User Creation
- `sudo adduser username` - Create user with home directory, password, and default settings (interactive)
- `sudo useradd username` - Basic user creation (manual configuration needed)

### User Deletion
- `sudo deluser username` - Delete user account only
- `sudo deluser --remove-home username` - Delete user and their home directory

### User Information
- `id` - Show your user ID, group ID, and all group memberships
- `id username` - Show specific user's ID and groups
- `whoami` - Display your current username
- `groups` - List groups you belong to
- `groups username` - List groups for specific user
- `getent passwd` - View all users on the system
- `getent passwd username` - View specific user information

### Password Management
- `sudo passwd username` - Set or change a user's password

### Group Creation and Deletion
- `sudo groupadd groupname` - Create a new group
- `sudo groupdel groupname` - Delete a group

### Group Information
- `getent group` - View all groups on the system
- `getent group groupname` - View information about specific group

### Group Management
- `sudo usermod -g groupname username` - Change user's primary group
- `sudo usermod -aG groupname username` - Add user to secondary group (append)
- `sudo usermod -G group1,group2 username` - Replace all secondary groups (⚠️ DANGER!)

### Navigation
- `cd <directory>` - Change directory
- `pwd` - Show current location

## Important Tips

1. **adduser vs useradd** - `adduser` is interactive and creates home directory automatically; `useradd` requires manual configuration
2. **Primary vs Secondary Groups** - Every user has ONE primary group (default for new files) and can have MULTIPLE secondary groups
3. **Use -aG for safety** - Always use `-aG` to ADD to groups; using `-G` alone REPLACES all groups!
4. **Verify before deleting** - Always check user information with `id` before deleting
5. **Home directory cleanup** - Decide if you need to keep or remove home directories when deleting users
6. **sudo is required** - All user/group management commands require sudo privileges
7. **Test users only** - Only modify test users created in this lab, never modify system users!

## Safety Rules

- **Understand before executing** - Read each command explanation before running it
- **Work with test users only** - Only create/modify/delete users created in this lab
- **Never modify system users** - Don't touch users like root, www-data, mysql, etc.
- **Verify changes** - Use `id`, `groups`, and `getent` commands to verify changes
- **Use sudo responsibly** - User management is logged and audited for security
- **Be careful with -G** - The `usermod -G` command (without -a) replaces ALL groups!

## Lab Submission

After completing all exercises:

1. Create a file called `my_answers.txt` in the lab directory
2. Write short answers to each exercise question
3. Include your reflections on what you learned about user and group management
4. Save the file

## Help

If you get stuck:

1. Read the instructions again in the current clue file
2. Check your identity with `whoami` and `id`
3. Verify user information with `getent passwd username`
4. Check group membership with `groups username`
5. Remember: All user/group management requires sudo
6. Use `man adduser`, `man usermod`, etc. for detailed command documentation

## Good Luck!

Remember: User and group management is a fundamental skill for Linux system administration. Understanding these concepts will help you manage multi-user systems, control access, and maintain security!

---

**Linux Course - Users and Groups Module**  
**Users and Groups Management Lab**  
**Version**: v1.0
