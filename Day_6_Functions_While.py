# Functions

# Built-in Functions
# print() Name of a function followed by a set of parantheses
# len()

# Create a Function
# def my_function():
#    Do this
# my_function() Calling function


# While Loops

# While something_is_true:
   # Do something repeatedly

# Example Simple Function

def greet():
   print("Hello")
   print("How do you do?")
   print("Isn't the weather nice today?")

greet()

# Example 

def greet_with_name(name):  # Function that allows for Input
   print(f"Hello {name}")
   print(f"How do you do {name}?")
   print("Isn't the weather nice today?")

greet_with_name("Axel")

# Example

def greet_with(name, surname):  # Functions with more than 1 input
   print(name, surname)

greet_with("Jason", "Bourne")
greet_with(name="Jason", surname="Bourne")
greet_with(surname="Bourne", name="Jason")


# Paint Area Calculator

import math

def paint_calc(height, width, cover):
   number_cans = math.ceil((height * width) / cover)
   print(f"You will need {number_cans} cans of paint")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
