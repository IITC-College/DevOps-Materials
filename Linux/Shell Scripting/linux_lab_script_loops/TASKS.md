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

**Instructions:**
1. Create a script called `check_dirs_step1.sh`
2. Add the shebang
3. Create a for loop that iterates over directory names:
   ```bash
   for DIR in project1 project2 logs; do
       echo "Checking $DIR"
   done
   ```
4. Make it executable and run it

**Expected Output:**
```
Checking project1
Checking project2
Checking logs
```

**Script Name:** `check_dirs_step1.sh`

---

### Task 2: Loop and Check Directory Existence

**Objective:** Combine loops with conditionals to check if directories exist

**Instructions:**
1. Extend your `check_dirs_step1.sh` (or create `check_dirs_step2.sh`)
2. Inside the loop, check if each directory exists:
   ```bash
   for DIR in project1 project2 logs; do
       DIR_PATH="src/data/environments/$DIR"
       if [ -d "$DIR_PATH" ]; then
           echo "  $DIR: exists"
       else
           echo "  $DIR: missing"
       fi
   done
   ```
3. Run the script
4. Verify by checking: `ls src/data/environments/`

**Expected Output:**
```
  project1: exists
  project2: missing
  logs: exists
```
(project2 doesn't exist in the src/data/environments folder)

**Script Name:** `check_dirs_step1.sh` (extended) or `check_dirs_step2.sh`

---

### Task 3: Loop Over Items from a File

**Objective:** Read list items from a file and iterate over them

**Instructions:**
1. Check the paths file: `cat src/data/configs/paths.txt`
2. Create a script called `process_paths.sh`
3. Loop over the paths from the file:
   ```bash
   #!/bin/bash
   for PATHNAME in $(cat src/data/configs/paths.txt); do
       echo "Processing $PATHNAME"
   done
   ```
4. Run the script

**Expected Output:**
```
Processing logs
Processing config
Processing backup
```

**Script Name:** `process_paths.sh`

---

### Task 4: Create a While Loop with Counter

**Objective:** Learn `while` loop syntax for count-based iteration

**Instructions:**
1. Create a script called `run_count.sh`
2. Use a while loop with a counter:
   ```bash
   #!/bin/bash
   COUNT=1
   while [ $COUNT -le 3 ]; do
       echo "Run $COUNT"
       COUNT=$((COUNT + 1))
   done
   echo "Done."
   ```
3. Run the script
4. Experiment: Change `-le 3` to `-le 5` and run again

**Expected Output:**
```
Run 1
Run 2
Run 3
Done.
```

**Script Name:** `run_count.sh`

---

### Task 5: Implement a Retry Pattern

**Objective:** Use while loops to implement retry logic with break

**Instructions:**
1. Create a script called `retry_check.sh`
2. Implement a retry pattern:
   ```bash
   #!/bin/bash
   MAX_ATTEMPTS=3
   ATTEMPT=1
   
   while [ $ATTEMPT -le $MAX_ATTEMPTS ]; do
       echo "Attempt $ATTEMPT..."
       
       # Simulate a check that passes on attempt 2
       if [ $ATTEMPT -eq 2 ]; then
           echo "  OK - check passed!"
           break
       fi
       
       echo "  Not ready - retrying..."
       ATTEMPT=$((ATTEMPT + 1))
   done
   
   echo "Done."
   ```
3. Run the script (should stop at attempt 2)
4. Remove the `break` statement and run again (should run all 3 attempts)

**Expected Output (with break):**
```
Attempt 1...
  Not ready - retrying...
Attempt 2...
  OK - check passed!
Done.
```

**Script Name:** `retry_check.sh`

---

### Task 6: Combine For and While Loops

**Objective:** Nest loops for complex scenarios like checking multiple directories with retry

**Instructions:**
1. Create a script called `check_dirs_retry.sh`
2. Combine a for loop (directories) with a while loop (retry):
   ```bash
   #!/bin/bash
   
   for DIR in project1 project2; do
       echo "Checking directory: $DIR"
       ATTEMPT=1
       MAX_ATTEMPTS=2
       
       while [ $ATTEMPT -le $MAX_ATTEMPTS ]; do
           echo "  Attempt $ATTEMPT..."
           
           if [ -d "src/data/environments/$DIR" ]; then
               echo "  Found!"
               break
           fi
           
           echo "  Not found, retrying..."
           ATTEMPT=$((ATTEMPT + 1))
       done
       
       if [ $ATTEMPT -gt $MAX_ATTEMPTS ]; then
           echo "  $DIR not found after $MAX_ATTEMPTS attempts."
       fi
   done
   ```
3. Run the script and observe how it checks each directory with retry logic

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
