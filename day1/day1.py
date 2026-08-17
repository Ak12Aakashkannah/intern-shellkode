# DAY 1 - PYTHON FUNDAMENTALS
# Fresher Onboarding & Ramp-Up Program


# MODULE 1: PYTHON BASICS

print("=" * 60)
print("MODULE 1: PYTHON BASICS")
print("=" * 60)

# Simple Calculator

print("\nSimple Calculator")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nResults:")
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)

if num2 != 0:
    print("Division:", num1 / num2)
else:
    print("Division: Cannot divide by zero")


# String Manipulation

print("\nString Manipulation")

text = input("Enter a string: ")

print("Original:", text)
print("Reversed:", text[::-1])
print("First 3 characters:", text[:3])


# Dynamic Greeting

print("\nDynamic Greeting")

name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"Hello {name}! You are {age} years old.")
print(f"Welcome to Python, {name}!")


# MODULE 2: CONTROL FLOW

print("\n" + "=" * 60)
print("MODULE 2: CONTROL FLOW")
print("=" * 60)

# Grade Calculator

print("\nGrade Calculator")

score = float(input("Enter your score: "))

if score < 0 or score > 100:
    print("Invalid score.")

elif score > 90:
    print("Grade: A")

elif score > 80:
    print("Grade: B")

elif score > 70:
    print("Grade: C")

else:
    print("Grade: D")


# Leap Year Checker

print("\nLeap Year Checker")

year = int(input("Enter a year: "))

if year % 400 == 0:
    print(f"{year} is a leap year.")

elif year % 100 == 0:
    print(f"{year} is not a leap year.")

elif year % 4 == 0:
    print(f"{year} is a leap year.")

else:
    print(f"{year} is not a leap year.")


# Star Pyramid

print("\nStar Pyramid")

rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):

    for j in range(rows - i):
        print(" ", end="")

    for j in range(2 * i - 1):
        print("*", end="")

    print()


# FizzBuzz

print("\nFizzBuzz")

for number in range(1, 101):

    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")

    elif number % 3 == 0:
        print("Fizz")

    elif number % 5 == 0:
        print("Buzz")

    else:
        print(number)


# MODULE 3: DATA STRUCTURES

print("\n" + "=" * 60)
print("MODULE 3: DATA STRUCTURES")
print("=" * 60)

# Word Frequency Counter

print("\nWord Frequency Counter")

paragraph = input("Enter a paragraph: ")

paragraph = paragraph.lower()

punctuation = ".,!?;:\"'()[]{}"

for symbol in punctuation:
    paragraph = paragraph.replace(symbol, "")

words = paragraph.split()

word_frequency = {}

for word in words:

    if word in word_frequency:
        word_frequency[word] += 1

    else:
        word_frequency[word] = 1

print("\nWord Frequency:")

for word, count in word_frequency.items():
    print(f"{word}: {count}")


# List Comprehensions

print("\nList Comprehensions")

squares = [number ** 2 for number in range(1, 11)]

print("Squares:", squares)

even_numbers = [
    number
    for number in range(1, 21)
    if number % 2 == 0
]

print("Even numbers:", even_numbers)

words = ["python", "java", "c++", "javascript"]

uppercase_words = [word.upper() for word in words]

print("Uppercase words:", uppercase_words)


# Set Operations

print("\nSet Operations")

list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]

set1 = set(list1)
set2 = set(list2)

intersection = set1.intersection(set2)

difference1 = set1.difference(set2)

difference2 = set2.difference(set1)

print("List 1:", list1)
print("List 2:", list2)

print("Common elements:", intersection)
print("Only in List 1:", difference1)
print("Only in List 2:", difference2)


# END OF DAY 1

print("\n" + "=" * 60)
print("DAY 1 COMPLETE!")
print("=" * 60)