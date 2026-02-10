# Shell Scripting Lab: Basics

## Goal

Learn to create, structure, and run bash scripts by building a simple deployment script. You'll master shebangs, file permissions, and execution methods.

## Prerequisites

- Linux system with bash
- A text editor (nano, vim, or any editor)

## Tasks

### Task 1: Create Your First Script

**Objective:** Create a basic bash script with echo statements

**Instructions:**
1. Create a file called `first_deploy.sh` in this lab directory
2. Add five echo statements that simulate a deployment process:
   - "Deploy started..."
   - "Stopping old service..."
   - "Copying files..."
   - "Starting new service..."
   - "Deploy complete."
3. Save the file
4. Run the script with: `bash first_deploy.sh`

**Expected Output:**
All five lines should print to the terminal in order.

**Script Name:** `first_deploy.sh`

---

### Task 2: Add the Shebang Line

**Objective:** Understand and add a shebang to specify the interpreter

**Instructions:**
1. Open `first_deploy.sh` in your editor
2. Add `#!/bin/bash` as the very first line
3. Save the file
4. Try running the script with: `./first_deploy.sh`

**Expected Output:**
You should see a "Permission denied" error. This is expected and you'll fix it in the next task!

**Script Name:** `first_deploy.sh` (modify existing)

---

### Task 3: Understand File Permissions

**Objective:** Learn to check and understand file permissions

**Instructions:**
1. Run `ls -l first_deploy.sh` to check the file permissions
2. Note the permission string (e.g., `-rw-r--r--`)
3. Notice there's no `x` (execute) permission
4. Verify that `bash first_deploy.sh` still works (bash doesn't need execute permission)
5. Compare with the sample script: `ls -l src/sample_script.sh`

**Expected Output:**
- Your script shows permissions like `-rw-r--r--` (no x)
- The sample script shows permissions with `x` (e.g., `-rwxr-xr-x`)
- Running with `bash first_deploy.sh` works fine

**Script Name:** `first_deploy.sh` (inspection only)

---

### Task 4: Make Your Script Executable

**Objective:** Use chmod to add execute permissions

**Instructions:**
1. Run `chmod +x first_deploy.sh`
2. Check the permissions again with `ls -l first_deploy.sh`
3. Notice the `x` now appears in the permission string
4. Run the script with `./first_deploy.sh`

**Expected Output:**
- Permissions now show `x` flags (e.g., `-rwxr-xr-x`)
- Running `./first_deploy.sh` works and prints all five lines

**Script Name:** `first_deploy.sh` (modify permissions)

---

### Task 5: Compare Execution Methods

**Objective:** Understand the difference between `./script.sh` and `bash script.sh`

**Instructions:**
1. With execute permission, run: `./first_deploy.sh` (should work)
2. Run: `bash first_deploy.sh` (should also work)
3. Remove execute permission: `chmod -x first_deploy.sh`
4. Try `./first_deploy.sh` (should fail)
5. Try `bash first_deploy.sh` (should still work!)
6. Restore execute permission: `chmod +x first_deploy.sh`

**Expected Output:**
- Both methods work when the file has execute permission
- Only `bash script.sh` works without execute permission
- Understanding: `./script.sh` requires the shebang and execute permission; `bash script.sh` explicitly uses the bash interpreter

**Script Name:** `first_deploy.sh` (testing only)

---

## Completion

You've successfully learned:
- How to create bash scripts
- What a shebang line is and why it's important
- How to check and modify file permissions
- Two different ways to execute scripts
- When to use `./script.sh` vs `bash script.sh`
