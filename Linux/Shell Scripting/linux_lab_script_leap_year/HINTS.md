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
