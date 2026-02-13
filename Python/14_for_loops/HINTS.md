# Hints – for Loops and range()

Use if you're stuck.

---

## Part 1 – Basics

**1.1** `for i in range(5):` then indent and `print(i)`. range(5) gives 0,1,2,3,4.

**1.2** `for i in range(1, 6):` then `print(i)`. range(1, 6) gives 1 up to 5 (stop is exclusive).

**1.3** `for i in range(0, 10, 2):` then `print(i)`. Third argument is the step.

**1.4** `for i in range(5, 0, -1):` then `print(i)`. After loop: `print("Go!")`. Negative step goes backward.

**1.5** `n = int(input("Enter n: "))` then `for i in range(1, n + 1):` and `print(i)`. Use n+1 because range stop is exclusive.

**1.6** `n = int(input("Enter n: "))`, `total = 0`, then `for i in range(1, n + 1): total += i`. After loop: `print(total)`.

---

## Part 2 – More for and range

**2.1** `n = int(input("How many? "))` then `for _ in range(n):` and `print("Hello")`. The variable `_` is conventional when you don't use the value.

**2.2** `n = int(input("Enter n: "))` then `for i in range(0, n + 1, 2):` and `print(i)`.

**2.3** `total = 0`, `for i in range(2, 11, 2):` then `print(i)` and `total += i`. After loop: `print(total)`.

---

## Part 3 – Real tasks

**3.1** `num = int(input("Enter a number: "))` then `for i in range(1, 11):` and e.g. `print(str(num) + " x " + str(i) + " = " + str(num * i))`.

**3.2** `n = int(input("How many scores? "))`, `total = 0`. `for i in range(n):` prompt "Score " + str(i+1) + ":", read float, add to total. After: `average = total / n`, `print("Average: " + str(round(average, 1)))`.

**3.3** `n = int(input("Length: "))`, `char = input("Character: ")`. `for i in range(n): print(char, end="")` then `print()` to start a new line.

**3.4** `n = int(input("How many names? "))`. `for i in range(n):` then `name = input("Name " + str(i+1) + ": ")` and `print("Hello, " + name)`.

**3.5** `n = int(input("How many numbers? "))`, `total = 0`. `for i in range(n):` read number, add to total. After: `print("Sum: " + str(total))`.

---

## range() reminder

- **range(stop)** → 0, 1, …, stop-1
- **range(start, stop)** → start, start+1, …, stop-1 (stop is exclusive)
- **range(start, stop, step)** → start, start+step, … (stops before reaching stop). Use step=-1 for countdown.

---

## Common errors

| Error | Check |
|-------|--------|
| Off-by-one | range(1, 5) gives 1,2,3,4 not 5. Use range(1, n+1) to include n. |
| IndentationError | Body of for must be indented. |
| NameError | Variable in range (e.g. n) must be defined first (e.g. from input()). |
