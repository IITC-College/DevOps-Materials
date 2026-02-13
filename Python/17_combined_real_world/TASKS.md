# Tasks – Combined Real-World (Everything So Far)

These tasks are harder and more realistic. Each one combines **input()**, **variables**, **conditions** (if/elif/else), **logical operators** (and/or/not), **loops** (for/while, range, break/continue), **type casting** (int/float/str), **operators**, and **string formatting**. Use comments where they help. Create each file, run it, and test with different inputs.

Run scripts with: `python3 script_name.py`

---

## Task 1 – Grade report (name, N scores, average, letter grade)

**File:** `real_grade_report.py`

- Ask for the student's name and how many scores they have. Read that many scores in a loop (prompt like "Score 1:", "Score 2:", …). Store each in a variable and add to a total. After the loop compute the average (total / count). Use if/elif/else to set a letter grade: A (≥90), B (≥80), C (≥70), D (≥60), F (otherwise). Print one line: `"Student: [name], Average: [avg], Grade: [letter]"` using variables and `str()`.
- Use: input(), variables, for + range(), int()/float(), accumulation, if/elif/else, string concatenation.

**Expected output (example – Ali, 3 scores 85, 90, 78):**
```
Student name: Ali
How many scores? 3
Score 1: 85
Score 2: 90
Score 3: 78
Student: Ali, Average: 84.3, Grade: B
```

---

## Task 2 – Menu calculator (loop until quit)

**File:** `real_menu_calc.py`

- Use a loop that runs until the user quits. Each time: print a menu "1=Add 2=Subtract 3=Multiply 4=Quit" and read the choice (int). If choice is 4, print "Bye" and break. If 1: read two numbers (float), print their sum. If 2: read two numbers, print their difference. If 3: read two numbers, print their product. If anything else: print "Invalid option". Then loop again (except when 4). Use variables for choice and for the two numbers.
- Use: while True or for with large range + break, input(), int()/float(), if/elif/else, operators.

**Expected output (example – Add 10 and 3, then Quit):**
```
1=Add 2=Subtract 3=Multiply 4=Quit
Choice: 1
First number: 10
Second number: 3
13.0
1=Add 2=Subtract 3=Multiply 4=Quit
Choice: 4
Bye
```

---

## Task 3 – Login with 3 attempts

**File:** `real_login.py`

- Store a secret username and password in two variables (e.g. "admin" and "secret"). Use a for loop that runs at most 3 times. Each time: ask for username and password (two inputs). If both match the secret, print "Welcome, [username]!" and break. Otherwise print "Wrong. Attempts left: X" (use a variable or expression for X, e.g. 2 - attempt index). After the loop, if the user never succeeded (you can use a variable like logged_in = False, set True on success), print "Locked."
- Use: for + range(), input(), comparison (==), and, break, variables, str().

**Expected output (example – wrong twice, then correct):**
```
Username: admin
Password: wrong
Wrong. Attempts left: 2
Username: user
Password: x
Wrong. Attempts left: 1
Username: admin
Password: secret
Welcome, admin!
```

---

## Task 4 – Expense list and budget check

**File:** `real_expenses.py`

- Ask "How many expenses?" and read n. Use a variable total = 0. In a for loop (range(n)): ask for a description (string) and an amount (float). Add the amount to total and print a line like "  [description]: [amount]" using variables. After the loop print "Total: " + str(round(total, 2)). If total > 100 print "Over budget!" else print "Within budget." Use variables for description, amount, and total.
- Use: input(), int()/float(), for + range(), accumulation, if/else, str(), round().

**Expected output (example – 2 expenses: Coffee 4.5, Lunch 12):**
```
How many expenses? 2
Expense 1 description: Coffee
Expense 1 amount: 4.5
  Coffee: 4.5
Expense 2 description: Lunch
Expense 2 amount: 12
  Lunch: 12.0
Total: 16.5
Within budget.
```

---

## Task 5 – Temperature converter with menu

**File:** `real_temp_convert.py`

- Loop until quit. Print menu: "1=C to F 2=F to C 3=Quit". Read choice (int). If 1: ask for temperature in Celsius (float), compute F = C * 9/5 + 32, print "F: " + str(round(F, 1)). If 2: ask for Fahrenheit, compute C = (F - 32) * 5/9, print "C: " + str(round(C, 1)). If 3: print "Bye" and break. Else: print "Invalid". Use variables for choice and temperature.
- Use: while/for + break, input(), int()/float(), if/elif/else, operators, str(), round().

**Expected output (example – 1, then 25, then 3):**
```
1=C to F 2=F to C 3=Quit
Choice: 1
Celsius: 25
F: 77.0
1=C to F 2=F to C 3=Quit
Choice: 3
Bye
```

---

## Task 6 – Number stats (min, max, sum, average) without min()/max()

**File:** `real_stats.py`

- Ask "How many numbers?" and read n. Read n numbers (float) in a for loop. Use variables: total (sum), and for min and max either set them to the first value (read the first outside the loop or use the first inside) and update inside the loop with if (e.g. if current < min: min = current). After the loop print "Min: [min], Max: [max], Sum: [sum], Average: [avg]". Handle n=0 (don't divide by zero; print "No numbers" or skip average). Use variables and str().
- Use: input(), int()/float(), for + range(), variables, if (for min/max), operators, division.

**Expected output (example – 4 numbers: 3, 7, 2, 9):**
```
How many numbers? 4
Number 1: 3
Number 2: 7
Number 3: 2
Number 4: 9
Min: 2.0, Max: 9.0, Sum: 21.0, Average: 5.25
```

---

## Task 7 – Simple quiz (3 questions, score)

**File:** `real_quiz.py`

- Define three questions and their correct answers (e.g. "What is 2+2?" → 4, "What is 5*3?" → 15, "What is 10/2?" → 5). Use a variable score = 0. Loop over the three (e.g. for i in range(3), and use separate variables or a simple pattern for question text and correct answer). For each: print the question, read the user's answer (int), compare to the correct answer; if equal, add 1 to score. After the loop print "Score: X/3" and if score == 3 print "Perfect!" else print "Keep practicing." Use variables and str().
- Use: for + range(), input(), int(), comparison, if, variables, str().

**Expected output (example – 4, 15, 5):**
```
What is 2+2? 4
What is 5*3? 15
What is 10/2? 5
Score: 3/3
Perfect!
```

---

## Task 8 – Validated registration (name and age)

**File:** `real_register.py`

- Ask for name. Use a while loop: if the name is empty (e.g. after stripping spaces: name.strip() == ""), print "Name cannot be empty" and ask again; otherwise break. Then ask for age (int). Use another while loop: if age < 1 or age > 120, print "Age must be 1-120" and ask again; otherwise break. Finally print "Registered: [name], age [age]." Use variables and logical operators (and/or) in the conditions.
- Use: while, input(), int(), if, and/or, variables, str(). (You can use .strip() on the string to ignore leading/trailing spaces.)

**Expected output (example – empty name once, then "Ali", then 200, then 25):**
```
Name: 
Name cannot be empty
Name: Ali
Age: 200
Age must be 1-120
Age: 25
Registered: Ali, age 25.
```

---

## Done

You've combined: input and variables, type casting, conditions and logical operators, for/while loops with range and break, accumulation and min/max logic, and string formatting—all in small realistic programs.
