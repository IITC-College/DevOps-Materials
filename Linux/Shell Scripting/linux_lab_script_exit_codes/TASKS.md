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

**Requirements:**
- Create a script called `check_dir_exit.sh`
- Add the shebang
- Accept a directory path as first command-line argument ($1)
- If no argument provided, use default: "src/data/environments/project1"
- Check if the directory exists
- If exists: print "Directory found: [path]" and exit with code 0
- If not: print "Directory NOT found: [path]" and exit with code 1
- Test both scenarios and verify exit codes

**Technical Hints:**
- Default parameter syntax: `VAR="${1:-default_value}"`
- Directory check: `[ -d "$PATH" ]`
- Exit success: `exit 0`
- Exit failure: `exit 1`
- Check last exit code: `echo $?` (immediately after running)
- Exit code 0 = success, non-zero = failure

**Expected Output:**
```
# With existing directory
./check_dir_exit.sh
Directory found: src/data/environments/project1
$ echo $?
0

# With missing directory
./check_dir_exit.sh missing
Directory NOT found: missing
$ echo $?
1
```

**Testing:**
1. Run without arguments - should find default directory (exit 0)
2. Run with "missing" - should not find it (exit 1)
3. Always check `echo $?` immediately after each run
4. Exit codes communicate success/failure to other scripts!

**Script Name:** `check_dir_exit.sh`

---

### Task 2: Check Config File with Exit Codes

**Objective:** Apply exit codes to file validation

**Requirements:**
- Create a script called `check_config_exit.sh`
- Add the shebang
- Accept a file path as first argument, default to "src/data/configs/app.conf"
- Check if the file exists (not directory - file!)
- If exists: print "Config found: [path]" and exit 0
- If not: print "Config NOT found: [path]" and exit 1
- Test with valid and invalid paths

**Technical Hints:**
- File check uses `[ -f ]` instead of `[ -d ]`
- Same exit code pattern as Task 1
- Default parameter: `"${1:-default}"`
- This script can be used by other scripts to validate config

**Expected Output:**
- Valid path → "Config found: ..." (exit 0)
- Invalid path → "Config NOT found: ..." (exit 1)

**Testing:**
1. Run without arguments - should find default config
2. Run with "missing.conf" - should exit with 1
3. Verify with `echo $?` each time

**Script Name:** `check_config_exit.sh`

---

### Task 3: Chain Commands with && and ||

**Objective:** Use exit codes to control command flow

**Requirements:**
- Use your `check_config_exit.sh` script from Task 2
- Test command chaining with `&&` (AND operator)
- Test command chaining with `||` (OR operator)
- Test combining both operators
- Observe how exit codes control which commands run

**Technical Hints:**
- `cmd1 && cmd2` - run cmd2 ONLY if cmd1 exits with 0
- `cmd1 || cmd2` - run cmd2 ONLY if cmd1 exits non-zero
- `cmd1 && cmd2 || cmd3` - if cmd1 succeeds run cmd2, else run cmd3
- These operators check `$?` automatically

**Commands to Test:**
```bash
# Test 1: AND operator (only runs on success)
./check_config_exit.sh && echo "Next step..."

# Test 2: OR operator (only runs on failure)
./check_config_exit.sh missing || echo "Failed!"

# Test 3: Combined (success OR failure path)
./check_config_exit.sh && echo "Success!" || echo "Failed!"
```

**Expected Behavior:**
- Test 1 with valid file: prints "Config found..." AND "Next step..."
- Test 2 with missing file: prints "Config NOT found..." AND "Failed!"
- Test 3: always prints either "Success!" or "Failed!" based on result

**Testing:**
1. Run each test command
2. Observe which parts execute
3. This is how CI/CD pipelines chain steps!

**Script Name:** None (command-line testing)

---

### Task 4: Build a Fail-Fast Pipeline

**Objective:** Create a script that stops on first failure

**Requirements:**
- Create a script called `pipeline_simple.sh`
- Implement a 3-step validation pipeline
- Print header: "=== Validation Pipeline ==="
- **Step 1:** Check if directory exists (src/data/environments/project1)
  - If not: print error and exit 1
  - If yes: print success
- **Step 2:** Check if config file exists (src/data/configs/app.conf)
  - If not: print error and exit 1
  - If yes: print success
- **Step 3:** Simulate deployment (just print messages)
  - Print stopping, copying, starting messages
  - Print completion message
- Print footer: "=== All steps passed! ==="
- Exit with 0 if all steps succeed
- Test: Run normally (should complete), then break step 1 and run (should fail fast)

**Technical Hints:**
- Use `[ ! -d ]` for negation (if NOT exists)
- Exit immediately on first failure (fail-fast pattern)
- If step 1 fails, steps 2 and 3 never execute
- This is how CI/CD pipelines work: stop on first error
- Each step should have clear success/error messages

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
(Script exits immediately - steps 2 and 3 never run)

**Testing:**
1. Run with valid paths - should complete all steps
2. Change step 1 directory to "missing" - should fail immediately
3. Restore step 1, break step 2 - should fail at step 2 (no step 3)
4. This demonstrates defensive programming!

**Script Name:** `pipeline_simple.sh`

---

### Task 5: Create a Wrapper Script

**Objective:** Learn to capture and pass through exit codes

**Requirements:**
- Create a script called `wrapper.sh`
- Add the shebang
- Print "Running check_config_exit.sh..."
- Call the `check_config_exit.sh` script
- Pass all arguments from wrapper to the called script
- Capture the exit code from the called script
- Print "Script exited with code: [code]"
- Exit the wrapper with the SAME exit code (pass-through)
- Test with valid and invalid arguments

**Technical Hints:**
- `$@` passes all command-line arguments to another script
- Capture exit code: `EXIT_CODE=$?` (must be immediately after command)
- Exit with variable: `exit $EXIT_CODE`
- Wrapper scripts monitor and log other scripts
- The wrapper's exit code should match the wrapped script

**Expected Output:**
```
# With valid config
./wrapper.sh
Running check_config_exit.sh...
Config found: src/data/configs/app.conf

Script exited with code: 0
$ echo $?
0

# With invalid path
./wrapper.sh missing
Running check_config_exit.sh...
Config NOT found: missing

Script exited with code: 1
$ echo $?
1
```

**Testing:**
1. Run without arguments - should exit 0
2. Check `echo $?` - should be 0
3. Run with "missing" - should exit 1
4. Check `echo $?` - should be 1
5. Wrapper preserves the exit code!

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
