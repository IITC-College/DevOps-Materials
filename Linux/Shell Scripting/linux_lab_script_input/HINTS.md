# Hints

## Task 1
- `read -p "prompt text" VARIABLE_NAME` combines prompt and read
- The variable name comes after the prompt string
- No `$` when declaring the variable with read
- Use `$VARIABLE` to access the value later

## Task 2
- `read -p` = prompt on same line, better UX
- plain `read` = no prompt, just waits (cursor on blank line)
- Always use `-p` for user-friendly scripts
- The `-p` flag stands for "prompt"

## Task 3
- You can use the same variable multiple times
- Each `$SERVICE` will be replaced with the user's input
- Variables persist for the entire script execution
- Good practice: Confirm what the user entered before taking action

## Task 4
- Empty input means the variable contains an empty string ""
- Bash doesn't prevent empty input by default
- When you echo an empty variable, you just get blank space
- This is a common source of bugs in scripts
- Try it: press Enter immediately when prompted

## Task 5
- Empty input scenarios in DevOps:
  - `rm -rf /$DIRECTORY` with empty DIRECTORY = disaster!
  - Deploying to empty environment name might default to production
  - Empty backup path could backup nothing or wrong location
- Real-world scripts MUST validate all user input
- Validation checks you'll learn: `[ -z "$VAR" ]` (is empty), `[ -n "$VAR" ]` (not empty)

## General Tips
- Always validate user input in production scripts
- Use descriptive prompts: "Enter service name (web/db/api): "
- Consider providing default values: `read -p "Environment [dev]: " ENV`
- Test scripts with empty input, spaces, special characters
- The `read` command returns non-zero exit code on EOF (Ctrl+D)
- For multiple inputs, use multiple read statements or read multiple variables at once: `read VAR1 VAR2`
- For sensitive input (passwords), use `read -s` to hide input

---

## Solutions

### Task 1 Solution

```bash
#!/bin/bash
read -p "Enter service name: " SERVICE
echo "Checking service: $SERVICE"
```

### Task 2 Solution

```bash
#!/bin/bash
# read_test.sh - without -p flag
read SERVICE
echo "Service: $SERVICE"
```

### Task 3 Solution

```bash
#!/bin/bash
read -p "Enter service name: " SERVICE
echo "Checking service: $SERVICE"
echo "Will check status of $SERVICE now."
```

### Task 4 & 5

These tasks are about testing and understanding, not writing new code. Use the Task 3 solution and test it with empty input (just press Enter when prompted).
