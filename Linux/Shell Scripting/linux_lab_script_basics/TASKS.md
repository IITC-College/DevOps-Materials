# Shell Scripting Lab: Basics

## Goal

Learn the fundamentals of creating and running bash scripts. You'll practice creating script files, adding shebangs, managing permissions, and executing scripts in different ways - all using simple echo commands.

## Prerequisites

- Linux system with bash
- A text editor (nano, vim, or any editor)

## Tasks

### Task 1: Create a Welcome Script

**Objective:** Create your first bash script with simple echo statements

**Instructions:**
1. Create a file called `welcome.sh`
2. Add these echo statements to the file:
   ```bash
   echo "================================"
   echo "Welcome to Bash Scripting!"
   echo "================================"
   echo ""
   echo "This is my first script."
   echo "Scripts help automate tasks."
   echo ""
   echo "Let's get started!"
   ```
3. Run the script: `bash welcome.sh`

**Expected Output:**
```
================================
Welcome to Bash Scripting!
================================

This is my first script.
Scripts help automate tasks.

Let's get started!
```

**Script Name:** `welcome.sh`

---

### Task 2: Add a Shebang Line

**Objective:** Add a shebang to tell the system which interpreter to use

**Instructions:**
1. Open `welcome.sh` in your editor
2. Add `#!/bin/bash` as the **very first line** (before the echo statements)
3. Save the file
4. Try to run it with: `./welcome.sh`

**Expected Output:**
You'll get a "Permission denied" error - this is normal! You need to make it executable first (next task).

**Script Name:** `welcome.sh` (modify existing)

---

### Task 3: Make the Script Executable

**Objective:** Add execute permission so you can run the script with `./`

**Instructions:**
1. Check current permissions: `ls -l welcome.sh`
2. Make it executable: `chmod +x welcome.sh`
3. Check permissions again: `ls -l welcome.sh` (notice the `x` now appears)
4. Run the script: `./welcome.sh`

**Expected Output:**
```
================================
Welcome to Bash Scripting!
================================

This is my first script.
Scripts help automate tasks.

Let's get started!
```

**Script Name:** `welcome.sh` (modify permissions)

---

### Task 4: Create a Deployment Messages Script

**Objective:** Create a new script that simulates deployment messages

**Instructions:**
1. Create a file called `deploy.sh`
2. Add the shebang as the first line: `#!/bin/bash`
3. Add echo statements that simulate a deployment:
   ```bash
   #!/bin/bash
   echo "Starting deployment..."
   echo ""
   echo "Step 1: Stopping old service"
   echo "Step 2: Backing up database"
   echo "Step 3: Copying new files"
   echo "Step 4: Running migrations"
   echo "Step 5: Starting new service"
   echo ""
   echo "Deployment complete!"
   ```
4. Make it executable: `chmod +x deploy.sh`
5. Run it: `./deploy.sh`

**Expected Output:**
```
Starting deployment...

Step 1: Stopping old service
Step 2: Backing up database
Step 3: Copying new files
Step 4: Running migrations
Step 5: Starting new service

Deployment complete!
```

**Script Name:** `deploy.sh`

---

### Task 5: Create a Status Report Script

**Objective:** Practice creating scripts with formatted output

**Instructions:**
1. Create a file called `status.sh`
2. Start with the shebang: `#!/bin/bash`
3. Add echo statements that display a status report:
   ```bash
   #!/bin/bash
   echo "========================================="
   echo "        SYSTEM STATUS REPORT"
   echo "========================================="
   echo ""
   echo "Service Status:"
   echo "  - Web Server: Running"
   echo "  - Database: Running"
   echo "  - Cache: Running"
   echo ""
   echo "Resource Usage:"
   echo "  - CPU: 45%"
   echo "  - Memory: 62%"
   echo "  - Disk: 78%"
   echo ""
   echo "Last Backup: 2 hours ago"
   echo "Next Scheduled Backup: In 6 hours"
   echo ""
   echo "========================================="
   ```
4. Make it executable: `chmod +x status.sh`
5. Run it: `./status.sh`

**Expected Output:**
```
=========================================
        SYSTEM STATUS REPORT
=========================================

Service Status:
  - Web Server: Running
  - Database: Running
  - Cache: Running

Resource Usage:
  - CPU: 45%
  - Memory: 62%
  - Disk: 78%

Last Backup: 2 hours ago
Next Scheduled Backup: In 6 hours

=========================================
```

**Script Name:** `status.sh`

---

## Completion

Congratulations! You've successfully created 5 bash scripts:
1. **welcome.sh** - Your first script with echo statements
2. **deploy.sh** - Simulated deployment messages
3. **status.sh** - Formatted status report

### Key Concepts Learned:
- Creating bash script files
- Adding shebang lines (`#!/bin/bash`)
- Using echo statements to display output
- Making scripts executable with `chmod +x`
- Running scripts with `./script.sh` vs `bash script.sh`
- Understanding file permissions

### What You've Mastered:
✓ Script creation and structure
✓ The purpose of shebangs
✓ File permissions basics
✓ Two methods of script execution
✓ Formatting output with echo

### Next Steps:
Now that you understand the basics of creating and running scripts, move on to the Variables lab to learn how to make your scripts dynamic and interactive!
