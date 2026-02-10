# Hints

## Task 1
- Function syntax: `function_name() { commands; }`
- Or: `function function_name { commands; }`
- Functions must be defined before they're called
- Call function by name: `function_name` (no parentheses needed)
- Functions run in current shell (can access script variables)

## Task 2
- `$1` = first parameter passed to function
- `$2` = second parameter, `$3` = third, etc.
- `$@` = all parameters as separate words
- `$#` = number of parameters
- Always quote parameters: `"$1"` not `$1`
- Parameters are positional: order matters

## Task 3
- Functions eliminate copy-paste code
- One function, many calls with different parameters
- If you need to change logic, only edit the function once
- Think: "What varies?" → that becomes a parameter
- What's repeated? → that stays in the function body

## Task 4
- Functions can return values via `echo`
- Capture with: `RESULT=$(function_name)`
- Command substitution `$(...)` inside functions works too
- `date '+FORMAT'` lets you format timestamps
- Common formats: `%Y-%m-%d`, `%H:%M:%S`, `%Y-%m-%d %H:%M:%S`

## Task 5
- Loops + functions = powerful automation
- Loop variable passed as function parameter: `function_name "$VAR"`
- The function doesn't know about the loop - it just receives values
- Clean separation: loop handles iteration, function handles logic
- Easy to extend: add more items to loop, function stays same

## Task 6
- Multiple functions working together
- Each function has single responsibility
- Main script reads like a story: log → deploy → log
- `sleep` simulates work (remove in real scripts or replace with actual checks)
- Professional scripts use functions for clarity
- Think about what each function should do before coding

## General Tips

### Function Basics
```bash
# Simple function
say_hello() {
    echo "Hello!"
}

# Function with parameter
greet() {
    echo "Hello, $1!"
}
greet "Alice"  # Output: Hello, Alice!

# Multiple parameters
add() {
    echo $(($1 + $2))
}
add 5 3  # Output: 8

# Capture return value
RESULT=$(add 5 3)
echo "Result: $RESULT"
```

### Local Variables
```bash
# Without local (variable visible outside function)
set_name() {
    NAME="Bob"
}

# With local (variable only inside function)
set_name() {
    local NAME="Bob"
    echo $NAME
}
```

### Return vs Echo
```bash
# Return: exit status (0-255)
check_file() {
    if [ -f "$1" ]; then
        return 0  # Success
    else
        return 1  # Failure
    fi
}

# Echo: output text (capture with $(...))
get_status() {
    if [ -f "$1" ]; then
        echo "exists"
    else
        echo "missing"
    fi
}

# Usage
if check_file "test.txt"; then
    echo "File found!"
fi

STATUS=$(get_status "test.txt")
echo "Status: $STATUS"
```

### Function Parameters
```bash
show_params() {
    echo "First: $1"
    echo "Second: $2"
    echo "All: $@"
    echo "Count: $#"
}

show_params apple banana cherry
# Output:
# First: apple
# Second: banana
# All: apple banana cherry
# Count: 3
```

### Best Practices
1. **Define functions at the top** of your script
2. **Use descriptive names**: `deploy_service` not `ds`
3. **One function, one purpose** (single responsibility)
4. **Quote parameters** to handle spaces: `"$1"` not `$1`
5. **Use local variables** when possible
6. **Return early** on errors
7. **Add comments** for complex functions

### Common Patterns

**Validation function:**
```bash
validate_env() {
    if [ -z "$1" ]; then
        echo "Error: Environment required"
        return 1
    fi
    if [ "$1" != "prod" ] && [ "$1" != "staging" ]; then
        echo "Error: Invalid environment"
        return 1
    fi
    return 0
}
```

**Retry function:**
```bash
retry_command() {
    local MAX_ATTEMPTS=3
    local ATTEMPT=1
    
    while [ $ATTEMPT -le $MAX_ATTEMPTS ]; do
        if "$@"; then  # Run the command passed as parameters
            return 0
        fi
        echo "Attempt $ATTEMPT failed, retrying..."
        ATTEMPT=$((ATTEMPT + 1))
        sleep 2
    done
    
    return 1
}

# Usage: retry_command curl https://api.example.com
```

**Error handling:**
```bash
die() {
    echo "ERROR: $1" >&2
    exit 1
}

# Usage
[ -f "config.txt" ] || die "Config file not found"
```

### Debugging Functions
- Add `echo "DEBUG: $1"` at function start
- Use `set -x` before function call to trace
- Check `$?` after function returns
- Test functions with different inputs
- Call functions with explicit values before using in loops

### When to Use Functions
✓ Code is repeated 2+ times  
✓ Block of code has clear purpose  
✓ Logic might change independently  
✓ Want to test part of script  
✓ Script is getting long (100+ lines)  

### Function Limitations
- Can't return strings directly (use echo + capture)
- Return codes limited to 0-255
- Parameters accessed positionally, not by name
- No built-in parameter validation (do it manually)
