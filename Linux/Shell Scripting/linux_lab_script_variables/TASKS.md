# Shell Scripting Lab: Variables

## Goal

Master bash variables and command substitution by creating backup scripts with dynamic values and timestamps. You'll learn to store values in variables, use them in output, and generate timestamps for file naming.

## Prerequisites

- Script Basics lab (or equivalent knowledge)
- Linux system with bash
- A text editor

## Tasks

### Task 1: Create a Script with Hardcoded Values

**Objective:** Build a simple backup script with hardcoded application information

**Instructions:**
1. Create a script called `backup_step1.sh`
2. Add a shebang line: `#!/bin/bash`
3. Add four echo statements:
   - "Backup started for app: myapp"
   - "Version: 1.0"
   - "Backing up..."
   - "Backup complete."
4. Make it executable with `chmod +x backup_step1.sh`
5. Run the script: `./backup_step1.sh`

**Expected Output:**
```
Backup started for app: myapp
Version: 1.0
Backing up...
Backup complete.
```

**Script Name:** `backup_step1.sh`

---

### Task 2: Convert Hardcoded Values to Variables

**Objective:** Learn to declare and use variables in bash

**Instructions:**
1. Create a new script called `backup_step2.sh`
2. Add the shebang line
3. Declare two variables at the top:
   - `APP_NAME="myapp"`
   - `VERSION="1.0"`
4. Use these variables in echo statements:
   - `echo "Backup started for app: $APP_NAME"`
   - `echo "Version: $VERSION"`
   - `echo "Backing up..."`
   - `echo "Backup complete."`
5. Make it executable and run it

**Expected Output:**
Same as Task 1, but now using variables

**Script Name:** `backup_step2.sh`

---

### Task 3: Add More Variables and Practice Syntax

**Objective:** Expand your variable usage and avoid common syntax errors

**Instructions:**
1. Open `backup_step2.sh` (or create `backup_step3.sh` as a copy)
2. Add a new variable: `BACKUP_DIR="backups"`
3. Add an echo statement: `echo "Target directory: $BACKUP_DIR"`
4. Test the script
5. Experiment: Try adding a space in the assignment (e.g., `APP_NAME = "myapp"`) and see what error you get
6. Fix it back to the correct syntax (no spaces around `=`)

**Expected Output:**
```
Backup started for app: myapp
Version: 1.0
Target directory: backups
Backing up...
Backup complete.
```

**Script Name:** `backup_step2.sh` (modified) or `backup_step3.sh`

---

### Task 4: Use Command Substitution for Dynamic Dates

**Objective:** Learn to capture command output in variables

**Instructions:**
1. Check the sample log files: `ls src/data/logs/`
2. Create a script called `backup_with_date.sh`
3. Add the shebang line
4. Add a DATE variable using command substitution: `DATE=$(date +%Y-%m-%d)`
5. Add echo statements:
   - `echo "Backup date: $DATE"`
   - `echo "Backing up logs from src/data/logs/..."`
6. Make it executable and run it

**Expected Output:**
```
Backup date: 2026-02-10
Backing up logs from src/data/logs/...
```
(Date will be today's date)

**Script Name:** `backup_with_date.sh`

---

### Task 5: Create Timestamped Backup Filenames

**Objective:** Combine variables to build dynamic filenames

**Instructions:**
1. Create a script called `backup_timestamped.sh`
2. Add the shebang
3. Add the DATE variable: `DATE=$(date +%Y-%m-%d)`
4. Create a backup filename variable: `BACKUP_FILE="backup_${DATE}.log"`
5. Add echo: `echo "Backup file will be: $BACKUP_FILE"`
6. Run the script

**Expected Output:**
```
Backup file will be: backup_2026-02-10.log
```
(With today's date)

**Script Name:** `backup_timestamped.sh`

---

### Task 6: Build a Complete Backup Script

**Objective:** Combine all concepts into one comprehensive script

**Instructions:**
1. Create a script called `backup_full.sh`
2. Add the shebang
3. Add all variables from previous tasks:
   - `APP_NAME="myapp"`
   - `VERSION="1.0"`
   - `BACKUP_DIR="backups"`
   - `DATE=$(date +%Y-%m-%d)`
   - `BACKUP_FILE="backup_${DATE}.log"`
4. Add echo statements that use all variables:
   - Start message with app name and version
   - Date information
   - Target directory
   - Backup filename
   - Completion message
5. Make it executable and run it

**Expected Output:**
```
Backup started for app: myapp
Version: 1.0
Backup date: 2026-02-10
Target directory: backups
Backup file will be: backup_2026-02-10.log
Backing up logs...
Backup complete.
```

**Script Name:** `backup_full.sh`

---

## Completion

You've successfully learned:
- How to declare variables in bash
- Correct variable syntax (no spaces around `=`)
- How to use variables in output with `$VAR`
- Command substitution with `$(command)`
- Creating dynamic values with date
- Combining variables for complex strings
