# # For Loop

# # for item in list_of_items
# #     Do something to each item

# # Example

# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " Pie")
# print(fruits)

# # Calculates the average student height

# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
  
# total_height = 0
# for height in student_heights:
#   total_height += height
# print(f"total height = {total_height}")

# number_of_students = 0
# for student in student_heights:
#   number_of_students += 1
# print(f"number of students = {number_of_students}")
  
# average_height = round(total_height / number_of_students)
# print(average_height)


# # Range

# # for number in range(a, b): I am going to get hold of each number in that range and do something with that number. ! B not included
# #    print(number)

# # Example

# total = 0
# for number in range(1, 101):
#     total += number
# print(total)


# # FizzBuzz Game

# for number in range(1,101):
#     if number % 3 == 0:
#         if number % 5 == 0:
#             print("FizzBuzz")
#         else:
#             print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)
       

# # Password Generator

# import random

# q1 = int(input("How many letters would you like in your password?: "))
# q2 = int(input("How many symbols would you like?: "))
# q3 = int(input("How many numbers would you like?: "))


# letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
# symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "&", "~", "*"]
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# password = ""
# for i in range(1, q1 + 1):
#     # random_i = random.choice(letters)
#     password += random.choice(letters)
# for i in range(1, q2 + 1):
#     password += random.choice(symbols)
# for i in range(1, q3 + 1):
#     password += random.choice(numbers)
# print(password)
    




