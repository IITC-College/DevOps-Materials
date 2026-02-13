# Hints – List as Argument to a Function

Use if you're stuck.

---

## Part 1 – Pass a list and read it

**1.1** `def print_length(items):` then `print(len(items))`. Call with `print_length([10, 20, 30])` and `print_length(["a", "b"])`.

**1.2** `def sum_list(numbers):` then `total = 0`, `for n in numbers: total += n`, `return total`. Call `total = sum_list([1, 2, 3, 4, 5])`, `print(total)`, and `print(sum_list([10, 20]))`.

**1.3** `def print_each(items):` then `for item in items: print(item)`. Call with a list of strings and a list of numbers.

---

## Part 2 – Return a new list

**2.1** `def double_list(numbers):` then `result = []`, `for n in numbers: result.append(n * 2)`, `return result`. Do not do `numbers[i] = ...`; build a new list. After the call, print the returned list and the original list.

**2.2** `def first_and_last(items):` then `if len(items) == 0: return []` else `return [items[0], items[-1]]`. Call with a non-empty list and with `[]`.

---

## Part 3 – Mutating the list

**3.1** `def add_item(items, value):` then `items.append(value)`. Create `my_list = [1, 2, 3]`, call `add_item(my_list, 4)`, then `print(my_list)`. The same list is modified.

**3.2** `def set_at_index(items, index, value):` then `items[index] = value`. Call with a list, index 2, and a new value; print the list after.

**3.3** `def clear_list(items):` then use `while len(items) > 0: items.pop()` or `items.clear()`. Do **not** write `items = []` — that would only change the local name. Call with a list, then print it; it should be empty.

---

## Part 4 – List and other parameters

**4.1** `def add_if_missing(items, value):` then `if value not in items: items.append(value)`. Call with a list and a new value, then with a value already in the list; print the list after each call.

**4.2** `def count_value(items, target):` then `count = 0`, `for x in items: if x == target: count += 1`, `return count`. Call with a list and a target value; print the return value.

---

## Reminders

- **Passing a list:** The parameter gets a **reference** to the same list. Reading (len, indexing, loop) does not change the caller’s list.
- **Mutating:** `items.append(x)`, `items[i] = x`, `items.clear()`, `items.pop()` change the list **in place**. The caller sees those changes.
- **Reassigning the parameter:** `items = []` or `items = [1, 2, 3]` inside the function only changes the local name; it does **not** change the list the caller passed. To change the caller’s list, mutate it (e.g. clear then append, or use .clear()).
- **Returning a new list:** Build a new list inside the function and return it; the original list is unchanged.

---

## Common errors

| Error | Check |
|-------|--------|
| IndexError when list is empty | Check `len(items) > 0` or `len(items) >= 1` before using `items[0]` or `items[-1]`. |
| Caller’s list unchanged when you wanted to clear | You probably did `items = []` inside the function. Use `items.clear()` or pop in a loop instead. |
| Modifying list while iterating | If you remove elements in a loop, iterate over a copy (e.g. `for x in items[:]:`) or use a while loop with pop. |
