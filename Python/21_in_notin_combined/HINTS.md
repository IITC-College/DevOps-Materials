# Hints – in and not in, Combined

Use if you're stuck. Uses ideas from lists, conditions, loops, and input labs.

---

## Part 1 – Basics

**1.1** allowed = ["yes", "y", "ok"]. print("yes" in allowed), print("no" in allowed).

**1.2** banned = ["spam", "bad", "x"], word = input("Enter word: "). if word not in banned: print("Allowed"). else: print("Blocked").

**1.3** numbers = [10, 20, 30, 40, 50], n = int(input("Enter a number: ")). if n in numbers: print("In the list"). else: print("Not in the list").

**1.4** text = "hello world". print("world" in text), print("xyz" not in text). in works on strings (substring).

---

## Part 2 – Conditions and input

**2.1** options = ["1", "2", "3"], choice = input("Choose 1, 2, or 3: "). if choice in options: print("Valid: " + choice). else: print("Invalid choice").

**2.2** users = ["ali", "bo", "cat"], username = input("Username: "). if username.lower() in users: print("Welcome, " + username + "!"). else: print("Unknown user").

**2.3** blocked = ["admin", "root", "test"], username = input("Username: "). if username not in blocked: print("OK"). else: print("Blocked").

---

## Part 3 – Loops

**3.1** all_items = [1, 2, 3, 4, 5], seen = [2, 4], new_items = []. for item in all_items: if item not in seen: new_items.append(item). print(new_items).

**3.2** quit_words = ["quit", "exit", "q"]. for i in range(5): word = input("Word: "). if word in quit_words: print("Bye"), break. else: print("You said: " + word).

**3.3** answers = [1, 2, 3, 2, 1], correct = [1, 3], count = 0. for a in answers: if a in correct: count += 1. print("Score: " + str(count)).

---

## Part 4 – Combined

**4.1** tags = [], n = int(input("How many tags to add? ")). for i in range(n): tag = input("Tag " + str(i+1) + ": "). if tag not in tags: tags.append(tag), print("Added"). else: print("Already exists"). print(tags).

**4.2** valid = ["a", "b", "c", "q"]. while True: choice = input("Options: a, b, c, q (quit): "). if choice in valid: if choice == "q": print("Bye"), break. else: print("You chose " + choice). else: print("Invalid").

**4.3** digits = "0123456789", password = input("Password: "). found = False. for char in password: if char in digits: found = True, break. if found: print("Password has a digit"). else: print("Password must contain a digit").

**4.4** valid_yes = ["yes", "y"], valid_no = ["no", "n"]. while True: answer = input("Continue? (yes/no): ").lower(). if answer in valid_yes: print("Continuing"), break. elif answer in valid_no: print("Stopping"), break. else: print("Please enter yes or no").

**4.5** list1 = [1, 2, 3, 4, 5], list2 = [3, 4, 5, 6, 7], common = []. for x in list1: if x in list2: common.append(x). print("Common: " + str(common)).

---

## Reminders

- **x in my_list** is True if x is an element of my_list (one of the items). For strings, **sub in text** is True if sub is a substring.
- **x not in my_list** is the opposite of x in my_list.
- Use **in** for validation (is choice in valid options?), filtering (keep only if not in seen), and membership (is user in list?).

---

## Common mistakes

| Mistake | Check |
|--------|--------|
| Comparing types | 3 in [1, 2, 3] works. "3" in [1, 2, 3] is False (string vs int). Use int(input()) if list has numbers. |
| List of strings | valid = ["1", "2"] then if input() in valid works because input() returns a string. |
