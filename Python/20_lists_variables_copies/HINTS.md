# Hints – Variables vs Lists, Cutting (Slicing), and Real Copies [:]
Use if you're stuck. Do list labs 18 and 19 first.

---

## Part 1 – Variables vs lists

**1.1** a = 10, b = a, a = 20. print(a), print(b). With numbers, b got the value 10; changing a doesn't change b.

**1.2** a = [1, 2, 3], b = a, a[0] = 99. print(a), print(b). Both show [99, 2, 3] because a and b refer to the same list.

**1.3** original = [10, 20, 30], other = original. other.append(40), other[0] = 0. print(original), print(other). Same list, so both show [0, 20, 30, 40].

---

## Part 2 – Cutting lists (slicing)

**2.1** nums = [10, 20, 30, 40, 50, 60], middle = nums[2:5]. print(middle). Slice [2:5] is indices 2, 3, 4 (stop 5 is excluded).

**2.2** data = [1, 2, 3, 4, 5, 6, 7]. print(data[:3]), print(data[-3:]). [:3] = first 3; [-3:] = last 3.

**2.3** items = ["a", "b", "c", "d", "e"], tail = items[2:]. print(tail). [2:] = from index 2 to end.

**2.4** nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]. evens = nums[::2], print(evens). odds = nums[1::2], print(odds). [::2] = every 2nd; [1::2] = from index 1, every 2nd.

**2.5** a = [1, 2, 3, 4, 5], b = a[1:4]. a[2] = 99. print(a), print(b). A slice creates a new list; changing a doesn't change b.

---

## Part 3 – Real copy with [:]
**3.1** a = [1, 2, 3], b = a[:]. a[0] = 99. print(a), print(b). a[:] creates a new list with the same elements. b stays [1, 2, 3].

**3.2** original = [5, 10, 15], copy = original[:]. copy.append(20), copy[0] = 0. print(original), print(copy). Original unchanged; copy is [0, 10, 15, 20].

**3.3** nums = [30, 10, 20], sorted_list = nums[:], sorted_list.sort(). print(nums), print(sorted_list). Original stays [30, 10, 20]; sorted_list is [10, 20, 30].

---

## Part 4 – Copy with list()
**4.1** a = [1, 2, 3], b = list(a). a[0] = 99. print(a), print(b). list(a) also creates a new list.

**4.2** data = [7, 8, 9], copy1 = data[:], copy2 = list(data). data[1] = 0. print(data), print(copy1), print(copy2). Both copy methods work.

---

## Part 5 – When to use a copy
**5.1** items = [1, 2, 3, 4, 5], reversed_copy = items[:], reversed_copy.reverse(). print("Original:", items), print("Reversed copy:", reversed_copy).

**5.2** data = [10, 20, 30], backup = data (no copy). data.append(40), data[0] = 0. print("data:", data), print("backup:", backup). Both change because they're the same list.

**5.3** data = [10, 20, 30], backup = data[:]. data.append(40), data[0] = 0. print("data:", data), print("backup:", backup). backup stays [10, 20, 30].

---

## Reminders
- **b = a** (list): b and a point to the same list. Changing a[i] or appending to a also affects b.
- **Cutting (slicing):** list[start:stop] = elements from start to stop-1. list[:n] = first n. list[n:] = from n to end. list[-n:] = last n. list[::step] = every step-th element. A slice always creates a **new** list.
- **b = a[:]** or **b = list(a)**: full copy. Use when you need to modify one list without changing the other.

---

## Common mistakes
| Mistake | Fix |
|--------|-----|
| "I copied the list but both change" | You used b = a. Use b = a[:] or b = list(a). |
| Using = and expecting a backup | For a backup, use backup = original[:] before changing original. |
