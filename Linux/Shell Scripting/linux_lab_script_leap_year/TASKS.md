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

**Instructions:**
1. Create a script called `leap_step1.sh`
2. Add the shebang and set a variable: `YEAR=2024`
3. Use an arithmetic conditional to check if the year is divisible by 4:
   ```bash
   #!/bin/bash
   YEAR=2024
   if (( YEAR % 4 == 0 )); then
       echo "$YEAR is divisible by 4 (candidate for leap year)"
   else
       echo "$YEAR is not divisible by 4 (not a leap year)"
   fi
   ```
4. Run the script
5. Change YEAR to 2023 and run again

**Expected Output:**
- With 2024: "2024 is divisible by 4 (candidate for leap year)"
- With 2023: "2023 is not divisible by 4 (not a leap year)"

**Script Name:** `leap_step1.sh`

---

### Task 2: Add the 100-Year Exception

**Objective:** Years divisible by 100 are not leap years (unless divisible by 400)

**Instructions:**
1. Create a script called `leap_step2.sh`
2. Set `YEAR=1900`
3. Implement logic: if divisible by 100 and not by 400, it's not a leap year:
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
4. Test with YEAR=1900, YEAR=2000, YEAR=2024, YEAR=2023

**Expected Output:**
- 1900 → not a leap year (divisible by 100 but not 400)
- 2000 → leap year (divisible by 400)
- 2024 → leap year (divisible by 4, not by 100)
- 2023 → not a leap year (not divisible by 4)

**Script Name:** `leap_step2.sh`

---

### Task 3: Read Year from User Input

**Objective:** Prompt for the year instead of hardcoding it

**Instructions:**
1. Create a script called `leap_year.sh`
2. Prompt the user for a year:
   ```bash
   #!/bin/bash
   read -p "Enter a year: " YEAR
   ```
3. Use the same leap-year logic from Task 2 (if/elif/else with % 400, % 100, % 4)
4. Output only one line: either "YEAR is a leap year." or "YEAR is not a leap year."
5. Make it executable and test with 2000, 1900, 2024

**Expected Output:**
```
Enter a year: 2024
2024 is a leap year.
```

```
Enter a year: 1900
1900 is not a leap year.
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
