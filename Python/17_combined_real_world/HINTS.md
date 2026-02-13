# Hints – Combined Real-World

Use if you're stuck. Try to use what you know from previous labs.

---

**1 – Grade report**  
name = input("Student name: "), n = int(input("How many scores? ")). total = 0, for i in range(n): score = float(input("Score " + str(i+1) + ": ")), total += score. average = total / n. Then if average >= 90: grade = "A", elif average >= 80: grade = "B", etc. print("Student: " + name + ", Average: " + str(round(average,1)) + ", Grade: " + grade).

**2 – Menu calculator**  
while True: print menu, choice = int(input("Choice: ")). If choice == 4: print "Bye", break. Elif choice == 1: a = float(input("First: ")), b = float(input("Second: ")), print(a + b). Elif 2: same with a - b. Elif 3: same with a * b. Else: print "Invalid option".

**3 – Login**  
secret_user = "admin", secret_pass = "secret". logged_in = False. for i in range(3): user = input("Username: "), pwd = input("Password: "). If user == secret_user and pwd == secret_pass: print "Welcome, " + user + "!", logged_in = True, break. Else: print "Wrong. Attempts left:", 2 - i. After loop: if not logged_in: print "Locked."

**4 – Expenses**  
n = int(input("How many expenses? ")), total = 0. for i in range(n): desc = input("Expense " + str(i+1) + " description: "), amount = float(input("Expense " + str(i+1) + " amount: ")), total += amount, print "  " + desc + ": " + str(amount). print "Total: " + str(round(total, 2)). if total > 100: print "Over budget!" else: print "Within budget."

**5 – Temp converter**  
while True: print "1=C to F 2=F to C 3=Quit", choice = int(input("Choice: ")). If choice == 3: print "Bye", break. Elif choice == 1: c = float(input("Celsius: ")), f = c * 9/5 + 32, print "F: " + str(round(f, 1)). Elif choice == 2: f = float(input("Fahrenheit: ")), c = (f - 32) * 5/9, print "C: " + str(round(c, 1)). Else: print "Invalid".

**6 – Stats**  
n = int(input("How many numbers? ")). If n == 0: print "No numbers". Else: read first number into total, min_val, max_val. for i in range(n - 1): read next number, add to total, if next < min_val: min_val = next, if next > max_val: max_val = next. average = total / n. print "Min: " + str(min_val) + ", Max: " + str(max_val) + ", Sum: " + str(total) + ", Average: " + str(average). Simpler: read all in loop; for the first (i==0) set min and max to that value; for rest update min/max with if.

**7 – Quiz**  
score = 0. Questions can be three pairs: ( "What is 2+2?", 4 ), ( "What is 5*3?", 15 ), ( "What is 10/2?", 5 ). for i in range(3): use a variable for question and answer (or if/elif for i). print question, ans = int(input()), if ans == correct: score += 1. print "Score: " + str(score) + "/3". if score == 3: print "Perfect!" else: print "Keep practicing."

**8 – Registration**  
while True: name = input("Name: "). if name.strip() != "": break. print "Name cannot be empty". Then while True: age = int(input("Age: ")). if age >= 1 and age <= 120: break. print "Age must be 1-120". print "Registered: " + name + ", age " + str(age) + "."

---

## Tips

- **Min/Max without built-ins:** Set min and max to the first number, then in the loop: if current < min: min = current; if current > max: max = current.
- **Loop until valid:** while True, read input, if valid break, else print error.
- **Round for display:** round(x, 1) or round(x, 2) then str() for printing.
- **.strip()** on a string removes leading/trailing spaces; use it to treat "  " as empty.
