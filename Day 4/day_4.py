"""
Description : Part of 100 Days of Code - The Complete
Python Pro Bootcamp for 2022

Day 4 : Randomisation and Python Lists

Day 4 Project: Rock Paper Scissors


Author: Ahmed Harbi
Date: November 2021

"""

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

#Write your code below this line 👇


import random

choises = [rock, paper, scissors]
user_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.    '))
if user_choice >= 3 or user_choice < 0:
    print("You entered an invalid choise.")
else:
    user_choice = choises[user_choice]
    print (user_choice)

    computer_choice = random.choice(choises)
    print(f"Computer Chose:\n{computer_choice}")

    if user_choice == computer_choice:
        print("It's a draw.")
    if (user_choice == rock and computer_choice == scissors) or (user_choice == paper and computer_choice == rock) or (user_choice == scissors and computer_choice == paper):
        print("You win!")
    if (user_choice == scissors and computer_choice == rock) or (user_choice == rock and computer_choice == paper) or (user_choice == paper and computer_choice == scissors):
        print("You lose.")