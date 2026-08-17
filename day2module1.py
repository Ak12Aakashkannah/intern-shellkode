from functools import reduce


# Function Library

# Find minimum number
def find_min(numbers):
    return min(numbers)


# Find maximum number
def find_max(numbers):
    return max(numbers)


# Calculate average
def average(numbers):
    return sum(numbers) / len(numbers)


# Check if a number is prime
def is_prime(number):
    if number < 2:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True


# Check if a string is a palindrome
def is_palindrome(text):
    text = text.lower()
    return text == text[::-1]


# Test Function Library
numbers = [10, 20, 30, 40, 50]

print("Minimum:", find_min(numbers))
print("Maximum:", find_max(numbers))
print("Average:", average(numbers))

print("Is 7 prime?", is_prime(7))
print("Is 10 prime?", is_prime(10))

print("Is 'madam' a palindrome?", is_palindrome("madam"))
print("Is 'hello' a palindrome?", is_palindrome("hello"))


# *args Example
def add_numbers(*args):
    return sum(args)


print("\n*args Example:")
print("Sum:", add_numbers(10, 20, 30, 40))


# **kwargs Example
def show_details(**kwargs):
    print("\n**kwargs Example:")

    for key, value in kwargs.items():
        print(key, ":", value)


show_details(
    name="Aakash",
    age=20,
    course="Python"
)


# Lambda Functions
min_lambda = lambda numbers: min(numbers)
max_lambda = lambda numbers: max(numbers)
average_lambda = lambda numbers: sum(numbers) / len(numbers)

print("\nLambda Examples:")
print("Minimum:", min_lambda(numbers))
print("Maximum:", max_lambda(numbers))
print("Average:", average_lambda(numbers))


# Map Example
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squared_numbers = list(map(lambda x: x ** 2, numbers))

print("\nMAP Example:")
print("Original numbers:", numbers)
print("Squared numbers:", squared_numbers)


# Filter Example
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print("\nFILTER Example:")
print("Even numbers:", even_numbers)


# Reduce Example
product = reduce(lambda x, y: x * y, numbers)

print("\nREDUCE Example:")
print("Product:", product)