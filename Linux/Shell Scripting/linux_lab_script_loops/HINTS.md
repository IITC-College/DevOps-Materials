# Hints

## Task 1
- `for` syntax: `for VAR in list; do commands; done`
- The loop variable (`DIR`) is assigned each value in turn
- List items are space-separated
- Loop body is between `do` and `done`
- You can iterate over anything: numbers, strings, file paths

## Task 2
- Combine loop with conditional: `if [ -d ]` inside `for`
- Build full path with: `"$BASE/$DIR"` or `"${BASE}/${DIR}"`
- Check before you use: always validate paths exist
- Indentation helps readability (2 or 4 spaces)

## Task 3
- `$(command)` runs command and returns output
- `cat file.txt` outputs file contents
- Each line becomes a loop item (with default word splitting)
- **Warning:** This method breaks on paths with spaces
- Better approach for files with spaces: `while read LINE; do ... done < file.txt`
- For simple lists (no spaces), `$(cat file)` is fine

## Task 4
- `while [ condition ]; do commands; done`
- Condition is tested before each iteration
- `-le` means "less than or equal"
- Other operators: `-lt` (<), `-gt` (>), `-ge` (>=), `-eq` (==), `-ne` (!=)
- Arithmetic: `$((expression))`
- Common: `COUNT=$((COUNT + 1))` increments by 1
- `$(($COUNT + 1))` can also be written as `$((COUNT++)` (but post-increment)

## Task 5
- `break` exits the loop immediately
- Common in retry patterns: try until success, then break
- `continue` skips rest of current iteration (not used here)
- Retry pattern = while + counter + conditional break
- Real-world use: wait for service health check, with max retries
- Good practice: always have a maximum retry count

## Task 6
- Nested loops: outer loop controls, inner loop repeats for each outer iteration
- Indent nested loops for clarity
- Be careful with variable names: use different names for inner/outer
- Check if loop exhausted: compare counter after loop
- Pattern: try something multiple times per item in a list
- Real-world: check multiple servers, retrying health check for each

## General Tips

### For Loop Variations
```bash
# Over list
for ITEM in apple orange banana; do echo $ITEM; done

# Over numbers (brace expansion)
for NUM in {1..5}; do echo $NUM; done

# Over files
for FILE in *.txt; do echo $FILE; done

# Over command output
for USER in $(cat users.txt); do echo $USER; done

# C-style for (bash specific)
for ((i=0; i<5; i++)); do echo $i; done
```

### While Loop Variations
```bash
# With counter
COUNT=1
while [ $COUNT -le 5 ]; do
    echo $COUNT
    COUNT=$((COUNT + 1))
done

# Read from file (handles spaces)
while read LINE; do
    echo "$LINE"
done < file.txt

# Infinite loop (Ctrl+C to stop)
while true; do
    echo "Running..."
    sleep 1
done

# Until loop (opposite of while)
COUNT=1
until [ $COUNT -gt 5 ]; do
    echo $COUNT
    COUNT=$((COUNT + 1))
done
```

### Arithmetic Operations
```bash
# Addition
RESULT=$((5 + 3))

# Subtraction
RESULT=$((10 - 3))

# Multiplication
RESULT=$((4 * 5))

# Division
RESULT=$((20 / 4))

# Modulo
RESULT=$((10 % 3))

# Increment
COUNT=$((COUNT + 1))
# or
((COUNT++))

# Decrement
COUNT=$((COUNT - 1))
# or
((COUNT--))
```

### Loop Control
- `break`: exit loop immediately
- `break 2`: exit two levels of nested loops
- `continue`: skip to next iteration
- Exit codes: check `$?` after commands in loops

### Common Patterns

**Wait for file to appear:**
```bash
while [ ! -f "file.txt" ]; do
    echo "Waiting for file..."
    sleep 1
done
```

**Process all files in directory:**
```bash
for FILE in /path/to/dir/*; do
    if [ -f "$FILE" ]; then
        echo "Processing $FILE"
    fi
done
```

**Countdown:**
```bash
COUNT=10
while [ $COUNT -gt 0 ]; do
    echo $COUNT
    COUNT=$((COUNT - 1))
    sleep 1
done
echo "Blast off!"
```

### Performance Tips
- Don't parse `ls`: use globbing (`for f in *.txt`)
- For large files, use `while read` instead of `$(cat)`
- Add `sleep` in retry loops to avoid hammering
- Set reasonable max attempts (don't loop forever)

### Debugging
- Add `echo "DEBUG: VAR=$VAR"` in loops
- Use `set -x` to trace execution
- Test with small iterations first (e.g., 3 instead of 100)
- Check loop variable after loop to see final value
