# Hints

## Task 1 - One Guess
- `RANDOM` is a bash variable that gives a random number 0–32767
- `RANDOM % 10` gives 0–9; `RANDOM % 10 + 1` gives 1–10
- Store in variable: `SECRET=$(( RANDOM % 10 + 1 ))`
- Compare with arithmetic: `(( GUESS > SECRET ))`, `(( GUESS < SECRET ))`, `(( GUESS == SECRET ))`
- Use if/elif/else to print "Too high!", "Too low!", or "Correct!"

## Task 2 - Loop Until Correct
- Option A: `while true; do ... if (( GUESS == SECRET )); then echo "Correct!"; break; fi; done`
- Option B: `GUESS=0; while (( GUESS != SECRET )); do read -p "Your guess: " GUESS; ... done`
- Make sure you read the guess inside the loop each time
- When correct, print the message and exit the loop (break or let condition fail)

## Task 3 - Count Attempts
- Before the loop: `ATTEMPTS=0`
- Inside the loop, after reading GUESS: `ATTEMPTS=$(( ATTEMPTS + 1 ))`
- When correct: `echo "Correct! You got it in $ATTEMPTS attempt(s)."`

## Task 4 - Configurable Range
- For min and max: `SECRET=$(( RANDOM % (MAX - MIN + 1) + MIN ))` gives a number in [MIN, MAX]
- Reading from file: e.g. `read MIN MAX < src/config.txt`
- Or prompt: `read -p "Max number (1 to N): " MAX` and use MIN=1
- Use the same comparison logic; only SECRET and the prompt message change

## General Tips
- **$RANDOM**: 0–32767; use modulo and offset for your range
- **Arithmetic**: `(( ))` for comparisons and math; no $ inside for variables
- **Loop**: Always read a new guess inside the loop so the user can try again
- **Break**: `break` exits the innermost loop
