# Hints – while Loops

Use if you're stuck.

---

**1** `count = 0`, then `while count < 5:` (colon, indent), `print(count)`, `count += 1`. Make sure you increment so the loop eventually stops.

**2** `n = int(input("Enter n: "))`, `i = 1`, then `while i <= n:` print `i`, `i += 1`.

**3** `n = int(input("Enter n: "))`, `total = 0`, `i = 1`. While `i <= n`: `total += i`, `i += 1`. After loop: `print(total)`.

**4** `x = 5`, then `while x > 0:` print `x`, `x -= 1`. After loop: `print("Done")`.

**5** Read once before the loop. `while number < 1 or number > 10:` ask again and store in `number`. When condition is false, print the number. Or use `while True`, read, if 1 <= n <= 10 break, else keep looping.

**6** `total = 0.0`. `while True`: name = input("Item name (or 'done' to finish):"). If name == "done": break. Else: price = float(input("Price:")), total += price, print "Added " + name + ": " + str(price) + ". Running total: " + str(total). After loop: print "Total: " + str(total).

**7** `while True`: print menu (1=Add 2=Subtract 3=Multiply 4=Quit), choice = int(input("Choice:")). If choice == 4: print "Bye", break. Elif choice == 1: read two numbers, print sum. Elif 2: read two, print difference. Elif 3: read two, print product. Else: print "Invalid option".

**8** secret = "python", attempts = 0. While attempts < 3: pwd = input("Password:"). If pwd == secret: print "Welcome", break. Else: print "Wrong. Attempts left:", (2 - attempts), then attempts += 1. After loop: if attempts == 3: print "Locked".

**9** total = 0, count = 0. while True: n = int(input("Enter a number (0 to finish):")). If n == 0: break. total += n, count += 1. After loop: print "Count:", count, "Sum:", total. If count > 0: print "Average:", total / count. Else: print "No numbers entered".

**10** name = input("Student name:"), n = int(input("How many scores?")). total = 0, i = 0. While i < n: score = float(input("Score " + str(i+1) + ":")), total += score, i += 1. average = total / n. print "Student: " + name + ", Average: " + str(round(average, 1)).

---

## Reminders

- **Infinite loop:** Ensure the condition eventually becomes false (e.g. increment counter) or use `break`.
- **Indentation:** Everything inside the `while` block must be indented.
- **break** exits the loop immediately; use it for "stop when 0" or "stop when quit".

---

## Common errors

| Error | Check |
|-------|--------|
| Loop never ends | Condition never false; did you update the variable (e.g. `i += 1`)? |
| IndentationError | Body of while must be indented. |
| NameError | Variable used in condition must be set before the loop (e.g. read input or assign). |
