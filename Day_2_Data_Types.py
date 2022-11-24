# print(len(12546))  # object of type 'int' has no len() function

# # Strings

# print("Hello"[0])  # Pulling out a particular element from a string is called sub-scripting.

# num_char = len(input('What is your name?:'))
# print("Your anem has" + num_char + "characters")  # str can only concatenate str (not "int")

# # Integer

# print(12 + 25)
# print(154_154_856 + 1)  # We can replace those commas (154,154,856) simply with underscores.


# # Float

# print(3.14159)
# print(3141.59)  # Floating point number


# # Boolen

# print(True, False)


# # Converting Data

# num_char = len(input('What is your name?:'))
# new_num_char = str(num_char)
# print("Your anem has" + num_char + "characters")

# a = str(123)
# print(type(a))
# b = float(123)
# print(type(b))
# c = int(12.1)
# print(type(c))
# print(c)

# # Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8
# two_digit_number = input("Type a two digit number: ")
# print(int(two_digit_number[0]) + int(two_digit_number[1]))


# # Mathematical Operations

# # PEMDAS
# # Parentheses  ()
# # Exponents  **
# # Multiplication  * Divison  /  # We calculate left to right
# # Addition  + Subtraction  -

# # Example

# print(3 * 3 + 3 / (4 - 3))

# # BMI Calculator
# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
# new_height = float(height)
# new_weight = int(weight)
# output = int(new_weight/(new_height**2))

# print(output) 

# # Round number

# print(round(8 / 3))  # It is going to round it into a whole number
# print(round(2.66666548, 2))  # It is going to round it to two decimal places
# print(round(8 / 3, 2))

# # Floor Divison

# print(8 // 3)  # A whole number ignore after all the numbers the decimal


# # F string

# score = 0
# height = 1.8
# isWinnig = True
# print(f"Your score is {score}, your height is {height}, you are winnig is {isWinnig}")


# # Your Life in Weeks
# age = input("What is your current age? ")
# total_days = 32850
# total_weeks = 4680
# total_months = 1080
# pass_days = int(age)*365
# pass_weeks = int(age)*52
# pass_months = int(age)*12

# print(f"You have {total_days - pass_days} days, {total_weeks - pass_weeks} weeks, and {total_months - pass_months} months left.")

# # Tip Calculator


total_bill = input("What was the total bill? ")
perc_tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")
calculator = round((float(total_bill) / int(people)) * (int(perc_tip) / 100), 2)

print("Welcome to he tip calculator")
print(f"Each person should pay: ${calculator}")
