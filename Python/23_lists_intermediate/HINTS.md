# Hints – Lists Intermediate (negative index, del, non-existing, combined)

Use if you're stuck. Do all list basics first: 18_lists, 19_lists_methods, 20_lists_variables_copies, 21_in_notin_combined, 22_lists_2d_3d.

---

## Part 1 – Negative index, del, non-existing

**1.1** data = ["a", "b", "c", "d", "e"]. print(data[-1]), print(data[-2]), print(data[-3]), print(data[-len(data)]). -1 is last, -2 is second to last.

**1.2** vals = [10, 20, 30, 40, 50], del vals[2], print(vals), del vals[-1], print(vals). del removes the element at that index.

**1.3** items = ["apple", "banana", "cherry"], idx = int(input("Enter index: ")). if idx >= 0 and idx < len(items): print(items[idx]). else: print("Invalid index").

**1.4** allowed = ["yes", "y", "ok"], answer = input("Enter response: "). if answer not in allowed: print("Not allowed"). else: print("Allowed").

**1.5** nums = [5, 10, 15, 20], idx = int(input("Enter index to remove: ")). if 0 <= idx < len(nums): del nums[idx], print(nums). else: print("Invalid index"), print(nums).

---

## Part 2 – Harder combined

**2.1** words = ["apple", "banana", "cherry", "banana", "date"], target = input("Enter word: "). found = False. for i in range(len(words)): if words[i] == target: print("Found at index " + str(i)), found = True, break. if not found: print("Not found").

**2.2** Read n, build list of n numbers. pos = []. for n in numbers: if n > 0: pos.append(n). print("Original: " + str(numbers)), print("Positives only: " + str(pos)).

**2.3** my_list = []. while True: print menu, choice = int(input("Choice: ")). if choice == 1: val = input("Value: ") (or int), my_list.append(val). elif choice == 2: print(my_list). elif choice == 3: idx = int(input("Index: ")); if 0 <= idx < len(my_list): del my_list[idx], print("Removed"); else: print("Invalid index"). elif choice == 4: print("Bye"), break.

**2.4** nums = [1, 2, 3, 2, 4, 2, 5], val = int(input("Enter value to remove: ")). new_list = []. for n in nums: if n != val: new_list.append(n). print("Original: " + str(nums)), print("After removing " + str(val) + ": " + str(new_list)).

**2.5** Build list from input (n numbers). if len(nums) == 0: print("Empty list"). else: total = 0, for n in nums: total += n. min_val = nums[0], max_val = nums[0], for n in nums: if n < min_val: min_val = n; if n > max_val: max_val = n. count_pos = 0, for n in nums: if n > 0: count_pos += 1. print "Sum: " + str(total) + ", Min: " + str(min_val) + ", Max: " + str(max_val) + ", Positive count: " + str(count_pos).

**2.6** tasks = []. while True: print "1=Add 2=List 3=Remove 4=Quit", choice = int(input("Choice: ")). if choice == 1: task = input("Task: "), tasks.append(task). elif choice == 2: for i in range(len(tasks)): print(str(i+1) + ". " + tasks[i]). elif choice == 3: num = int(input("Which number? ")); if 1 <= num <= len(tasks): del tasks[num - 1], print("Removed"); else: print("Invalid"). elif choice == 4: print("Bye"), break.

---

## Reminders

- **Negative index:** -1 is last, -2 is second to last. Valid range is -len(list) <= i < len(list).
- **del list[i]** removes the element at index i. Check 0 <= i < len(list) before del.
- **Non-existing:** Check index with 0 <= index < len(list). For value, use "if x not in list".

---

## Common errors

| Error | Check |
|-------|--------|
| IndexError | Index must be in 0 to len-1 (or -len to -1). Check before access or del. |
| Modifying list while looping | If you delete by index in a forward for loop, indices shift; prefer building a new list or check index range. |
