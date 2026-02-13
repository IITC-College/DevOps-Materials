# Hints – Lists in Python

Use if you're stuck.

---

## Part 1 – Creating and accessing

**1.1** nums = [10, 20, 30, 40, 50], print(nums), print(nums[0]), print(nums[-1]). Index -1 is the last element.

**1.2** my_list = [1, 2.5, "hello", True], print(my_list), print(my_list[2]).

**1.3** items = ["apple", "banana", "cherry", "date"], print(len(items)), print(items[0]), print(items[-1]), print(items[2]).

**1.4** my_list = [], my_list.append(5), my_list.append(10), my_list.append(15), print(my_list), print(len(my_list)).

---

## Part 2 – Modifying

**2.1** vals = [1, 2, 3, 4, 5], vals[2] = 100, print(vals), vals[-1] = 99, print(vals).

**2.2** my_list = [], for i in range(1, 6): my_list.append(i * 10), print(my_list).

**2.3** numbers = [10, 20, 30, 40, 50], total = 0, for n in numbers: total += n, print(total), average = total / len(numbers), print(average).

---

## Part 3 – Looping

**3.1** fruits = ["apple", "banana", "cherry"]. for fruit in fruits: print(fruit). Then for i in range(len(fruits)): print(str(i) + ": " + fruits[i]).

**3.2** nums = [1, 2, 3, 4, 5], for i in range(len(nums)): nums[i] = nums[i] * 2, print(nums).

**3.3** allowed = ["yes", "y", "ok"], answer = input("Enter response: "). if answer in allowed: print "Allowed" else: print "Not allowed".

---

## Part 4 – Lists and input

**4.1** n = int(input("How many numbers? ")), numbers = [], for i in range(n): num = int(input("Number " + str(i+1) + ": ")), numbers.append(num). print(numbers), print(len(numbers)).

**4.2** Build list as in 4.1. total = 0, for n in numbers: total += n. max_val = numbers[0], for n in numbers: if n > max_val: max_val = n. print "Sum: " + str(total) + ", Max: " + str(max_val).

**4.3** n = int(input("How many names? ")), names = [], for i in range(n): name = input("Name " + str(i+1) + ": "), names.append(name). for name in names: print "Hello, " + name + "!".

---

## Part 5 – More

**5.1** Build list from input (n and n numbers). if len(my_list) > 0: print "First: " + str(my_list[0]) + ", Last: " + str(my_list[-1]). else: print "Empty list".

**5.2** numbers = [3, -1, 5, -2, 0, 4], count = 0, for n in numbers: if n > 0: count += 1. print "Positive count: " + str(count).

---

## Reminders

- **Indexing:** 0 is first, -1 is last. List indices must be integers.
- **append(x)** adds one element at the end. my_list.append(x).
- **len(list)** returns the number of elements.
- **in** checks membership: if x in my_list.

---

## Common errors

| Error | Check |
|-------|--------|
| IndexError: list index out of range | Index must be < len(list). Check empty list before [0] or [-1]. |
| TypeError: 'int' not iterable | You wrote for x in len(list); use for x in list or for i in range(len(list)). |
