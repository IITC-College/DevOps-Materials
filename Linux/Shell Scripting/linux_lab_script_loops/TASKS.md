# Shell Scripting Lab: Loops

## Goal

Master bash loops (`for` and `while`) to automate repetitive tasks. You'll learn to iterate over lists, check multiple directories, implement retry patterns, and combine loops for complex automation scenarios.

## Prerequisites

- Script Basics, Variables, and Conditionals labs (or equivalent knowledge)
- Linux system with bash
- A text editor

## Tasks

### Task 1: Create a For Loop Over a List

**Objective:** Learn basic `for` loop syntax with a hardcoded list

**Requirements:**
- Create a script called `check_dirs_step1.sh`
- Add the shebang line
- Create a for loop that iterates over three directory names: project1, project2, logs
- For each iteration, print "Checking [directory name]"
- Make it executable and run it

**Technical Hints:**
- For loop syntax: `for VARIABLE in list of items; do ... done`
- The variable (e.g., DIR) gets each value in turn
- Use `$VARIABLE` inside the loop to reference current value
- Separate list items with spaces
- The `do` and `done` keywords mark the loop body

**Expected Output:**
```
Checking project1
Checking project2
Checking logs
```

**Testing:**
1. Run the script - should print three lines
2. Try adding another directory name to the list
3. Run again - should print four lines now

**Script Name:** `check_dirs_step1.sh`

---

### Task 2: Loop and Check Directory Existence

**Objective:** Combine loops with conditionals to check if directories exist

**Requirements:**
- Extend your `check_dirs_step1.sh` (or create `check_dirs_step2.sh`)
- First, verify what's in the directory: `ls src/data/environments/`
- Modify the loop to check if each directory actually exists
- For each directory in the list, build the full path: "src/data/environments/[dirname]"
- Use a conditional inside the loop to test existence
- If exists, print "  [dirname]: exists"
- If missing, print "  [dirname]: missing"

**Technical Hints:**
- Combine for loop with if statement (nest them)
- Build path inside loop: `DIR_PATH="src/data/environments/$DIR"`
- Use `[ -d "$DIR_PATH" ]` to test existence
- The conditional goes INSIDE the loop body
- Indentation (spaces) helps readability

**Expected Output:**
```
  project1: exists
  project2: missing
  logs: exists
```
(Based on what actually exists in src/data/environments/)

**Testing:**
1. Run and observe which directories exist
2. Create missing directory: `mkdir src/data/environments/project2`
3. Run again - should now show "exists" for project2

**Script Name:** `check_dirs_step1.sh` (extended) or `check_dirs_step2.sh`

---

### Task 3: Loop Over Items from a File

**Objective:** Read list items from a file and iterate over them

**Requirements:**
- First, examine the paths file: `cat src/data/configs/paths.txt`
- Create a script called `process_paths.sh`
- Add the shebang
- Create a for loop that iterates over the contents of the file
- Use command substitution to read the file
- For each path name, print "Processing [pathname]"
- Run the script

**Technical Hints:**
- Command substitution: `$(command)`
- Read file: `cat filename`
- Combine them: `for VAR in $(cat file); do`
- The output of `cat` becomes the list for the loop
- Each word/line in the file becomes one iteration

**Expected Output:**
```
Processing logs
Processing config
Processing backup
```
(Based on actual contents of paths.txt)

**Testing:**
1. Run the script
2. Edit paths.txt and add another line
3. Run again - should process the new item too
4. This shows dynamic list processing!

**Script Name:** `process_paths.sh`

---

### Task 4: Create a While Loop with Counter

**Objective:** Learn `while` loop syntax for count-based iteration

**Requirements:**
- Create a script called `run_count.sh`
- Add the shebang
- Initialize a counter variable COUNT starting at 1
- Create a while loop that runs while COUNT is less than or equal to 3
- Inside the loop, print "Run [count number]"
- Increment the counter after each iteration
- After the loop, print "Done."
- Run and observe the output

**Technical Hints:**
- While loop syntax: `while [ condition ]; do ... done`
- Numeric comparison: `[ $VAR -le number ]` (less than or equal)
- Increment counter: `COUNT=$((COUNT + 1))`
- Arithmetic syntax: `$((expression))`
- The condition is tested BEFORE each iteration

**Expected Output:**
```
Run 1
Run 2
Run 3
Done.
```

**Testing:**
1. Run the script as-is
2. Change `-le 3` to `-le 5` - should run 5 times
3. Change increment to `COUNT=$((COUNT + 2))` - should skip numbers
4. This shows how while loops use conditions

**Script Name:** `run_count.sh`

---

### Task 5: Implement a Retry Pattern

**Objective:** Use while loops to implement retry logic with break

**Requirements:**
- Create a script called `retry_check.sh`
- Add the shebang
- Set MAX_ATTEMPTS to 3
- Initialize ATTEMPT counter to 1
- Create a while loop that runs while ATTEMPT <= MAX_ATTEMPTS
- For each attempt:
  - Print "Attempt [number]..."
  - Simulate a check that succeeds on attempt 2 (use if statement)
  - If check succeeds (ATTEMPT equals 2), print success message and break out of loop
  - Otherwise, print "Not ready - retrying..." and increment counter
- After loop, print "Done."
- Test with and without the break statement

**Technical Hints:**
- Numeric equality: `[ $VAR -eq number ]`
- Break statement: `break` (exits loop immediately)
- Without break, loop continues until condition fails
- This pattern is common in DevOps (waiting for services, retries, etc.)
- Increment counter AFTER the check (not before)

**Expected Output (with break):**
```
Attempt 1...
  Not ready - retrying...
Attempt 2...
  OK - check passed!
Done.
```

**Testing:**
1. Run as-is - should stop at attempt 2
2. Remove `break` statement - should run all 3 attempts
3. Change `[ $ATTEMPT -eq 2 ]` to `[ $ATTEMPT -eq 1 ]` - should succeed immediately
4. This simulates real retry logic for health checks!

**Script Name:** `retry_check.sh`

---

### Task 6: Combine For and While Loops

**Objective:** Nest loops for complex scenarios like checking multiple directories with retry

**Requirements:**
- Create a script called `check_dirs_retry.sh`
- Add the shebang
- Create an outer for loop that iterates over: project1, project2
- For EACH directory in the loop:
  - Print "Checking directory: [dirname]"
  - Initialize attempt counter and max attempts (e.g., 2)
  - Create an inner while loop for retry logic
  - In the while loop, print attempt number
  - Check if the directory exists in "src/data/environments/"
  - If found, print "Found!" and break
  - If not found, print retry message and increment counter
  - After the while loop, check if max attempts exceeded
  - If exceeded, print failure message
- This combines all loop concepts into one realistic script

**Technical Hints:**
- Outer loop: `for DIR in list`
- Inner loop: `while [ condition ]`
- Reset ATTEMPT counter for EACH directory (inside for loop, before while)
- The while loop is INSIDE the for loop (nested)
- After while loop ends, check if it succeeded or failed
- Pattern: for each item, retry until success or max attempts

**Expected Output:**
```
Checking directory: project1
  Attempt 1...
  Found!
Checking directory: project2
  Attempt 1...
  Not found, retrying...
  Attempt 2...
  Not found, retrying...
  project2 not found after 2 attempts.
```
(Based on what actually exists)

**Testing:**
1. Run and observe retry logic for each directory
2. Create project2: `mkdir -p src/data/environments/project2`
3. Run again - both should be found on first attempt
4. This is a real-world pattern for checking multiple services/resources!

**Script Name:** `check_dirs_retry.sh`

---

## Completion

You've successfully learned:
- `for` loops with hardcoded lists
- `for` loops with command output
- Reading lists from files
- `while` loops with counters
- Arithmetic operations with `$((...))`
- The `break` statement to exit loops early
- Retry patterns (common in DevOps for health checks)
- Nesting loops for complex automation

Loops are essential for automation! Use them to:
- Check multiple servers
- Process multiple files
- Retry operations until success
- Wait for services to become ready
- Batch operations across environments
