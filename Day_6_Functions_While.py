# # Functions

# # Built-in Functions
# # print() Name of a function followed by a set of parantheses
# # len()

# # Create a Function
# # def my_function():
# #    Do this
# # my_function() Calling function


# # While Loops

# # While something_is_true:
   # # Do something repeatedly


# # Hangman

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_of_game = False
word_list = ["penguin", "nato", "christmas", "democracy", "malware", "board"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
print(f"{' '.join(display)}")

if "_" not in display:
        end_of_game = True
        print("You win.")
print(stages[lives])