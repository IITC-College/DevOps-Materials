# Shell Scripting Lab: Case Statements

## Goal

Master the bash `case` statement for building clean, maintainable menu-driven scripts. You'll progress from simple number menus to sophisticated ops tools with real commands and functions.

## Prerequisites

- Script Basics, Variables, Input, and Conditionals labs (or equivalent knowledge)
- Linux system with bash
- A text editor

## Tasks

### Task 1: Create a Case Statement with Numbers

**Objective:** Learn basic `case` syntax for menu options

**Instructions:**
1. Create a script called `menu_step1.sh`
2. Add the shebang
3. Read user input:
   ```bash
   read -p "Enter option (1/2/3): " CHOICE
   ```
4. Add a case statement:
   ```bash
   case "$CHOICE" in
       1)
           echo "You selected Option 1"
           ;;
       2)
           echo "You selected Option 2"
           ;;
       3)
           echo "You selected Option 3"
           ;;
       *)
           echo "Invalid option"
           ;;
   esac
   ```
5. Make executable and test with: 1, 2, 3, and 9

**Expected Output:**
- 1 → "You selected Option 1"
- 2 → "You selected Option 2"
- 9 → "Invalid option"

**Script Name:** `menu_step1.sh`

---

### Task 2: Case Statement with String Options

**Objective:** Use case with descriptive string values instead of numbers

**Instructions:**
1. Create a script called `menu_step2.sh`
2. Read input for string options:
   ```bash
   read -p "Enter option (disk/uptime/exit): " CHOICE
   ```
3. Add case with strings:
   ```bash
   case "$CHOICE" in
       disk)
           echo "Option: disk check"
           ;;
       uptime)
           echo "Option: uptime"
           ;;
       exit)
           echo "Exiting."
           ;;
       *)
           echo "Invalid option"
           ;;
   esac
   ```
4. Test with: disk, uptime, exit, restart (invalid)

**Expected Output:**
- "disk" → "Option: disk check"
- "uptime" → "Option: uptime"
- "restart" → "Invalid option"

**Script Name:** `menu_step2.sh`

---

### Task 3: Add Exit Codes to Default Branch

**Objective:** Learn to exit with error code 1 for invalid options

**Instructions:**
1. Open `menu_step2.sh` (or create `menu_step3.sh`)
2. Modify the default branch `*)` to exit with code 1:
   ```bash
   *)
       echo "Invalid option"
       exit 1
       ;;
   ```
3. Run with an invalid option (e.g., "restart")
4. Check the exit code: `echo $?` (should show 1)
5. Run with a valid option and check exit code (should show 0)

**Expected Output:**
- Invalid option exits with code 1
- Valid options exit with code 0
- Use `echo $?` immediately after script runs to see the exit code

**Script Name:** `menu_step2.sh` (modified) or `menu_step3.sh`

---

### Task 4: Add Real Commands to Menu

**Objective:** Execute actual system commands in case branches

**Instructions:**
1. Create a script called `menu_ops.sh`
2. Create a menu with real commands:
   ```bash
   #!/bin/bash
   read -p "Enter option (1=disk, 2=uptime, 3=exit): " CHOICE
   
   case "$CHOICE" in
       1)
           df -h .
           ;;
       2)
           uptime
           ;;
       3)
           echo "Exiting."
           exit 0
           ;;
       *)
           echo "Invalid option."
           exit 1
           ;;
   esac
   ```
3. Test each option:
   - 1 shows disk usage
   - 2 shows system uptime
   - 3 exits cleanly
   - 9 shows error and exits with code 1

**Expected Output:**
- 1 → disk usage output from `df`
- 2 → system uptime
- 3 → "Exiting."
- 9 → "Invalid option." (exit code 1)

**Script Name:** `menu_ops.sh`

---

### Task 5: Build Full Menu with Functions

**Objective:** Combine case statements with functions for clean, maintainable code

**Instructions:**
1. Create a script called `menu_full.sh`
2. Define functions at the top:
   ```bash
   #!/bin/bash
   
   show_disk() {
       echo "=== Disk Usage (current directory) ==="
       df -h .
   }
   
   show_uptime() {
       echo "=== System Uptime ==="
       uptime
   }
   
   show_status() {
       echo "=== System Status ==="
       echo "Hostname: $(hostname)"
       echo "Date: $(date)"
   }
   ```
3. Add a menu prompt:
   ```bash
   echo "Operations Menu:"
   echo "1) Check disk usage"
   echo "2) Show uptime"
   echo "3) Show system status"
   echo "4) Exit"
   read -p "Enter choice: " CHOICE
   ```
4. Add case statement calling functions:
   ```bash
   case "$CHOICE" in
       1)
           show_disk
           ;;
       2)
           show_uptime
           ;;
       3)
           show_status
           ;;
       4)
           echo "Exiting."
           exit 0
           ;;
       *)
           echo "Invalid option."
           exit 1
           ;;
   esac
   ```
5. Test all menu options

**Expected Output:**
A professional menu system with formatted output for each option.

**Script Name:** `menu_full.sh`

---

## Completion

You've successfully learned:
- Basic `case` statement syntax
- Pattern matching with numbers and strings
- The default branch with `*)`
- Exit codes in case branches
- Executing real commands in case branches
- Combining case statements with functions
- Building clean, maintainable menu-driven scripts

The `case` statement is cleaner than long `if/elif` chains when you have many options to handle. It's perfect for menu systems, command routing, and option parsing in DevOps tools!
