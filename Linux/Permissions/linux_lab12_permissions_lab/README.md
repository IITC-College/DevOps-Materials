# Linux Lab 12 - Permissions Lab

Welcome to the hands-on Permissions Lab! In this lab you will **fix** broken file permissions, transfer ownership, and manage group-level access in a simulated company environment.

## Installation Instructions

### Method 1: Download with curl (Recommended)

```bash
curl -L -o lab.tar.gz https://github.com/IITC-College/DevOps-Materials/releases/download/v12.0-permissions/linux_lab12_permissions_lab.tar.gz
tar -xzf lab.tar.gz
cd linux_lab12_permissions_lab
```

> **Note:** If you get "not in gzip format" or a tiny download, the release may not be published yet. Use Method 2 or ask the instructor for the tarball.

### Method 2: From the repository (if release not yet published)

```bash
git clone https://github.com/IITC-College/DevOps-Jan26.git
cd DevOps-Jan26/Linux/Permissions/linux_lab12_permissions_lab
```

## Instructor Setup (Required Before Lab)

**CRITICAL**: Before students start the lab, instructors must run the environment setup script:

```bash
sudo ./setup_environment.sh
```

This single script will:
- Create lab users (**intern**, **developer**, **manager**) with locked passwords
- Create lab groups (**engineering**, **marketing**, **devops**)
- Add the student user to the **engineering** group
- Set **intentionally WRONG** permissions and ownership for students to fix
- Assign group memberships: intern → engineering; developer → engineering+devops; manager → engineering+marketing+devops

**Note**: Students may need to log out and back in (or run `newgrp engineering`) for group membership to take effect.

## Lab Objective

In this lab you will actively **fix** broken permissions in a simulated company environment:

- **chmod**: Fix overly permissive and overly restrictive file permissions using both **numeric (absolute)** and **symbolic** modes
- **chown**: Transfer file ownership to the correct users and departments
- **Group Management**: Ensure files are accessible to the right groups while protected from others
- **Multi-Group Scenarios**: Work with users who belong to multiple groups

## Important: What This Lab IS and ISN'T

- ❌ **NOT** about just reading permissions (that was Lab 6)
- ❌ **NOT** about using `chmod 777` to fix everything
- ✅ **IS** about applying the **principle of least privilege**
- ✅ **IS** about choosing the RIGHT permissions for each situation
- ✅ **IS** about understanding WHO should own WHAT

## How to Start?

1. Open the `start_here.txt` file - everything is there!
2. Read the instructions carefully
3. Follow the 10 steps in order

```bash
cat start_here.txt
```

## The 10 Steps

| Step | Topic | What You'll Fix |
|------|-------|-----------------|
| 1 | chmod (numeric) | Lock down exposed HR salary data |
| 2 | chmod (symbolic) | Make a build script executable |
| 3 | chmod (both modes) | Secure API keys and employee reviews |
| 4 | chown | Transfer engineering files to correct owner |
| 5 | chown + chgrp | Fix marketing department file ownership |
| 6 | chown + chmod | Unlock shared documents for all employees |
| 7 | ownership + execute | Fix automation scripts with correct access |
| 8 | data sensitivity | Secure reports with appropriate access levels |
| 9 | group analysis | Analyze multi-group access scenarios |
| 10 | final audit | Verify the entire company structure |

## Commands You'll Use

### Changing Permissions (chmod)
- `chmod 644 file` - Set exact permissions using numeric mode
- `chmod 600 file` - Owner read+write only
- `chmod 750 dir` - Owner full, group read+execute, others none
- `chmod u+x file` - Add execute for owner (symbolic)
- `chmod g+rw file` - Add read+write for group (symbolic)
- `chmod o-rwx file` - Remove all permissions for others (symbolic)

### Changing Ownership (chown/chgrp)
- `sudo chown user file` - Change file owner
- `sudo chown user:group file` - Change owner and group
- `sudo chgrp group file` - Change group only
- `sudo chown -R user:group dir/` - Recursive ownership change

### Reading Permissions
- `ls -l` - Detailed file listing with permissions
- `ls -la` - Include hidden files
- `stat file` - Detailed file info including numeric permissions
- `id` - Show your user ID and groups
- `groups user` - Show a user's groups
- `getent group groupname` - Show group members

## Important Tips

1. **Always verify** - Run `ls -l` after every change to confirm it worked
2. **Use `stat`** - It shows numeric permissions (e.g., 0644) which helps verify your work
3. **Principle of least privilege** - Give the minimum permissions needed, not more
4. **sudo is required** for chown and chgrp - you cannot change ownership without it
5. **Numeric vs symbolic** - Know when to use each: numeric for setting exact permissions, symbolic for adding/removing specific bits
6. **Group membership matters** - A user can only access group-permitted files if they are actually in that group

## Safety Rules

- **Never use chmod 777** - This is almost always wrong and a security risk
- **Don't change permissions on system files** - Only work within the lab directory
- **Use sudo carefully** - Only for chown/chgrp, not for bypassing permission checks
- **Read error messages** - They tell you exactly what went wrong

## Lab Submission

After completing all 10 steps:

1. Create a file called `my_answers.txt` in the lab directory
2. Write short answers to each step's questions
3. Include your reflections on what you learned
4. Save the file

## Help

If you get stuck:

1. Re-read the hints in `start_here.txt` for that step
2. Check `ls -l` output - it tells you the current state
3. Use `stat <file>` to see numeric permissions
4. Use `id` and `groups` to verify group memberships
5. Remember: `sudo` is needed for `chown` and `chgrp`
6. Ask the instructor if you're stuck for more than 10 minutes

## Good Luck!

You've already learned to READ permissions - now it's time to MASTER them. Think like a real SysAdmin: every file needs the RIGHT owner, the RIGHT group, and the RIGHT permissions. No more, no less.

---

**Linux Course - Day 2**
**Permissions Lab**
**Version**: v12.1
