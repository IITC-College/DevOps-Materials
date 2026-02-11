# Shell Scripting Lab: Conditionals

## Goal

Master bash conditional statements to build safer, smarter scripts. You'll learn to check if files and directories exist, validate user input, and create robust pre-deployment validation scripts.

## Prerequisites

- Script Basics, Variables, and Input labs (or equivalent knowledge)
- Linux system with bash
- A text editor

## Tasks

### Task 1: Check if a File Exists

**Objective:** Learn to use `[ -f ]` to check file existence

**Requirements:**
- First, explore the available config files: `ls src/data/configs/`
- Create a script called `check_config.sh`
- Add the shebang line
- Create a CONFIG variable that stores the path to `.env.prod`
- Use an if/else conditional to check if the file exists
- If it exists, print "Config file exists."
- If it doesn't exist, print "Config file not found."
- Test with the existing file
- Then change the path to a non-existent file and test again

**Technical Hints:**
- File existence test: `[ -f "filepath" ]`
- Conditional syntax: `if [ test ]; then ... else ... fi`
- **CRITICAL:** Always quote variables in tests: `"$VAR"`
- The `-f` flag tests for regular files
- Path should be relative to where you run the script

**Expected Output:**
- With `.env.prod`: "Config file exists."
- With `.env.missing`: "Config file not found."

**Testing:**
1. Run with path to `.env.prod` - should say "exists"
2. Change CONFIG to `.env.missing` - should say "not found"
3. Change back to verify it still works

**Script Name:** `check_config.sh`

---

### Task 2: Check if a Directory Exists

**Objective:** Learn to use `[ -d ]` to check directory existence

**Requirements:**
- First, explore the environment directories: `ls src/data/environments/`
- Create a script called `check_dir.sh` (or extend `check_config.sh`)
- Add the shebang if creating new file
- Create a DEPLOY_DIR variable storing the path to the "prod" directory
- Use an if/else conditional to check if the directory exists
- If it exists, print "Deploy directory exists."
- If not, print "Deploy directory not found."
- Test with existing directory, then test with non-existent directory

**Technical Hints:**
- Directory existence test: `[ -d "dirpath" ]`
- The `-d` flag tests for directories (vs `-f` for files)
- Same if/else structure as Task 1
- Quote the variable: `"$DEPLOY_DIR"`
- Can add this to existing script or create new one

**Expected Output:**
- With `prod`: "Deploy directory exists."
- With `missing`: "Deploy directory not found."

**Testing:**
1. Run with path to `prod` directory - should say "exists"
2. Change DEPLOY_DIR to `missing` - should say "not found"
3. This shows you can check files AND directories

**Script Name:** `check_dir.sh` or extended `check_config.sh`

---

### Task 3: Validate Empty Input

**Objective:** Learn to use `[ -z ]` to check for empty strings

**Requirements:**
- Create a script called `validate_input.sh`
- Add the shebang line
- Prompt the user to enter an environment (prod or staging)
- Store the input in an ENV variable
- Check if the ENV variable is empty
- If empty, print an error message and exit with code 1
- If not empty, print "Environment: [env value]"
- Test both scenarios: with input and without input

**Technical Hints:**
- Empty string test: `[ -z "$VAR" ]` (z = zero length)
- Read with prompt: `read -p "prompt" VARIABLE`
- Exit with error: `exit 1`
- Exit with success: `exit 0` (or no explicit exit)
- The error check should come BEFORE using the variable

**Expected Output:**
- With "prod": "Environment: prod"
- With empty input: "Error: environment cannot be empty." (and script exits)

**Testing:**
1. Run and type "prod" - should print "Environment: prod"
2. Run and press Enter immediately - should show error and exit
3. Check exit code with `echo $?` - should be 1 for error

**Script Name:** `validate_input.sh`

---

### Task 4: Validate Environment Values

**Objective:** Use `if/elif/else` to restrict input to specific allowed values

**Requirements:**
- Create a script called `validate_env.sh`
- Add the shebang
- Prompt user to enter environment (prod or staging)
- Store in ENV variable
- First, check if ENV is empty (like Task 3) - if so, error and exit
- Then check if ENV equals "prod" - if so, print "Deploying to PRODUCTION."
- Else if ENV equals "staging" - print "Deploying to STAGING."
- Otherwise, print error message and exit with code 1
- Test with all scenarios: prod, staging, dev (invalid), and empty

**Technical Hints:**
- String comparison: `[ "$VAR" = "value" ]`
- Use `elif` for additional conditions (not just `else if`)
- Structure: `if ... then ... elif ... then ... else ... fi`
- Check empty first, then check valid values
- Only valid values should succeed

**Expected Output:**
- "prod" → "Deploying to PRODUCTION."
- "staging" → "Deploying to STAGING."
- "dev" → "Error: environment must be prod or staging."
- empty → "Error: environment cannot be empty."

**Testing:**
1. Test "prod" - should deploy to production
2. Test "staging" - should deploy to staging
3. Test "dev" - should error (not valid)
4. Test empty - should error (empty check)
5. Verify exit codes with `echo $?`

**Script Name:** `validate_env.sh`

---

### Task 5: Create Directory Only if Missing

**Objective:** Use negation `[ ! -d ]` to conditionally create directories

**Requirements:**
- Create a script called `ensure_dir.sh`
- Add the shebang
- Set a TARGET variable with path "src/data/environments/backup"
- Check if the directory does NOT exist (negation)
- If it doesn't exist, create it and print a success message
- If it already exists, print that it already exists
- Run the script twice to test both scenarios

**Technical Hints:**
- Negation: `[ ! -d "path" ]` (! means NOT)
- Create directory: `mkdir -p "path"` (the -p creates parent dirs too)
- Same if/else structure, but with negated condition
- First run should create, second run should skip creation

**Expected Output:**
- First run: "Created src/data/environments/backup"
- Second run: "src/data/environments/backup already exists."

**Testing:**
1. Remove directory if it exists: `rm -rf src/data/environments/backup`
2. Run script - should create and print message
3. Run again - should say already exists
4. This pattern is common in setup/initialization scripts

**Note:** While `mkdir -p` handles this automatically, the conditional allows you to add custom logic (logging, permissions, etc.)

**Script Name:** `ensure_dir.sh`

---

### Task 6: Build a Pre-Deployment Validator

**Objective:** Combine multiple checks into one comprehensive validation script

**Requirements:**
- Create a script called `pre_deploy_validate.sh`
- Combine ALL validation techniques from previous tasks into one script
- Perform these checks in order (fail fast on first error):
  1. Check if config file exists (`.env.prod`)
  2. Check if deployment directory exists (`prod`)
  3. Prompt user for environment input
  4. Validate environment is not empty
  5. Validate environment is either "prod" or "staging"
- If ANY check fails, print error and exit with code 1
- If ALL checks pass, print success message with the environment name
- Test with various scenarios to verify all validations work

**Technical Hints:**
- Use all concepts from Tasks 1-5
- File check: `[ -f ]`, Directory check: `[ -d ]`
- Empty check: `[ -z ]`, String comparison: `[ "$VAR" = "value" ]`
- Multiple conditions: `[ "$X" != "a" ] && [ "$X" != "b" ]`
- Exit early on errors (defensive programming)
- Structure: config → directory → user input → validation → success

**Expected Output:**
- All checks pass: "All checks passed! Ready to deploy to prod."
- Config missing: "Error: Config file not found." (exit 1)
- Directory missing: "Error: Deploy directory not found." (exit 1)
- Empty input: "Error: Environment cannot be empty." (exit 1)
- Invalid env: "Error: Environment must be prod or staging." (exit 1)

**Testing:**
1. Run with all valid - should succeed
2. Rename config file - should fail at config check
3. Restore config, remove directory - should fail at directory check
4. Restore directory, enter empty - should fail at empty check
5. Enter "dev" - should fail at validation check
6. This is a complete pre-deployment validation script!

**Script Name:** `pre_deploy_validate.sh`

---

## Completion

You've successfully learned:
- File existence checks with `[ -f ]`
- Directory existence checks with `[ -d ]`
- Empty string checks with `[ -z ]`
- Negation with `[ ! ]`
- Multiple conditions with `if/elif/else`
- Building comprehensive validation logic
- Using exit codes to signal errors

These conditional skills are fundamental to writing safe, reliable DevOps scripts!
