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

**Instructions:**
1. Look at the config files: `ls src/data/configs/`
2. Create a script called `check_config.sh`
3. Add the shebang and create a variable:
   ```bash
   #!/bin/bash
   CONFIG="src/data/configs/.env.prod"
   ```
4. Add a conditional:
   ```bash
   if [ -f "$CONFIG" ]; then
       echo "Config file exists."
   else
       echo "Config file not found."
   fi
   ```
5. Run the script - should say "Config file exists"
6. Change CONFIG to a non-existent file (e.g., `.env.missing`) and run again

**Expected Output:**
- With `.env.prod`: "Config file exists."
- With `.env.missing`: "Config file not found."

**Script Name:** `check_config.sh`

---

### Task 2: Check if a Directory Exists

**Objective:** Learn to use `[ -d ]` to check directory existence

**Instructions:**
1. Look at environment directories: `ls src/data/environments/`
2. Create a script called `check_dir.sh` or extend `check_config.sh`
3. Add a directory check:
   ```bash
   DEPLOY_DIR="src/data/environments/prod"
   if [ -d "$DEPLOY_DIR" ]; then
       echo "Deploy directory exists."
   else
       echo "Deploy directory not found."
   fi
   ```
4. Run with existing directory (`prod`), then change to non-existent (`missing`)

**Expected Output:**
- With `prod`: "Deploy directory exists."
- With `missing`: "Deploy directory not found."

**Script Name:** `check_dir.sh` or extended `check_config.sh`

---

### Task 3: Validate Empty Input

**Objective:** Learn to use `[ -z ]` to check for empty strings

**Instructions:**
1. Create a script called `validate_input.sh`
2. Add code to read input and check if it's empty:
   ```bash
   #!/bin/bash
   read -p "Enter environment (prod or staging): " ENV
   if [ -z "$ENV" ]; then
       echo "Error: environment cannot be empty."
       exit 1
   fi
   echo "Environment: $ENV"
   ```
3. Run with actual input (e.g., "prod")
4. Run again and press Enter without typing (empty input)

**Expected Output:**
- With "prod": "Environment: prod"
- With empty input: "Error: environment cannot be empty." (and script exits)

**Script Name:** `validate_input.sh`

---

### Task 4: Validate Environment Values

**Objective:** Use `if/elif/else` to restrict input to specific allowed values

**Instructions:**
1. Create a script called `validate_env.sh`
2. Read environment input
3. Check if it's empty first (reuse Task 3 logic)
4. Then check if it's "prod" or "staging":
   ```bash
   if [ "$ENV" = "prod" ]; then
       echo "Deploying to PRODUCTION."
   elif [ "$ENV" = "staging" ]; then
       echo "Deploying to STAGING."
   else
       echo "Error: environment must be prod or staging."
       exit 1
   fi
   ```
5. Test with: "prod", "staging", "dev" (should error), and empty (should error)

**Expected Output:**
- "prod" → "Deploying to PRODUCTION."
- "staging" → "Deploying to STAGING."
- "dev" → "Error: environment must be prod or staging."

**Script Name:** `validate_env.sh`

---

### Task 5: Create Directory Only if Missing

**Objective:** Use negation `[ ! -d ]` to conditionally create directories

**Instructions:**
1. Create a script called `ensure_dir.sh`
2. Set a target directory variable: `TARGET="src/data/environments/backup"`
3. Add logic:
   ```bash
   if [ ! -d "$TARGET" ]; then
       mkdir -p "$TARGET"
       echo "Created $TARGET"
   else
       echo "$TARGET already exists."
   fi
   ```
4. Run the script the first time (should create directory)
5. Run again (should say already exists)
6. Note: `mkdir -p` can do this alone, but the conditional lets you add custom logic

**Expected Output:**
- First run: "Created src/data/environments/backup"
- Second run: "src/data/environments/backup already exists."

**Script Name:** `ensure_dir.sh`

---

### Task 6: Build a Pre-Deployment Validator

**Objective:** Combine multiple checks into one comprehensive validation script

**Instructions:**
1. Create a script called `pre_deploy_validate.sh`
2. Combine checks from previous tasks:
   - Check if config file exists (`[ -f ]`)
   - Check if deployment directory exists (`[ -d ]`)
   - Read and validate environment input (not empty, must be prod or staging)
   - Print success message if all checks pass
3. Exit with error code 1 if any check fails
4. Test with various scenarios

**Example Structure:**
```bash
#!/bin/bash

# Check config file
CONFIG="src/data/configs/.env.prod"
if [ ! -f "$CONFIG" ]; then
    echo "Error: Config file not found."
    exit 1
fi

# Check deploy directory
DEPLOY_DIR="src/data/environments/prod"
if [ ! -d "$DEPLOY_DIR" ]; then
    echo "Error: Deploy directory not found."
    exit 1
fi

# Validate environment
read -p "Enter environment (prod or staging): " ENV
if [ -z "$ENV" ]; then
    echo "Error: Environment cannot be empty."
    exit 1
fi

if [ "$ENV" != "prod" ] && [ "$ENV" != "staging" ]; then
    echo "Error: Environment must be prod or staging."
    exit 1
fi

echo "All checks passed! Ready to deploy to $ENV."
```

**Expected Output:**
- All checks pass: "All checks passed! Ready to deploy to prod."
- Any check fails: Error message and exit

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
