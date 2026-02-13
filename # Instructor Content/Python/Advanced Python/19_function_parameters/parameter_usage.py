#!/usr/bin/env python3
# Using parameters in function body

def repeat_message(message, times):
    for i in range(times):
        print(f"{i+1}. {message}")

def calculate_average(num1, num2, num3):
    total = num1 + num2 + num3
    average = total / 3
    return average

def build_filename(name, extension):
    filename = f"{name}.{extension}"
    return filename

# Parameters are used in the function logic
repeat_message("Hello", 3)

avg = calculate_average(10, 20, 30)
print(f"Average: {avg}")

file = build_filename("report", "pdf")
print(f"Filename: {file}")
