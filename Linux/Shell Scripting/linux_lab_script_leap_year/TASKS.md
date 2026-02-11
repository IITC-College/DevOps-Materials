# Shell Scripting Lab: Leap Year

## Goal

Build a script that determines whether a given year is a leap year. You'll use variables, user input, arithmetic, and conditionals to implement the leap-year rules.

## Prerequisites

- Script Basics, Variables, Input, and Conditionals labs (or equivalent knowledge)
- Linux system with bash
- A text editor

## Leap Year Rules (reminder)

- Divisible by 4 → leap year (unless also divisible by 100)
- Divisible by 100 → not a leap year (unless also divisible by 400)
- Divisible by 400 → leap year

Examples: 2000 is leap, 1900 is not, 2024 is leap, 2023 is not.

## Tasks

### Task 1: Check Divisibility by 4

**Objective:** Use arithmetic to check if a year is divisible by 4

**Requirements:**
- Create `leap_step1.sh` with shebang
- Set YEAR variable to 2024
- Use arithmetic conditional to check if divisible by 4
- If divisible: print "[year] is divisible by 4 (candidate for leap year)"
- If not: print "[year] is not divisible by 4 (not a leap year)"
- Test with 2024, then change to 2023 and test again

**Technical Hints:**
- Arithmetic conditional: `(( expression ))`
- Modulo operator: `%` (remainder after division)
- Check if remainder is 0: `(( YEAR % 4 == 0 ))`
- Use if/else with arithmetic conditional

**Expected Output:**
- 2024: "2024 is divisible by 4 (candidate for leap year)"
- 2023: "2023 is not divisible by 4 (not a leap year)"

**Script Name:** `leap_step1.sh`

---

### Task 2: Add the 100-Year Exception

**Objective:** Years divisible by 100 are not leap years (unless divisible by 400)

**Requirements:**
- Create `leap_step2.sh` with shebang
- Set YEAR to 1900
- Implement complete leap year logic with if/elif/else:
  1. If divisible by 400: is a leap year
  2. Else if divisible by 100: not a leap year
  3. Else if divisible by 4: is a leap year
  4. Else: not a leap year
- Print appropriate message for each case
- Test with: 1900, 2000, 2024, 2023

**Technical Hints:**
- Check most specific rule first (400), then less specific (100, 4)
- Use multiple elif branches
- Order matters! Check 400 before 100

**Expected Output:**
- 1900 → not a leap year (divisible by 100 but not 400)
- 2000 → leap year (divisible by 400)
- 2024 → leap year (divisible by 4, not by 100)
- 2023 → not a leap year (not divisible by 4)

**Script Name:** `leap_step2.sh`

---

### Task 3: Read Year from User Input

**Objective:** Prompt for the year instead of hardcoding it

**Requirements:**
- Create `leap_year.sh` with shebang
- Prompt user: "Enter a year: "
- Store input in YEAR variable
- Apply same leap year logic from Task 2
- Output simplified messages:
  - Leap year: "[year] is a leap year."
  - Not leap year: "[year] is not a leap year."
- Test with: 2000, 1900, 2024, 2023

**Technical Hints:**
- Use `read -p "prompt" VARIABLE`
- Reuse the if/elif/else structure from Task 2
- Simplify output messages (no need to explain why)

**Expected Output:**
```
Enter a year: 2024
2024 is a leap year.
```

**Script Name:** `leap_year.sh`

---

### Task 4: Validate Input Is a Number (Optional)

**Objective:** Reject non-numeric input and show a clear message

**Instructions:**
1. Open `leap_year.sh`
2. After reading YEAR, add a check that it's a positive integer (e.g. using a pattern or `[[ "$YEAR" =~ ^[0-9]+$ ]]`)
3. If invalid, print "Invalid year. Please enter a positive number." and exit with code 1
4. Test with valid year, then with "abc" or "-5"

**Expected Output:**
- Valid year → same as before
- "abc" → "Invalid year. Please enter a positive number." and exit 1

**Script Name:** `leap_year.sh` (extended)

---

## Completion

You've built a leap-year checker that:
- Uses arithmetic conditionals `(( ))` and modulo `%`
- Implements the full rule set (4, 100, 400)
- Reads input with `read -p`
- Optionally validates input

Use the same patterns for any "yes/no" decision based on numbers (e.g. even/odd, divisible checks).
