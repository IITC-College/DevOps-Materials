# Hints – Functions Basics

Use if you're stuck.

---

## Part 1 – Defining and calling

**1.1** `def say_hello():` then indent and `print("Hello!")`. After the function block, call with `say_hello()`.

**1.2** `def greet(name):` then indent and `print("Hello, " + name + "!")`. Call with `greet("Alice")` and `greet("Bob")`.

**1.3** `def add_and_print(a, b):` then indent and `print(a + b)`. No `return` needed if you only print. Call with `add_and_print(3, 5)` and `add_and_print(10, -2)`.

---

## Part 2 – Order matters

**2.1** Put `greet("World")` at the **top** of the file. Then define `def greet(name):` and print a greeting. Running the script runs the call first, so `greet` is not defined yet → NameError.

**2.2** Put the `def greet(name):` block **first**, then `greet("World")`. Definition before use.

---

## Part 3 – Return

**3.1** `def add(a, b):` then indent and `return a + b`. After the function: `print(add(3, 5))` and `print(add(10, -1))`.

**3.2** `def double(x):` then `return x * 2`. Use `result = double(7)`, `print(result)`, then e.g. `result = double(10)` and `print(result)`.

**3.3** `def say_hi():` then only `print("Hi")` (no return). Then `value = say_hi()` and `print(value)`. The function returns `None` by default.

**3.4** `def describe(n):` then `if n < 0: return "negative"` (indented under def). Next line (same indent as if): `return "zero or positive"`. Call with `print(describe(-5))`, etc.

**3.5** `def square(x): return x * x`. Then `print(square(4) + square(3))` and `print(square(square(2)))`.

---

## Reminders

- **Definition order:** In Python, a function must be **defined before** it is called. The interpreter executes the file from top to bottom; there is no hoisting like in JavaScript.
- **def** and **colon:** `def name(params):` — the colon is required and the body must be indented.
- **return** sends a value back to the caller. If there is no return (or just `return`), the function returns `None`.
- **Early return:** You can have multiple `return` statements; the first one that runs exits the function.

---

## Common errors

| Error | Check |
|-------|--------|
| NameError: name 'greet' is not defined | You are calling the function before it is defined. Move the `def` block above the call. |
| IndentationError | Function body must be indented (4 spaces). Same for `if` inside the function. |
| return outside function | You wrote `return` at the top level. `return` must be inside a `def` block. |
| Forgetting to call the function | Defining a function does not run it. You must write `function_name()` to call it. |
