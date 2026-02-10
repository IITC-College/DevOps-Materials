# Hints

## Task 1
- Exit codes: 0-255, where 0 = success, anything else = error
- `exit 0` is explicit success
- `exit 1` is conventional for general errors
- If script ends without explicit exit, uses exit code of last command
- `$?` holds exit code of most recent foreground command
- Must check `$?` immediately - it's overwritten by next command

## Task 2
- Pattern: validate → exit with appropriate code
- Exit codes communicate to calling process or CI/CD system
- Scripts should exit 0 only if truly successful
- Default parameter: `"${1:-default}"` uses $1 or "default" if not provided
- Good practice: always validate inputs before processing

## Task 3
- `&&` = "and then" (only if previous succeeded)
- `||` = "or else" (only if previous failed)
- `command1 && command2` → command2 runs only if command1 exits 0
- `command1 || command2` → command2 runs only if command1 exits non-zero
- Chain: `cmd1 && cmd2 && cmd3` → stops at first failure
- Alternate: `cmd1 || cmd2 || cmd3` → stops at first success

## Task 4
- Fail-fast = exit immediately on error, don't continue
- Good for: deployment scripts, validation pipelines, CI/CD
- Check each prerequisite before proceeding
- Exit 1 as soon as something fails
- Prevents damage from running with bad state
- Real-world: CI/CD systems watch exit codes to show pass/fail

## Task 5
- `$?` captures exit code of last command
- Store in variable immediately: `CODE=$?`
- Pass through with: `exit $CODE`
- Wrapper pattern useful for: logging, timing, retries
- Preserve original exit code so callers see actual result

## General Tips

### Exit Code Conventions
- **0**: Success, no errors
- **1**: General errors
- **2**: Misuse of command (bad arguments)
- **126**: Command found but not executable
- **127**: Command not found
- **128+N**: Fatal signal N (e.g., 130 = Ctrl+C)
- **130**: Script terminated by Ctrl+C (SIGINT)
- **137**: Script terminated by kill (SIGKILL)

### Checking Exit Codes
```bash
# Immediate check
./script.sh
echo $?

# Store for later
./script.sh
RESULT=$?
echo "Script exited with: $RESULT"

# Inline check
if ./script.sh; then
    echo "Success"
else
    echo "Failed"
fi

# With explicit test
./script.sh
if [ $? -eq 0 ]; then
    echo "Success"
fi
```

### Chaining Commands
```bash
# Run cmd2 only if cmd1 succeeds
cmd1 && cmd2

# Run cmd2 only if cmd1 fails
cmd1 || cmd2

# Try cmd1, fallback to cmd2 if fails
cmd1 || cmd2

# Run all, stop on first failure
cmd1 && cmd2 && cmd3 && cmd4

# Multiple commands on success
cmd1 && { cmd2; cmd3; cmd4; }

# With subshell
cmd1 && (cmd2; cmd3)
```

### Fail-Fast Pattern
```bash
#!/bin/bash

# Method 1: Explicit checks
check_step1 || exit 1
check_step2 || exit 1
check_step3 || exit 1

# Method 2: Exit on any error
set -e  # Exit immediately if any command fails
check_step1
check_step2
check_step3

# Method 3: Manual checks
if ! check_step1; then
    exit 1
fi
if ! check_step2; then
    exit 1
fi
```

### Exit on Error Modes
```bash
#!/bin/bash

# Exit on error
set -e

# Exit on undefined variable
set -u

# Exit on pipe failure (not just last command)
set -o pipefail

# Combine all
set -euo pipefail

# Disable temporarily
set +e
might_fail_command
set -e
```

### Function Exit Codes
```bash
# Functions can return 0-255
check_something() {
    if [ condition ]; then
        return 0
    else
        return 1
    fi
}

# Check function result
if check_something; then
    echo "Check passed"
fi

# Or capture exit code
check_something
RESULT=$?
```

### CI/CD Integration
```bash
#!/bin/bash
# CI/CD pipeline script

# Run tests
npm test || exit 1

# Run linter
npm run lint || exit 1

# Build
npm run build || exit 1

# Deploy
./deploy.sh || exit 1

echo "Pipeline complete!"
exit 0
```

### Best Practices
1. **Always exit with 0 on success** (explicitly)
2. **Exit with non-zero on any error**
3. **Use consistent exit codes** across scripts
4. **Check prerequisites before proceeding** (fail-fast)
5. **Document special exit codes** if you use them
6. **Test both success and failure paths**
7. **Use `set -e` for strict error handling**
8. **Clean up before exit** (temp files, locks)

### Common Patterns

**Exit with message:**
```bash
die() {
    echo "ERROR: $*" >&2
    exit 1
}

[ -f config ] || die "Config file not found"
```

**Cleanup on exit:**
```bash
cleanup() {
    rm -f /tmp/tempfile
}
trap cleanup EXIT

# Script runs...
# cleanup() called automatically on exit
```

**Multiple validations:**
```bash
validate() {
    [ -f "$CONFIG" ] || { echo "Config missing"; return 1; }
    [ -d "$DATA_DIR" ] || { echo "Data dir missing"; return 1; }
    [ -n "$API_KEY" ] || { echo "API key missing"; return 1; }
    return 0
}

validate || exit 1
```

### Debugging Exit Codes
- Add `echo "Exit code: $?"` after commands
- Use `set -x` to trace execution
- Check each step individually
- Verify `$?` immediately (don't let other commands overwrite it)
- Test failure cases intentionally
