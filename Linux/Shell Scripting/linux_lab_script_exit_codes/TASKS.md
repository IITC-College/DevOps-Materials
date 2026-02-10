# Shell Scripting Lab: Exit Codes

## Goal

Master exit codes to build robust CI/CD pipelines and automation. Learn how scripts communicate success or failure, chain commands with `&&` and `||`, and implement fail-fast patterns.

## Prerequisites

- Script Basics, Variables, Conditionals, and Case labs (or equivalent knowledge)
- Linux system with bash
- A text editor

## Tasks

### Task 1: Exit with Success or Failure

**Objective:** Learn to use `exit 0` (success) and `exit 1` (failure)

**Instructions:**
1. Create a script called `check_dir_exit.sh`
2. Check if a directory exists and exit with appropriate code:
   ```bash
   #!/bin/bash
   TARGET="${1:-src/data/environments/project1}"
   
   if [ -d "$TARGET" ]; then
       echo "Directory found: $TARGET"
       exit 0
   else
       echo "Directory NOT found: $TARGET"
       exit 1
   fi
   ```
3. Make it executable
4. Run with existing directory: `./check_dir_exit.sh`
5. Check exit code: `echo $?` (should be 0)
6. Run with missing directory: `./check_dir_exit.sh missing`
7. Check exit code: `echo $?` (should be 1)

**Expected Output:**
```
# With existing directory
Directory found: src/data/environments/project1
$ echo $?
0

# With missing directory
Directory NOT found: missing
$ echo $?
1
```

**Script Name:** `check_dir_exit.sh`

---

### Task 2: Check Config File with Exit Codes

**Objective:** Apply exit codes to file validation

**Instructions:**
1. Create a script called `check_config_exit.sh`
2. Check if a config file exists:
   ```bash
   #!/bin/bash
   CONFIG="${1:-src/data/configs/app.conf}"
   
   if [ -f "$CONFIG" ]; then
       echo "Config found: $CONFIG"
       exit 0
   else
       echo "Config NOT found: $CONFIG"
       exit 1
   fi
   ```
3. Test with valid and invalid paths
4. Check `echo $?` after each run

**Expected Output:**
- Valid path → exit code 0
- Invalid path → exit code 1

**Script Name:** `check_config_exit.sh`

---

### Task 3: Chain Commands with && and ||

**Objective:** Use exit codes to control command flow

**Instructions:**
1. Use your `check_config_exit.sh` script with `&&` and `||`:
   ```bash
   # This runs "Next step" only if check succeeds (exit 0)
   ./check_config_exit.sh && echo "Next step..."
   
   # This runs "Failed!" only if check fails (exit 1)
   ./check_config_exit.sh missing || echo "Failed!"
   
   # Combine both: success message OR failure message
   ./check_config_exit.sh && echo "Success!" || echo "Failed!"
   ```
2. Run each command and observe the behavior
3. Try with both valid and invalid paths

**Expected Behavior:**
- `&&` runs the next command only if exit code is 0
- `||` runs the next command only if exit code is non-zero
- Chain: `cmd1 && cmd2 || cmd3` → if cmd1 succeeds run cmd2, else run cmd3

**Script Name:** None (command-line testing)

---

### Task 4: Build a Fail-Fast Pipeline

**Objective:** Create a script that stops on first failure

**Instructions:**
1. Create a script called `pipeline_simple.sh`
2. Implement a multi-step validation pipeline:
   ```bash
   #!/bin/bash
   
   echo "=== Validation Pipeline ==="
   echo ""
   
   # Step 1: Check directory
   echo "Step 1: Checking directory..."
   if [ ! -d "src/data/environments/project1" ]; then
       echo "ERROR: Directory not found"
       exit 1
   fi
   echo "✓ Directory check passed"
   echo ""
   
   # Step 2: Check config
   echo "Step 2: Checking config..."
   if [ ! -f "src/data/configs/app.conf" ]; then
       echo "ERROR: Config file not found"
       exit 1
   fi
   echo "✓ Config check passed"
   echo ""
   
   # Step 3: Simulate deployment
   echo "Step 3: Deploying application..."
   echo "  → Stopping services..."
   echo "  → Copying files..."
   echo "  → Starting services..."
   echo "✓ Deployment complete"
   echo ""
   
   echo "=== All steps passed! ==="
   exit 0
   ```
3. Run the script (should succeed)
4. Break step 1 by changing the directory path to something that doesn't exist
5. Run again - deployment should never happen (fail-fast)

**Expected Output (success):**
```
=== Validation Pipeline ===

Step 1: Checking directory...
✓ Directory check passed

Step 2: Checking config...
✓ Config check passed

Step 3: Deploying application...
  → Stopping services...
  → Copying files...
  → Starting services...
✓ Deployment complete

=== All steps passed! ===
```

**Expected Output (failure at step 1):**
```
=== Validation Pipeline ===

Step 1: Checking directory...
ERROR: Directory not found
```
(Script exits immediately, steps 2 and 3 never run)

**Script Name:** `pipeline_simple.sh`

---

### Task 5: Create a Wrapper Script

**Objective:** Learn to capture and pass through exit codes

**Instructions:**
1. Create a script called `wrapper.sh`
2. Call another script and capture its exit code:
   ```bash
   #!/bin/bash
   
   echo "Running check_config_exit.sh..."
   ./check_config_exit.sh "$@"
   
   # Capture the exit code
   EXIT_CODE=$?
   
   echo ""
   echo "Script exited with code: $EXIT_CODE"
   
   # Pass the exit code through
   exit $EXIT_CODE
   ```
3. Run: `./wrapper.sh` (should exit with 0)
4. Run: `./wrapper.sh missing` (should exit with 1)
5. Check: `echo $?` after each run

**Expected Output:**
```
# With valid config
Running check_config_exit.sh...
Config found: src/data/configs/app.conf

Script exited with code: 0
$ echo $?
0

# With invalid path
Running check_config_exit.sh...
Config NOT found: missing

Script exited with code: 1
$ echo $?
1
```

**Script Name:** `wrapper.sh`

---

## Completion

You've successfully learned:
- Exit codes: 0 = success, non-zero = failure
- `$?` captures the last command's exit code
- `exit N` terminates script with code N
- `&&` chains commands (run next only if previous succeeded)
- `||` chains commands (run next only if previous failed)
- Fail-fast pattern: exit on first error
- Capturing and passing through exit codes
- Why exit codes matter in CI/CD

Exit codes are fundamental to automation and CI/CD:
- **Jenkins/GitLab CI/CD** marks steps as passed (green) or failed (red) based on exit codes
- **Scripts chained together** use exit codes to decide whether to continue
- **Make/build systems** stop on first failure
- **Monitoring systems** alert on non-zero exits
- **Professional scripts always use exit codes properly**
