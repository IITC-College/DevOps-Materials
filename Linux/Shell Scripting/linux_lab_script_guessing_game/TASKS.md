# Shell Scripting Lab: Number Guessing Game

## Goal

Build a number guessing game in bash. The script picks a random number, the user guesses, and the script says "higher", "lower", or "correct". You'll use variables, `read`, conditionals, and a `while` loop.

## Prerequisites

- Script Basics, Variables, Input, Conditionals, and Loops labs (or equivalent knowledge)
- Linux system with bash
- A text editor

## Tasks

### Task 1: Pick a Random Number and One Guess

**Objective:** Generate a random number (1–10) and compare one user guess

**Instructions:**
1. Create a script called `guess_step1.sh`
2. Add the shebang
3. Pick a random number between 1 and 10:
   ```bash
   #!/bin/bash
   SECRET=$(( RANDOM % 10 + 1 ))
   echo "I'm thinking of a number between 1 and 10."
   read -p "Your guess: " GUESS
   ```
4. Compare GUESS to SECRET with conditionals and print "Too high!", "Too low!", or "Correct!"
5. Use arithmetic comparison: `(( GUESS > SECRET ))`, `(( GUESS < SECRET ))`, `(( GUESS == SECRET ))`
6. Run the script a few times (the number changes each run)

**Expected Output:**
```
I'm thinking of a number between 1 and 10.
Your guess: 5
Too low!
```
(or "Too high!" or "Correct!")

**Script Name:** `guess_step1.sh`

---

### Task 2: Loop Until Correct

**Objective:** Let the user keep guessing until they get it right

**Instructions:**
1. Create a script called `guess_step2.sh`
2. Set SECRET the same way: `SECRET=$(( RANDOM % 10 + 1 ))`
3. Use a `while` loop: repeat "read guess, compare, print message" until `GUESS` equals `SECRET`
4. When correct, print "Correct!" and exit the loop
5. Hint: use `while true; do ... done` and `break` when correct, or `while (( GUESS != SECRET )); do` and set GUESS before the loop (e.g. 0) so the loop runs at least once
6. Make it executable and play a full game

**Expected Output:**
```
I'm thinking of a number between 1 and 10.
Your guess: 3
Too low!
Your guess: 7
Too high!
Your guess: 5
Correct!
```

**Script Name:** `guess_step2.sh`

---

### Task 3: Count Attempts

**Objective:** Show how many guesses it took

**Instructions:**
1. Create a script called `guess_step3.sh` (or extend `guess_step2.sh`)
2. Add a variable `ATTEMPTS=0` before the loop
3. Inside the loop, after each guess, increment: `ATTEMPTS=$(( ATTEMPTS + 1 ))`
4. When the user is correct, print "Correct! You got it in N attempt(s)."
5. Run and verify the count

**Expected Output:**
```
Correct! You got it in 3 attempt(s).
```

**Script Name:** `guess_step3.sh`

---

### Task 4: Configurable Range (Optional)

**Objective:** Use a range from a file or from user input

**Instructions:**
1. Create `src/config.txt` with one line: `1 100` (min and max)
2. Create or extend your script to read the range (e.g. from the file or prompt for max)
3. Generate SECRET in that range: e.g. if MIN=1 and MAX=100, use `SECRET=$(( RANDOM % (MAX - MIN + 1) + MIN ))`
4. Print "I'm thinking of a number between MIN and MAX." using those values
5. Test with 1–100 and with a smaller range (e.g. 1–5)

**Expected Output:**
```
I'm thinking of a number between 1 and 100.
Your guess: 50
...
```

**Script Name:** `guess_game.sh` (or keep existing name)

---

## Completion

You've built a number guessing game that:
- Uses `$RANDOM` and arithmetic for a range
- Reads input with `read -p`
- Uses conditionals for higher/lower/correct
- Uses a `while` loop until the guess is correct
- Counts attempts
- Optionally uses a configurable range from a file or input

Same patterns apply to any "repeat until condition" or "guess and check" script.
