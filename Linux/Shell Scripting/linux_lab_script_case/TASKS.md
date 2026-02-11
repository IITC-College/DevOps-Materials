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

**Requirements:**
- Create a script called `menu_step1.sh`
- Add the shebang
- Prompt user to enter an option (1, 2, or 3)
- Store input in CHOICE variable
- Use a case statement to handle each option:
  - Option 1: print "You selected Option 1"
  - Option 2: print "You selected Option 2"
  - Option 3: print "You selected Option 3"
  - Any other input: print "Invalid option"
- Make executable and test with different inputs

**Technical Hints:**
- Case syntax: `case "$VAR" in ... esac`
- Each pattern ends with `)`
- Each branch ends with `;;`
- Default case: `*)` matches anything not matched above
- Quote the variable: `"$CHOICE"`
- Case is cleaner than multiple if/elif for many options

**Expected Output:**
- 1 → "You selected Option 1"
- 2 → "You selected Option 2"
- 3 → "You selected Option 3"
- 9 → "Invalid option"

**Testing:**
1. Test with 1, 2, 3 - should match specific options
2. Test with 9 or any other input - should show "Invalid option"
3. Test with empty input - should also hit default case

**Script Name:** `menu_step1.sh`

---

### Task 2: Case Statement with String Options

**Objective:** Use case with descriptive string values instead of numbers

**Requirements:**
- Create a script called `menu_step2.sh`
- Add the shebang
- Prompt user to enter an option: disk, uptime, or exit
- Store input in CHOICE variable
- Use case statement with string matching:
  - "disk": print "Option: disk check"
  - "uptime": print "Option: uptime"
  - "exit": print "Exiting."
  - Anything else: print "Invalid option"
- Test with various string inputs

**Technical Hints:**
- Case can match strings, not just numbers
- Patterns are case-sensitive: "disk" != "Disk"
- No quotes around patterns: `disk)` not `"disk")`
- But DO quote the variable: `case "$CHOICE" in`
- String matching is cleaner than multiple `[ "$VAR" = "value" ]` checks

**Expected Output:**
- "disk" → "Option: disk check"
- "uptime" → "Option: uptime"
- "exit" → "Exiting."
- "restart" → "Invalid option"

**Testing:**
1. Test with "disk", "uptime", "exit"
2. Test with "restart" (should be invalid)
3. Test with "Disk" (capital D) - should also be invalid (case-sensitive)

**Script Name:** `menu_step2.sh`

---

### Task 3: Add Exit Codes to Default Branch

**Objective:** Learn to exit with error code 1 for invalid options

**Requirements:**
- Modify `menu_step2.sh` (or create `menu_step3.sh`)
- Update the default branch (`*`) to exit with error code 1
- Keep the "Invalid option" message
- Valid options should complete normally (exit code 0)
- Test both valid and invalid options
- Verify exit codes using `echo $?` immediately after running

**Technical Hints:**
- `exit 1` means error (non-zero exit code)
- `exit 0` means success (can omit - default)
- Check exit code of previous command: `echo $?`
- Must check immediately - the value changes with each command
- Exit codes signal success/failure to other scripts/tools

**Expected Output:**
- Invalid option: prints message and exits with code 1
- Valid options: complete normally with code 0
- Verification: run `./script.sh` then immediately `echo $?`

**Testing:**
1. Run with "restart" (invalid)
2. Immediately run: `echo $?` - should show 1
3. Run with "disk" (valid)
4. Immediately run: `echo $?` - should show 0
5. This is how scripts communicate success/failure!

**Script Name:** `menu_step2.sh` (modified) or `menu_step3.sh`

---

### Task 4: Add Real Commands to Menu

**Objective:** Execute actual system commands in case branches

**Requirements:**
- Create a script called `menu_ops.sh`
- Add the shebang
- Prompt user with options: 1=disk, 2=uptime, 3=exit
- Store choice in CHOICE variable
- Use case statement to execute real commands:
  - Option 1: run `df -h .` (disk free space for current directory)
  - Option 2: run `uptime` (system uptime)
  - Option 3: print "Exiting." and exit with code 0
  - Invalid: print error and exit with code 1
- Test all options to see actual command output

**Technical Hints:**
- You can run ANY command in case branches
- `df -h .` shows disk usage in human-readable format
- `uptime` shows how long system has been running
- Explicit `exit 0` for successful exit option
- Each branch can have multiple commands
- Real ops menus would include: start service, stop service, check logs, etc.

**Expected Output:**
- 1 → disk usage output (filesystem, size, used, available, mounted on)
- 2 → system uptime (load averages, how long running)
- 3 → "Exiting."
- 9 → "Invalid option." (and exit code 1)

**Testing:**
1. Test option 1 - should show disk information
2. Test option 2 - should show uptime
3. Test option 3 - should exit cleanly
4. Test option 9 - should show error
5. This is a working ops menu!

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
