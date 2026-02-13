# Hints – Diving into the return Statement

Use if you're stuck.

---

## Part 1 – return vs print

**1.1** `def get_message(): return "Hello"`. Then e.g. `msg = get_message()`, `print(msg)`, and `print(get_message())`. The function only returns; the caller prints.

**1.2** `def print_sum(a, b): print(a + b)` (no return). `def return_sum(a, b): return a + b`. Call `print_sum(3, 5)` then `result = return_sum(3, 5)` and `print(result)`.

---

## Part 2 – None and multiple returns

**2.1** `def maybe_greet(do_it):` then `if do_it: return "Hi!"` and `return None`. Call `print(maybe_greet(True))` and `print(maybe_greet(False))`.

**2.2** `def sign(n):` then `if n < 0: return -1`, `elif n > 0: return 1`, `else: return 0`. One return runs and exits the function.

**2.3** `def letter_grade(score):` then `if score >= 90: return "A"`, `elif score >= 80: return "B"`, `elif score >= 70: return "C"`, `else: return "F"`. Call with 85, 72, 91.

---

## Part 3 – Using return value

**3.1** `def is_even(n): return n % 2 == 0`. Then `if is_even(4): print("even")` else `print("odd")`. Same for 7.

**3.2** `def double(x): return x * 2` and `def add_one(x): return x + 1`. Then `print(add_one(double(5)))` and `print(double(add_one(5)))`.

---

## Part 4 – Loop and multiple values

**4.1** `def first_positive(numbers):` then `for n in numbers:` and `if n > 0: return n`. After the loop: `return None`. Call with a list that has a positive and a list that doesn't.

**4.2** Use conditionals to set which is min and which is max, then `return smaller, larger` (e.g. `if a <= b: return a, b` else `return b, a`). Call with `low, high = min_max(10, 3)` and print both. For same values, e.g. `return a, b` when a == b is fine.

---

## Part 5 – Guard clause

**5.1** `def divide_safe(a, b):` then first line: `if b == 0: return None`. Next: `return a / b`. Call `print(divide_safe(10, 2))` and `print(divide_safe(10, 0))`.

---

## Reminders

- **return** sends a value back to the caller and **exits the function** at that line. Code after a return in the same branch does not run.
- **return** with no value (or `return None`) is the same as reaching the end of the function without returning — the result is `None`.
- **Multiple returns:** Only one return runs per call. Often used in if/elif/else or for guard clauses.
- **return a, b** returns a tuple `(a, b)`. You can unpack with `x, y = func()`.
- **Guard clause:** Check the bad case first, return early; then do the normal case.

---

## Common errors

| Error | Check |
|-------|--------|
| Function “returns” but value is None | You might be printing inside the function instead of returning, or you have a path that doesn’t return (e.g. missing else). |
| Unpacking error (too many / not enough values) | Your function must return the same number of values you unpack (e.g. two values for `a, b = func()`). |
| Division by zero | Guard: if divisor is 0, return None (or a sentinel) before dividing. |
