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

**Requirements:**
- Create a script called `backup_step1.sh`
- Add a shebang line at the very beginning
- Print exactly four messages:
  1. "Backup started for app: myapp"
  2. "Version: 1.0"
  3. "Backing up..."
  4. "Backup complete."
- Make the script executable
- Run the script to verify output

**Technical Hints:**
- Shebang for bash scripts: `#!/bin/bash`
- Use `echo` command to print messages
- Make executable: `chmod +x scriptname.sh`
- Run with: `./scriptname.sh`

**Expected Output:**
```
Backup started for app: myapp
Version: 1.0
Backing up...
Backup complete.
```

**Testing:**
1. Create the file with a text editor
2. Add the shebang as the first line
3. Add the echo statements
4. Save and make executable
5. Run and verify output matches exactly

**Script Name:** `backup_step1.sh`

---

### Task 2: Convert Hardcoded Values to Variables

**Objective:** Learn to declare and use variables in bash

**Requirements:**
- Create a new script called `backup_step2.sh`
- Add the shebang line
- Declare two variables at the top of the script:
  - APP_NAME should store "myapp"
  - VERSION should store "1.0"
- Print the same four messages as Task 1, but use the variables instead of hardcoded values:
  1. "Backup started for app: [use APP_NAME variable]"
  2. "Version: [use VERSION variable]"
  3. "Backing up..."
  4. "Backup complete."
- Make it executable and run it

**Technical Hints:**
- Variable syntax: `VARIABLE_NAME="value"` (no spaces around the `=`)
- Use variables in strings: `$VARIABLE_NAME` or `${VARIABLE_NAME}`
- Convention: Use UPPERCASE for variable names
- Variables must be declared before you use them

**Expected Output:**
```
Backup started for app: myapp
Version: 1.0
Backing up...
Backup complete.
```
(Same as Task 1, but now the values come from variables)

**Testing:**
1. Make executable and run to verify output
2. Try changing APP_NAME to "webapp" and re-run
3. The output should reflect the new value - this shows variables work!
4. Change it back to "myapp"

**Script Name:** `backup_step2.sh`

---

### Task 3: Add More Variables and Practice Syntax

**Objective:** Expand your variable usage and avoid common syntax errors

**Requirements:**
- Modify `backup_step2.sh` (or create `backup_step3.sh` as a copy)
- Add a third variable called BACKUP_DIR with the value "backups"
- Add a new message that prints "Target directory: [BACKUP_DIR value]"
- Place this new message after the version line but before "Backing up..."
- Test the script
- **Experiment:** Intentionally add a space around the `=` in one variable assignment (e.g., `APP_NAME = "myapp"`)
- Observe the error message
- Fix it back to correct syntax (no spaces around `=`)

**Technical Hints:**
- **CRITICAL:** Variable assignment has NO spaces around `=`
- Wrong: `VAR = "value"` (will cause "command not found" error)
- Right: `VAR="value"`
- Add the new variable at the top with the other variables
- Use `$BACKUP_DIR` to reference it in echo

**Expected Output:**
```
Backup started for app: myapp
Version: 1.0
Target directory: backups
Backing up...
Backup complete.
```

**Testing:**
1. Run with correct syntax - should work perfectly
2. Add space around `=` - should give error
3. Remove space - should work again
4. This teaches you the most common variable syntax mistake!

**Script Name:** `backup_step2.sh` (modified) or `backup_step3.sh`

---

### Task 4: Use Command Substitution for Dynamic Dates

**Objective:** Learn to capture command output in variables

**Requirements:**
- First, check what's in the sample log directory: `ls src/data/logs/`
- Create a script called `backup_with_date.sh`
- Add the shebang line
- Create a DATE variable that captures today's date in YYYY-MM-DD format
- Use command substitution to run the `date` command and store its output
- Print two messages:
  1. "Backup date: [date value]"
  2. "Backing up logs from src/data/logs/..."
- Make it executable and run it

**Technical Hints:**
- Command substitution syntax: `VARIABLE=$(command)`
- The `date` command with format: `date +formatstring`
- Date format codes: `%Y` (year), `%m` (month), `%d` (day)
- Combine format codes like: `+%Y-%m-%d`
- Test the date command first in terminal: `date +%Y-%m-%d`
- Then use it in your variable with `$()`

**Expected Output:**
```
Backup date: 2026-02-11
Backing up logs from src/data/logs/...
```
(Date will be whatever today's actual date is)

**Testing:**
1. Test the date format in terminal first
2. Run the script multiple days - date should update automatically
3. This shows the power of dynamic values!

**Script Name:** `backup_with_date.sh`

---

### Task 5: Create Timestamped Backup Filenames

**Objective:** Combine variables to build dynamic filenames

**Requirements:**
- Create a script called `backup_timestamped.sh`
- Add the shebang
- Create a DATE variable that stores today's date (same format as Task 4)
- Create a BACKUP_FILE variable that builds a filename like "backup_YYYY-MM-DD.log"
- The filename should embed the DATE variable value
- Print the message: "Backup file will be: [filename]"
- Run the script

**Technical Hints:**
- Embed variables in strings using: `"text_${VARIABLE}_more"`
- Curly braces `${}` help separate the variable from surrounding text
- Example pattern: `"prefix_${DATE}.extension"`
- The filename should include the word "backup", the date, and ".log" extension

**Expected Output:**
```
Backup file will be: backup_2026-02-11.log
```
(With today's actual date embedded in the filename)

**Testing:**
1. Run the script today
2. The date in the filename should match today's date
3. This is how real backup systems create unique filenames!

**Script Name:** `backup_timestamped.sh`

---

### Task 6: Build a Complete Backup Script

**Objective:** Combine all concepts into one comprehensive script

**Requirements:**
- Create a script called `backup_full.sh`
- Combine ALL the concepts from previous tasks into one complete script
- Declare five configuration variables at the top:
  - App name: "myapp"
  - Version: "1.0"
  - Backup directory: "backups"
  - Current date in YYYY-MM-DD format
  - Backup filename combining "backup_", the date, and ".log"
- Print seven messages that showcase all the variables:
  1. Backup started message with app name
  2. Version information
  3. Backup date
  4. Target directory
  5. Backup filename
  6. "Backing up logs..."
  7. "Backup complete."

**Technical Hints:**
- Organize all variables at the top (after shebang)
- Order matters: Define DATE before using it in BACKUP_FILE
- Use all the variable techniques you've learned:
  - Simple variable assignment
  - Command substitution
  - Variable embedding with `${}`
- This script demonstrates professional organization

**Expected Output:**
```
Backup started for app: myapp
Version: 1.0
Backup date: 2026-02-11
Target directory: backups
Backup file will be: backup_2026-02-11.log
Backing up logs...
Backup complete.
```

**Testing:**
1. Run and verify all output
2. Change APP_NAME to "webapp" and verify it updates
3. Run on different days - date should automatically update
4. This is a complete, reusable backup script template!

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
