from utilities.functions import add, subtract, greet
import requests
from utilities.functions import fibonacci_generator
import sys


#calculator
print(add(10, 5))
print(subtract(10, 5))
print(greet("Aakash"))

response = requests.get("https://thalappakatti.com/")

print("Status Code:", response.status_code)
print("Request successful!")

#fibonacci sequence
print("Fibonacci sequence:")

for number in fibonacci_generator(10):
    print(number)


#compare Generator vs list 
numbers_list = [i for i in range(100000)]

numbers_generator = (i for i in range(100000))

print("List memory:", sys.getsizeof(numbers_list), "bytes")
print("Generator memory:", sys.getsizeof(numbers_generator), "bytes")
