# Hints – Logical Operators (and, or, not)

Use if you're stuck.

---

## Part 1 – and

**1.1** `print(True and True)`, `print(True and False)`, `print(False and False)`. and is True only when both sides are True.

**1.2** `print(5 > 3 and 10 > 7)`, `print(5 > 3 and 2 > 10)`.

**1.3** `age = 25`, `has_ticket = True`, `print(age >= 18 and has_ticket)`. Then `has_ticket = False`, `print(age >= 18 and has_ticket)`.

**1.4** `n = int(input("Enter a number: "))`, `print(n >= 1 and n <= 10)`.

---

## Part 2 – or

**2.1** `print(True or False)`, `print(False or False)`, `print(True or True)`. or is True when at least one side is True.

**2.2** `print(3 > 5 or 10 > 7)`, `print(3 > 5 or 2 > 10)`.

**2.3** `is_weekend = False`, `is_holiday = True`, `print(is_weekend or is_holiday)`. Then set both False and print again.

**2.4** `age = int(input("Age: "))`, `amount = float(input("Amount: "))`. If `age >= 65 or amount >= 100`: print "Discount applies", else "No discount".

---

## Part 3 – not

**3.1** `print(not True)`, `print(not False)`.

**3.2** `print(not (5 > 10))`, `print(not (3 < 5))`. 5 > 10 is False, so not False is True.

**3.3** `empty = True`, `print(not empty)`. Then `empty = False`, `print(not empty)`.

---

## Part 4 – Combining

**4.1** `print((True and False) or True)` → False or True → True. `print(False and (True or False))` → False and True → False.

**4.2** `a = True`, `b = False`. `not (a and b)` → not (False) → True. `(not a) and b` → False and False → False.

**4.3** Read age and password. if age >= 18 and password == "secret": "Access granted". elif age < 18 and password == "secret": "Too young". else: "Access denied".

**4.4** `n = int(input("Enter n: "))`. if `not (n >= 1 and n <= 10)`: print "Out of range". else: "In range". Equivalent: `if n < 1 or n > 10`.

---

## Precedence

- **not** has highest precedence, then **and**, then **or**. Use parentheses when in doubt: `(a and b) or c`.

---

## Common errors

| Error | Check |
|-------|--------|
| Using &, \| instead of and, or | In Python use the words: `and`, `or`, `not` (not &, \|, !). |
| Confusing = and == | In conditions use == for equality. `and`/`or`/`not` work on boolean values. |
