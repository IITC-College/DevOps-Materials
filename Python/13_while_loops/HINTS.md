# Hints – while Loops

Use if you’re stuck.

---

**1** `count = 0`, then `while count < 5:` (colon, indent), `print(count)`, `count += 1`. Make sure you increment so the loop eventually stops.

**2** `n = int(input("Enter n: "))`, `i = 1`, then `while i <= n:` print `i`, `i += 1`.

**3** `n = int(input("Enter n: "))`, `total = 0`, `i = 1`. While `i <= n`: `total += i`, `i += 1`. After loop: `print(total)`.

**4** `x = 5`, then `while x > 0:` print `x`, `x -= 1`. After loop: `print("Done")`.

**5** Read once before the loop. `while number < 1 or number > 10:` ask again and store in `number`. When condition is false, print the number. Or use `while True`, read, if 1 <= n <= 10 break, else keep looping.

**6** `value = 1`, then `while value < 100:` print `value`, `value *= 2`. After loop you can print final value (128).

**7** `total = 0`. Loop: read number. If number == 0, break. Else total += number. After loop print total. Use `while True` and `break` when 0.

**8** `n = int(input("Enter n: "))`, `i = 0`. While `i <= n`: if `i % 2 == 0` print `i`. Then `i += 1`. Or start at 2 and do `i += 2` each time (no if needed).

**9** `n = int(input("Start from: "))`, `x = n`. While `x >= 0:` print `x`, `x -= 1`. Then print "Done".

**10** `word = ""` (or any value that’s not "quit"). While `word != "quit":` (or use `while True` and break when "quit"): read word, if word != "quit" print "You said: " + word. After loop print "Bye". Note: if you check at the start, you need to read once before the loop so `word` has a value, or use `while True` and read at the beginning of the loop, then break on "quit" before printing.

---

## Reminders

- **Infinite loop:** Ensure the condition eventually becomes false (e.g. increment counter) or use `break`.
- **Indentation:** Everything inside the `while` block must be indented.
- **break** exits the loop immediately; use it for “stop when 0” or “stop when quit”.

---

## Common errors

| Error | Check |
|-------|--------|
| Loop never ends | Condition never false; did you update the variable (e.g. `i += 1`)? |
| IndentationError | Body of while must be indented. |
| NameError | Variable used in condition must be set before the loop (e.g. read input or assign). |
