# Using API call and arguments
num = [1, 5, 6, 7]
total = sum(num)
print(total)

# Try and Except keyword
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(num1 + num2)
except ValueError:
    print("Invalid input!")

# Using OS module
import os

user_name = os.getenv("USERNAME")
print(user_name)

# Json dump and load
import json

text = "dump() converts python objects to json text and load() does the reverse"
with open("class.json", "w") as file:
    json.dump(text, file)

with open("class.json", "r") as file:
    load = json.load(file)
    print(load)