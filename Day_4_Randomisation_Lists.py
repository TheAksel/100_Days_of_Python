# Randomisation
import random  # Before use, you have to import the command

random_integer = random.randint(1, 10)
print(random_integer)

random_float = random.random()  # Returns the next random floating point number between [0.0 to 1.0) 1.0 not included
print(random_float)

print(random_float * 5)  # 0.0000... - 4.99999...


# "Heads" or "Tails"

game = input("Heads or Tails: ").capitalize

random_money = random.randint(0, 1)

if random_money == 0:
    print("Tails")
else:
    print("Heads")


# Lists

# variable = [item1, item2]

# variable[1] = "item3"  # You can change the items in the list.
# variable.append("item4")  # You can add new item to ypur list.
# variable.remove("item4")  # You can delete an item from list.
# variable.extend(["item5", "item6"])  # You can extend the list by appending all the items from the iterable.

 
# Example

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
name_list = len(names)

random_name = random.randint(0, name_list - 1)

print(names[random_name], "is going to buy the meal today!")


# Nested Lists

fruits = ["Strawberries", "Apple", " Grapes", "Peaches"]
vegetables = ["Spinach", "Kale", "Tomatoes"]
dirty_dozen = [fruits, vegetables]
print(dirty_dozen)

# Example

row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

horizontal = position[0]
vertical = position[1]
map[int(vertical) - 1][int(horizontal) - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")

# Example

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))

pc_player = random.randint(0,2)

if user == 0:
    if pc_player == 0:
        print(f"{rock}\n Computer chose:\n {rock}\n You win")
    elif pc_player == 1:
        print(f"{paper}\n Computer chose:\n {paper}\n You lose")
    else:
        print(f"{rock}\n Computer chose:\n {scissors}\n You lose")
if user == 1:
    if pc_player == 0:
        print(f"{paper}\n Computer chose:\n {rock}\n You lose")
    elif pc_player == 1:
        print(f"{paper}\n Computer chose:\n {paper}\n You win")
    else:
        print(f"{paper}\n Computer chose:\n {scissors}\n You lose")
if user == 2:
    if pc_player == 0:
        print(f"{scissors}\n Computer chose:\n {rock}\n You lose")
    elif pc_player == 1:
        print(f"{scissors}\n Computer chose:\n {paper}\n You lose")
    else:
        print(f"{scissors}\n Computer chose:\n {scissors}\n You win")
