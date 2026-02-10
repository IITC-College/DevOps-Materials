# Hints

## Task 1
- Start simple: just read and echo
- Use `read -p` for inline prompt
- Test with various inputs to see what happens
- This is the foundation - get it working first

## Task 2
- `if/elif/else` for multiple options
- String comparison: `[ "$VAR" = "value" ]`
- Each branch has its own echo statements
- `else` catches anything that doesn't match
- Think about what happens with typos (e.g., "deplyo")

## Task 3
- Empty check should be FIRST (before other checks)
- `[ -z "$VAR" ]` tests if variable is empty
- Exit with error code 1 for invalid input
- Add "Done." at the very end (after fi)
- "Done." should NOT show when there's an error

## Task 4
- Variables at the TOP of the script (after shebang)
- Use UPPERCASE for configuration variables (convention)
- Reference with `$VAR_NAME` or `${VAR_NAME}`
- Paths are relative to where you run the script
- Makes script easy to adapt for different apps

## Task 5
- Nested if: deploy branch now contains another if
- Confirmation must be exactly "yes" (not "y" or "YES")
- Anything other than "yes" = cancelled
- Empty confirmation (just Enter) = cancelled (safe default)
- Only deploy if user explicitly confirms

## Task 6
- Review the entire flow
- Test every branch
- Make sure error cases work (empty, invalid)
- Add descriptive comments
- Verify exit codes are appropriate
- Think about user experience (clear messages)

## General Tips

### Script Organization
```bash
#!/bin/bash
# Script description/purpose

# Configuration section
VAR1="value"
VAR2="value"

# Main logic
echo "Starting..."
# ... do work ...
echo "Done."
```

### Input Validation Pattern
```bash
# Read input
read -p "Enter something: " VAR

# Validate (empty, valid values, etc.)
if [ -z "$VAR" ]; then
    echo "Error: cannot be empty"
    exit 1
fi

# Process valid input
# ... rest of script
```

### Confirmation Pattern
```bash
read -p "Are you sure? (yes/no): " CONFIRM
if [ "$CONFIRM" != "yes" ]; then
    echo "Cancelled."
    exit 0
fi
# Proceed with dangerous operation...
```

### String Comparison
```bash
# Exact match
if [ "$ACTION" = "deploy" ]; then

# Not equal
if [ "$ACTION" != "deploy" ]; then

# Multiple options
if [ "$ACTION" = "deploy" ] || [ "$ACTION" = "build" ]; then

# Case-insensitive (convert to lowercase first)
ACTION_LOWER=$(echo "$ACTION" | tr '[:upper:]' '[:lower:]')
if [ "$ACTION_LOWER" = "deploy" ]; then
```

### Exit Codes
- `exit 0` = success (or cancelled operation)
- `exit 1` = error (invalid input, missing file, etc.)
- No explicit exit = use exit code of last command

### Variables vs Hardcoded
```bash
# Hardcoded (bad for maintenance)
echo "Deploying webapp..."
echo "Checking webapp..."
echo "Backing up logs from src/data/ops_env/logs..."

# Variables (easy to change)
APP_NAME="webapp"
LOG_DIR="src/data/ops_env/logs"
echo "Deploying $APP_NAME..."
echo "Checking $APP_NAME..."
echo "Backing up logs from $LOG_DIR..."
```

### Nested Conditionals
```bash
# Outer conditional
if [ "$ACTION" = "deploy" ]; then
    # Inner conditional (confirmation)
    if [ "$CONFIRM" = "yes" ]; then
        # Actually deploy
    else
        # Cancelled
    fi
elif [ "$ACTION" = "check" ]; then
    # Check logic
fi
```

### Testing Strategy
1. Test happy path (all valid actions)
2. Test edge cases (empty input)
3. Test error cases (invalid actions)
4. Test confirmations (yes and no)
5. Verify exit codes with `echo $?`

### User Experience
- Clear prompts (show options)
- Immediate feedback (echo what's happening)
- Success indicators (✓ or "OK")
- Error messages that explain the problem
- Consistency in messaging

### Debugging
```bash
# Add at top to trace execution
set -x

# Debug variables
echo "DEBUG: ACTION=$ACTION"
echo "DEBUG: CONFIRM=$CONFIRM"

# Check branching
echo "Entering deploy branch..."
```

### Common Mistakes
- Forgetting to close `fi`
- Not quoting variables: `[ $VAR = "x" ]` should be `[ "$VAR" = "x" ]`
- Wrong comparison: `[ "$VAR" == "x" ]` works but `=` is more portable
- Empty check after other checks (should be first)
- Exit code 0 for errors (should be 1)
- Typos in action names ("deplpy" won't match "deploy")

### Enhancement Ideas
- Add logging: `echo "[$(date)] Deploy started" >> ops.log`
- Add timeout: only allow deploy during business hours
- Add rollback: save previous version before deploy
- Add dry-run: `./ops_helper.sh --dry-run deploy`
- Add verbose mode: more detailed output
- Add quiet mode: minimal output
- Add colors: green for success, red for errors

### Production Considerations
What would a real ops helper need?
- Actual deployment logic (not just echo)
- Error handling (what if deploy fails?)
- Logging to file
- Service health checks (ping, curl, etc.)
- Backup to remote storage
- Notification (email, Slack)
- Access control (only certain users can deploy)
- Audit trail (who did what when)
