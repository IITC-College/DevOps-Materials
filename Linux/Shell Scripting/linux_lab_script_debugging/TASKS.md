# Shell Scripting Lab: Debugging

## Goal

Develop debugging skills by finding and fixing common bash script errors. You'll work with broken CI/CD scripts and learn to identify syntax errors, logic bugs, and path issues.

## Prerequisites

- Script Basics, Variables, and Conditionals labs (or equivalent knowledge)
- Linux system with bash
- A text editor

## Important Notes

- All broken scripts are in the `src/` folder
- Each script has comments indicating what type of bug to find
- Try to fix the errors yourself before checking hints
- Test scripts by running them: `bash scriptname.sh`
- Config files are in `src/data/configs/`

## Tasks

### Task 1: Fix Variable Assignment Syntax Error

**Objective:** Fix spaces in variable assignment

**Instructions:**
1. Open `src/ci_build_broken.sh`
2. Try to run it: `bash src/ci_build_broken.sh`
3. You'll see an error like "APP_NAME: command not found"
4. Find the bug (hint: look at the variable assignment)
5. Fix it and run again

**The Bug:** Spaces around `=` in variable assignment

**Expected Output (after fix):**
```
Building myapp...
Build step complete.
```

**Script Name:** `src/ci_build_broken.sh`

---

### Task 2: Fix Missing Quotes in Conditional

**Objective:** Fix unquoted variable in conditional test

**Instructions:**
1. Open `src/ci_test_broken.sh`
2. Run it: `bash src/ci_test_broken.sh`
3. It might work now but could break with certain filenames
4. Find the bug (hint: look at the conditional test)
5. Fix by adding proper quotes

**The Bug:** Missing quotes around `$CONFIG` in `[ -f $CONFIG ]`

**Why it matters:** Without quotes, if CONFIG contains spaces or is empty, the test will fail with a syntax error.

**Expected Output (after fix):**
```
Config found.
```

**Script Name:** `src/ci_test_broken.sh`

---

### Task 3: Fix Missing 'then' Keyword

**Objective:** Fix syntax error in if statement

**Instructions:**
1. Open `src/ci_deploy_broken.sh`
2. Run it: `bash src/ci_deploy_broken.sh`
3. You'll see a syntax error about unexpected 'echo'
4. Find the bug (hint: if statements need a keyword after the condition)
5. Fix it and run again

**The Bug:** Missing `then` after the if condition

**Expected Output (after fix):**
```
Deploying to production...
Deploy complete.
```

**Script Name:** `src/ci_deploy_broken.sh`

---

### Task 4: Fix Incorrect File Path

**Objective:** Fix wrong path reference

**Instructions:**
1. Open `src/validate_broken.sh`
2. Run it: `bash src/validate_broken.sh`
3. It reports "Config not found" even though the file exists
4. Check what file it's looking for and where the file actually is
5. Fix the CONFIG variable to point to the correct path

**The Bug:** CONFIG points to `config.txt` but should point to `data/configs/build_config.txt`

**Expected Output (after fix):**
```
Config found.
Validation passed.
```

**Script Name:** `src/validate_broken.sh`

---

### Task 5: Fix Missing 'fi' Keyword

**Objective:** Fix unclosed if statement

**Instructions:**
1. Open `src/pipeline_broken.sh`
2. Run it: `bash src/pipeline_broken.sh`
3. You'll see a syntax error about unexpected end of file
4. Find the bug (hint: every if needs a closing keyword)
5. Fix it and run again

**The Bug:** Missing `fi` to close the if statement

**Expected Output (after fix):**
```
Starting pipeline...
Step 1: validation passed
Pipeline step complete.
```

**Script Name:** `src/pipeline_broken.sh`

---

### Task 6: Fix Multiple Bugs in Complete CI Script

**Objective:** Find and fix ALL bugs in one script (comprehensive challenge)

**Instructions:**
1. Open `src/ci_full_broken.sh`
2. This script has MULTIPLE bugs from previous tasks
3. Try to run it and observe the errors
4. Fix ALL bugs:
   - Spaces in variable assignment
   - Missing quotes in conditional
   - Wrong file path
   - Missing `then` keyword
   - Missing `fi` keyword
5. Run the script after each fix to find the next error
6. Keep fixing until the script runs successfully

**The Bugs:**
1. `APP_NAME = "myapp"` → spaces around =
2. `[ -f $CONFIG ]` → missing quotes
3. `CONFIG="config.txt"` → wrong path
4. `if [ ... ]` → missing then
5. Missing `fi` at end

**Expected Output (after all fixes):**
```
Config found.
CI build complete.
```

**Script Name:** `src/ci_full_broken.sh`

---

## Completion

You've successfully learned:
- Common bash syntax errors and how to fix them
- Variable assignment must have no spaces: `VAR="value"` not `VAR = "value"`
- Always quote variables in tests: `[ -f "$VAR" ]`
- If statements need `then` and `fi` keywords
- Relative paths must point to the correct location
- How to systematically debug scripts
- Reading error messages to identify problems

## Debugging Checklist

When debugging bash scripts, check:
- ✓ Variable assignments (no spaces around `=`)
- ✓ Quotes around variables in conditionals
- ✓ `then` after if/elif conditions
- ✓ `fi` to close if statements
- ✓ `done` to close loops
- ✓ `esac` to close case statements
- ✓ File paths (absolute vs relative)
- ✓ Permissions (script executable?)
- ✓ Syntax: `;` and `then` placement

## Debugging Tools
- `bash -x script.sh` → trace execution
- `bash -n script.sh` → check syntax without running
- `set -x` in script → enable tracing
- `set -e` in script → exit on error
- `echo "DEBUG: VAR=$VAR"` → print variables
