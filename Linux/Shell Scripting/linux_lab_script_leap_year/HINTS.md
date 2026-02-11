# Hints

## Task 1 - Divisibility by 4
- Arithmetic in bash: `(( expression ))` — no `$` inside for variables: `(( YEAR % 4 == 0 ))`
- Modulo: `%` gives the remainder. If `YEAR % 4 == 0`, the year is divisible by 4
- Use `YEAR=2024` then change to `YEAR=2023` to test both branches

## Task 2 - 100 and 400 Rules
- Check 400 first: if divisible by 400, it's always a leap year
- Then 100: if divisible by 100 (and not 400), not a leap year
- Then 4: if divisible by 4 (and not 100), leap year
- Else: not a leap year
- Order matters: 400 before 100 before 4

## Task 3 - User Input
- `read -p "Enter a year: " YEAR` — YEAR will be a string; bash arithmetic `(( ))` will interpret it
- Simplify output to one line: "YEAR is a leap year." or "YEAR is not a leap year."
- No need to explain the rule in the output for this task

## Task 4 - Validate Input
- Regex in bash: `[[ "$YEAR" =~ ^[0-9]+$ ]]` — matches one or more digits only
- If the match fails, print error and `exit 1`
- Optional: reject 0 or negative by checking `(( YEAR > 0 ))` after confirming it's numeric

## General Tips
- **Arithmetic**: `(( a % b ))` is the remainder of a divided by b
- **Order of checks**: 400 → 100 → 4 → else
- **Quoting**: Inside `(( ))` you can use YEAR unquoted; in `[[ ]]` use `"$YEAR"`

---

## Solutions

### Task 1 Solution

```bash
#!/bin/bash
YEAR=2024
if (( YEAR % 4 == 0 )); then
    echo "$YEAR is divisible by 4 (candidate for leap year)"
else
    echo "$YEAR is not divisible by 4 (not a leap year)"
fi
```

### Task 2 Solution

```bash
#!/bin/bash
YEAR=1900
if (( YEAR % 400 == 0 )); then
    echo "$YEAR is a leap year (divisible by 400)"
elif (( YEAR % 100 == 0 )); then
    echo "$YEAR is not a leap year (divisible by 100 but not 400)"
elif (( YEAR % 4 == 0 )); then
    echo "$YEAR is a leap year (divisible by 4, not by 100)"
else
    echo "$YEAR is not a leap year (not divisible by 4)"
fi
```

### Task 3 Solution

```bash
#!/bin/bash
read -p "Enter a year: " YEAR

if (( YEAR % 400 == 0 )); then
    echo "$YEAR is a leap year."
elif (( YEAR % 100 == 0 )); then
    echo "$YEAR is not a leap year."
elif (( YEAR % 4 == 0 )); then
    echo "$YEAR is a leap year."
else
    echo "$YEAR is not a leap year."
fi
```

### Task 4 Solution (Optional)

```bash
#!/bin/bash
read -p "Enter a year: " YEAR

# Validate input is a positive number
if [[ ! "$YEAR" =~ ^[0-9]+$ ]]; then
    echo "Invalid year. Please enter a positive number."
    exit 1
fi

if (( YEAR % 400 == 0 )); then
    echo "$YEAR is a leap year."
elif (( YEAR % 100 == 0 )); then
    echo "$YEAR is not a leap year."
elif (( YEAR % 4 == 0 )); then
    echo "$YEAR is a leap year."
else
    echo "$YEAR is not a leap year."
fi
```
