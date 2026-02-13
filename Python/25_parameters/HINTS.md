# Hints – Parameters in Python

Use if you're stuck.

---

**1** `def describe(name, age):` then e.g. `print("Name: " + name + ", Age: " + str(age))`. Call: `describe("Ali", 25)`.

**2** `def subtract(a, b): return a - b`. Then `print(subtract(10, 3))` and `print(subtract(3, 10))`. First arg → a, second → b.

**3** `def greet(name, greeting="Hello"):` then `print(greeting + ", " + name + "!")`. Call: `greet("Bob")` — second argument not needed.

**4** Same `def greet(name, greeting="Hello"):`. Call `greet("Bob")` and `greet("Bob", "Hi")`. Second call overrides the default.

**5** `def info(name, age, city):` then print the three. Call: `info(name="Alice", age=30, city="Tel Aviv")` and `info(city="London", name="Bob", age=22)`.

**6** `def format_msg(from_name, to_name, separator=" -> "): return from_name + separator + to_name`. Call: `print(format_msg("Alice", "Bob"))` and `print(format_msg("Alice", "Bob", separator=" | "))`. Keyword can come last.

**7** `def multiply(a, b=2): return a * b`. Call: `print(multiply(5))` and `print(multiply(5, 3))`. Required param `a` first, default param `b` second.

**8** `def greet(name, greeting="Hello", punctuation="!"):` then print using all three. Call: `greet("Sam")`, `greet("Sam", "Hi")`, `greet("Sam", "Hey", "?")`. Each call fills from left to right.

**9** `def connect(host, port=80, secure=False):` then print host, port, secure. Call: `connect("example.com", secure=True)`. Using `secure=True` as keyword lets you skip `port` and keep its default.

**10** `def log(message, level="INFO"):` then `print("[" + level + "] " + message)`. Call: `log("Server started")`, `log("Error occurred", "ERROR")`, `log("Debug trace", level="DEBUG")`.

---

## Reminders

- **Positional:** Arguments are matched to parameters in order. First argument → first parameter, etc.
- **Keyword:** `name=value` in the call. Order doesn't matter; you can use keywords to skip parameters that have defaults.
- **Defaults:** In the definition, write `param=default_value`. Parameters with defaults must come **after** parameters without defaults (e.g. `def f(a, b=1)` not `def f(b=1, a)`).
- **Mixing:** In a call, put all positional arguments first, then keyword arguments.

---

## Common errors

| Error | Check |
|-------|--------|
| SyntaxError: non-default argument follows default argument | You wrote e.g. `def f(a=1, b)`. Put required params first: `def f(b, a=1)`. |
| TypeError: missing required positional argument | You didn't pass enough arguments. Check how many parameters have no default. |
| TypeError: got multiple values for argument | You passed a value both by position and by keyword for the same parameter. |
