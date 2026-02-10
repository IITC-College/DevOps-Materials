# Shell Scripting Lab: Case Statements

## Goal

Master the bash `case` statement for building clean, maintainable menu-driven scripts. You'll progress from simple number menus to ops tools that run real commands—no functions required (those come in the Functions lab).

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

## Completion

You've successfully learned:
- Basic `case` statement syntax
- Pattern matching with numbers and strings
- The default branch with `*)`
- Exit codes in case branches
- Executing real commands in case branches
- Building clean, menu-driven scripts

The `case` statement is cleaner than long `if/elif` chains when you have many options to handle. It's perfect for menu systems, command routing, and option parsing. Once you learn functions (Functions lab), you can combine case with functions for even cleaner menus!
