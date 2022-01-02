"""
Description : Part of 100 Days of Code - The Complete
Python Pro Bootcamp for 2022

Day 12 : Scope and Number Guessing Game

Day 12 Project: Number Guessing Game


Author: Ahmed Harbi
Date: November 2021

"""
import random

logo = """   _  __           __             _____                 _             _____              
  / |/ /_ ____ _  / /  ___ ____  / ___/_ _____ ___ ___ (_)__  ___ _  / ___/__ ___ _  ___ 
 /    / // /  ' \/ _ \/ -_) __/ / (_ / // / -_|_-<(_-</ / _ \/ _ `/ / (_ / _ `/  ' \/ -_)
/_/|_/\_,_/_/_/_/_.__/\__/_/    \___/\_,_/\__/___/___/_/_//_/\_, /  \___/\_,_/_/_/_/\__/ 
                                                            /___/                        """

attempts = 1
def welcome_screen():
    """Showing welcome, and some info about the game."""
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

def choose_difficulty():
    """Choosing difficulty of the game with user's input
    and return number of attempts he got."""

    difficulty = input("Choose a difficulty. Type 'easy or 'hard': ")
    if difficulty == 'easy':
        attempts = 10
    elif difficulty == 'hard':
        attempts = 5
    else:
        print("Sorry, Invalid input.")
        attempts = 0
    return attempts


welcome_screen()
attempts = choose_difficulty()
picked_number = random.randint(1, 100)

while(attempts > 0):
    print(f"You have {attempts} attempts remaining to guess the number.")
    guessed_number = int(input("Make a guess: "))
    if guessed_number > picked_number:
        print("Too high.")
        attempts -= 1
        if attempts != 0:
            print ("Guess again.")
    elif guessed_number < picked_number:
        print("Too low.")
        attempts -= 1
        if attempts != 0:
            print("Guess agian.")
    else:
        print(f"You got it! the answer was {picked_number}")
        attempts = 0
        break

if picked_number != guessed_number:
    print(f"You've run out of guesses, the number was {picked_number}, you lose.")