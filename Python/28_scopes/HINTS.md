# Hints – Scopes in Python

Use if you're stuck.

---

## Part 1 – Global and local

**1.1** At top level: `name = "Global"`. Define `def show_name():` and in the body `print(name)`. Call `show_name()` then `print(name)`. No assignment to `name` inside the function, so it refers to the global.

**1.2** Top level: `x = 10`, `print("before:", x)`. Define `def set_x():` then `x = 99` and `print(x)`. Call `set_x()`, then `print("after:", x)`. The assignment inside the function creates a local `x`; the global stays 10.

**1.3** Top level: `value = 100`. Define `def double(value): return value * 2`. Call `print(double(5))` then `print(value)`. The parameter `value` is local; the global `value` is unchanged.

---

## Part 2 – global keyword

**2.1** Top level: `counter = 0`, `print(counter)`. Define `def increment():` then first line inside: `global counter`, then `counter = counter + 1`. Call `increment()` three times, then `print(counter)`. You must declare `global counter` so the assignment updates the global.

**2.2** Top level: `total = 10`. Define `def add_to_total(amount):` then `global total`, then `total = total + amount` (or `total += amount`) and `print(total)`. Call `add_to_total(5)` and `add_to_total(3)`, then `print(total)`.

---

## Part 3 – Each function its own locals

**3.1** `def foo(): x = 1; print(x)`. `def bar(): x = 2; print(x)`. Call `foo()`, `bar()`, `foo()`. Each `x` is local to its function.

**3.2** `def set_secret(): secret = 42; print(secret)`. `def get_secret(): print(secret)`. Call `set_secret()` then `get_secret()`. The second call has no `secret` in its scope — NameError. Don’t define a global `secret`; the point is that one function’s local is not visible in another.

---

## Part 4 – Loop and block scope

**4.1** At top level: `for i in range(3): print(i)`. Then (same indentation as `for`): `print("after loop:", i)`. In Python, `i` still exists after the loop and is 2.

**4.2** Top level: `msg = "global"`, `print(msg)`. Define `def mix():` then `print(msg)` (reads global), then `msg = "local"`, then `print(msg)` (local). Call `mix()`, then `print(msg)` at top level. First print in function sees global; after assignment, `msg` is local; after the call, top-level `msg` is still "global".

---

## Reminders

- **Global scope:** Names defined at the top level (no indentation) of the file. They can be **read** inside functions.
- **Local scope:** Names assigned (or used as parameters) inside a function. They exist only while that function runs and are not visible outside or in other functions.
- **Shadowing:** If you assign to a name inside a function, that name is local there and “shadows” the global of the same name. The global is unchanged.
- **global:** To **assign** to a global variable from inside a function, you must write `global name` in that function first. Then assignments to `name` affect the global.
- **Parameters** are local to the function. A parameter with the same name as a global is a separate local variable.
- **No block scope:** In Python, `for` and `if` do not create a new scope; variables defined in a loop or if-block are still in the same scope (e.g. function or global).

---

## Common errors

| Error | Check |
|-------|--------|
| UnboundLocalError: local variable 'x' referenced before assignment | You assigned to `x` later in the function, so Python treats `x` as local everywhere in that function. If you meant the global, add `global x` at the start and ensure you don’t read it before assigning, or assign to a different name. |
| NameError: name 'x' is not defined | The name isn’t in the current scope (not local, not global). Check spelling, or that the variable is defined in an outer scope / global before use. |
| Expecting global to change but it doesn’t | You didn’t use `global name` before assigning to `name` inside the function, so the assignment created a local variable. |
