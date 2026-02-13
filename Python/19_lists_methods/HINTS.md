# Hints – List Methods (append, insert, swap, sort, reverse)

Use if you're stuck. Do 18_lists first.

---

## Part 1 – append and insert

**1.1** nums = [10, 20, 30], nums.append(40), print(nums). nums.insert(1, 15), print(nums). insert(i, x) inserts x at index i; elements at i and after shift right.

**1.2** words = ["banana", "cherry"], words.insert(0, "apple"), print(words). words.insert(len(words), "date"), print(words). insert(0, x) puts x at start; insert(len(list), x) is like append.

**1.3** vals = [1, 2, 4, 5], vals.insert(2, 3), print(vals).

---

## Part 2 – Swapping

**2.1** items = [10, 20, 30, 40, 50]. temp = items[0], items[0] = items[-1], items[-1] = temp. print(items).

**2.2** data = ["a", "b", "c", "d", "e"]. temp = data[1], data[1] = data[3], data[3] = temp. print(data).

**2.3** nums = [5, 10, 15, 20, 25]. i = int(input("Enter first index: ")), j = int(input("Enter second index: ")). if 0 <= i < len(nums) and 0 <= j < len(nums): temp = nums[i], nums[i] = nums[j], nums[j] = temp, print(nums). else: print("Invalid index").

---

## Part 3 – sort and reverse

**3.1** nums = [30, 10, 50, 20, 40], nums.sort(), print(nums). letters = ["banana", "apple", "date", "cherry"], letters.sort(), print(letters). sort() changes the list in place (ascending).

**3.2** vals = [1, 2, 3, 4, 5], vals.reverse(), print(vals). reverse() reverses the list in place.

**3.3** nums = [30, 10, 50, 20, 40], nums.sort(), nums.reverse(), print(nums). That gives descending order.

**3.4** Read n, build list of n numbers (append in loop). nums.sort(), print(nums).

---

## Part 4 – Combined

**4.1** data = [2, 4, 6], data.insert(0, 1), print(data). temp = data[0], data[0] = data[3], data[3] = temp, print(data). data.sort(), print(data).

---

## Reminders

- **insert(i, x)** inserts x at index i. Valid i is 0 to len(list) (insert at end is like append).
- **Swap:** use a temporary variable so you don't overwrite one value before copying it.
- **sort()** and **reverse()** modify the list in place; they don't return a new list (they return None).

---

## Common errors

| Error | Check |
|-------|--------|
| IndexError when swapping | Both indices must be 0 <= i < len(list). |
| sort() / reverse() return None | Don't write result = nums.sort(); use nums.sort() then use nums. |
