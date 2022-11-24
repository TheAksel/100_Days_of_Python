# Print function
print("What do you want to do?")

print("Hello World!")

print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")


# \n means new line
print("Hello World!\nHello World!\nHello World!")  # This is the command that shows you how to print seperates line.


# Combine two strings (Concatenation)
print("Hello" + "Angela")  # Without na space
print("Hello" + " Angela")  # With space
print("Hello " + "Angela")  # With space
print("Hello" + " " + "Angela")  # With space


# Input function
input("A prompt for the user")
input("What's your name?")
print("Hello " + input("What is your name?"))
print(len(input("What is your name? ")))

# Example
name = input("What is your name?")  # We've saved the data from this action to a name
print(name)

name = input("What is your name?")
length = len(name)
print(name)

# Example  Write a program that switches the values stored in the variables a and b.
a = input("a: ")
b = input("b: ")

c = a
a = b
b = c

print("a: " + a)
print("b: " + b)

# Example
print("Welcome to the Band Name Generator")
born = input("What's the name of the city yoi grew up?")
pet_name = input("What is your pet name")
print("Your band name could be" + " " + born + " " + pet_name)