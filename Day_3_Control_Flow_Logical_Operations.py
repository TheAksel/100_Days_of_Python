# If/Else

# if condition:
#    do this
# else:
#   do this

# Example
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?: "))

if height >= 120:
    print("You can ride the rollercoaster!")
else:
    print("Sorry, you have to grow taller befaore you can ride.")


# # # # # # # # # # # # # # # # # # # # 
# Operator # # Meaning # 
#   >    # # Greater Than #
#   <    # # Less Than #
#  >=    # # Greater than or equal to #
#  <=    # # Less than or equal to #
#  ==    # # Equal to # 
#  !=    # # Not equal to #
# # # # # # # # # # # # # # # # # # # # 


# Write a program that works out whether if a given number is an odd or even number.
number = int(input("Which number do you want to check? "))

if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")


# Nested if/else

# if condition:
#   if another condition:
#        do this
#    else:
#        do this
# else:
#    do this

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?: "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?: "))
    if age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry, you have to grow taller befaore you can ride.")


# If/Elif/Else

# if condition1:
#     do A
# elif condition 2:
#     do B
# else:
#    do this

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?: "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?: "))
    if age < 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry, you have to grow taller befaore you can ride.")


# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
bmi = round(weight / (height * height))

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are slightly underweight.")
if bmi > 18.5:
    if bmi < 25:
        print(f"Your BMI is {bmi}, you have a normal weight.")
    elif bmi < 30:
        print(f"Your BMI is {bmi}, you are slightly overweight")
    elif bmi < 35:
        print(f"Your BMI is {bmi}, you are obese.")
    else:
        print(f"Your BMI is {bmi}, you are clinically obese.")


# Write a program that works out whether if a given year is a leap year.
year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year")


# Example
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
total_price = 0


if size == "S":
    total_price = 15
elif size == "M":
    total_price = 20
else:
    total_price = 25

if add_pepperoni == "Y":
    if size == "S":
        total_price += 2
    elif size == "M":
        total_price += 3
    else:
        total_price += 3
else:
    total_price += 0

if extra_cheese == "Y":
    total_price += 1
    print(f"Your final bill is: ${total_price}.")
else:
    print(f"Your final bill is: ${total_price}.")


# Logical Operators

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

lower_case_name = name1.lower()
lower_case_name_2 = name2.lower()

t = lower_case_name_2.count("t") + lower_case_name.count("t")
r = lower_case_name_2.count("r") + lower_case_name.count("r")
u = lower_case_name_2.count("u") + lower_case_name.count("u")
e = lower_case_name_2.count("e") + lower_case_name.count("e")

l = lower_case_name_2.count("l") + lower_case_name.count("l")
o = lower_case_name_2.count("o") + lower_case_name.count("o")
v = lower_case_name_2.count("v") + lower_case_name.count("v")
e = lower_case_name_2.count("e") + lower_case_name.count("e")

total = t + r + u + e
total_2 = l + o + v + e
love_score = int(str(total) + str(total_2))

if (love_score < 10) or (love_score > 90):
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif (love_score > 40) or (love_score < 50):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")


# Choose Your Own Adventure

print("Welcome to Tresure Island.")
print("Your mission is to find the tresure.")

q1 = input('''You're at a crossroad. Where do you want to go? Type "left" or "right": ''')
q1 = q1.lower()

if q1 == "left":
    q2 = input('''You've come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across : ''')
    q2 = q2.lower()
    print(q2)
    if q2 == "swim":
        q3 = input('''You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?: ''')
        q3 = q3.lower()
        print(q3)
        if q3 == "red":
            print("It's a room full of fire.Game Over.")
        elif q3 == "yellow":
            print("You found the treasure! You Win!")
        elif q3 == "blue":
            print("You enter a room of beasts.Game Over.")
        else:
            print("You chose a door that doesn't exist.Game Over.")
    else:
        print("You get attacked by an angry trout.Game Over.")
else:
    print("You fell into a hole.Game Over.")
    