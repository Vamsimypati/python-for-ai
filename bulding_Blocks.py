# Function Defition
def python():
    print("Hello World!!")
python()

#calling Functions
def say_goodbye():
    print("Goodbye!!")
    print("See You Later!!")

say_goodbye()
say_goodbye()
say_goodbye()

# Function With Logic
def check_weather():
    temperature = 32
    if temperature > 25:
        print("Its Too Hot")
    else:
        print("Its Nice Weather")

check_weather()

# Basic parameters
def greet(name):
    print(f"Hello World , {name}")

greet("Vamsi")

# Multiple parameters
def calculate_total(price, tax_rate, discount):
    tax = price * tax_rate
    final_price = price + tax - discount
    print(f"Total: ${final_price}")

calculate_total(100, 0.08, 10)

# Return Values
def add_print(a,b):
    print(a + b)

add_print(a=13,b=17)

def add_return(a,b):
    return a + b

result = add_return(67,90)

#return statements
def calculate_area(width, height):
    area = width * height
    return area

room_heigth = calculate_area(27, 92)
print(f"Room size: {room_heigth} sq ft")

#using Return Values
def double(numbers):
    return numbers * 2

result = double(8)

total = double(8) + double(3)

print(double(9))

if double(4) > 10:
    print("It is a Valid Condition")

# Return Multiple Values
def simple_function():
    numbers = [1, 2, 3, 4, 5]
    first_number = numbers[3]
    last_number = numbers[-2]
    return first_number, last_number

first_number , last_number = simple_function()
print(first_number)

#import Random
import math
math.sqrt(16)

from math import sqrt,pi
sqrt(20)

#Buid in Choice
import random

number = random.randint(1,10)
choice = random.choice(["Apple", "Banana", "Ice Fruits"])

#Common build in modules
import datetime
today = datetime.date.today()
print(today)

import os
current_dir = os.getcwd()
print(current_dir)

import json
data = {"name": "Alice", "age":30}
json_string = json.dumps(data)

