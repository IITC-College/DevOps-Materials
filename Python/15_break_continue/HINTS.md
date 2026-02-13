# Hints – break and continue in for Loops

Use if you're stuck.

---

## Part 1 – break

**1.1** `for i in range(1, 11):` then if `i == 5`: print "Found 5", break. Else: print i.

**1.2** `for i in range(10):` then `n = int(input("Enter a number (0 to stop): "))`. If n == 0: print "Stopped", break. Else: print n.

**1.3** `total = 0`, `for i in range(100):` read number. If number == 0: break. Else: total += number. After loop: print "Sum: " + str(total).

**1.4** `n = int(input("How many? "))`. `for i in range(n):` read number. If number > 10: print "First > 10: " + str(number), break. After loop use a flag (e.g. found = False, set True when you break) to print "None > 10" only if you never broke. Or use else on the for: `for ...: ... break` then `else:` (for-else runs only if loop did not break).

---

## Part 2 – continue

**2.1** `for i in range(1, 11):` if `i % 2 != 0`: continue. Then print i (only runs for even).

**2.2** `for i in range(1, 11):` if `i % 3 == 0`: continue. Then print i.

**2.3** `total = 0`, `for i in range(5):` read number. If number < 0: print "Skipped", continue. total += number, print "Total so far: " + str(total). After loop: print "Final total: " + str(total).

---

## Part 3 – break and continue together

**3.1** `for i in range(5):` word = input("Word: "). If word == "quit": print "Bye", break. If word == "": print "Skipped", continue. Else: print "You said: " + word.

**3.2** `for i in range(5):` score = int(input("Score (0-100): ")). If score < 0 or score > 100: print "Invalid, try again", continue. Print "Valid: " + str(score), break.

**3.3** total = 0, for i in range(10): read number. If number < 0: print "Stopped (negative)", break. If number == 0: continue. total += number. After loop: print "Sum: " + str(total).

---

## Reminders

- **break** exits the loop immediately; no more iterations.
- **continue** skips the rest of the current iteration and goes to the next one.
- **for-else**: the `else` block after a `for` runs only if the loop did not hit `break`. You can use it for "not found" messages.

---

## Common errors

| Error | Check |
|-------|--------|
| Loop never breaks | Condition for break must be possible (e.g. user can type 0). |
| Wrong total | With continue, make sure you only add when you intend to; don't add then continue. |
| Indentation | break and continue must be inside the for body (same indent as the if). |
