"""
Description : Part of 100 Days of Code - The Complete
Python Pro Bootcamp for 2022

Day 7 : Hangman Game

Author: Ahmed Harbi
Date: November 2021

"""

import random
import hangman
logo = hangman.logo


print(logo)

stages = hangman.stages

words = hangman.words

chosen = random.choice(words)

revealed = ""

for i in range(len(chosen)):
    revealed += "_"

for letter in revealed:
    print(letter, end=" ")
print('\n')

counter = 0

while(counter < len(stages)):
    guessed_letter = input("Guess a letter: ")

    if guessed_letter.lower() in revealed.lower():
        print(f"\nYou already guessed {guessed_letter}. Try another letter.")
    else:
        if guessed_letter.lower() in chosen.lower():
            for i in range(len(chosen)):
                if chosen[i].lower() == guessed_letter.lower():
                    revealed = revealed[:i] + guessed_letter + revealed[i+1:]
            
            print ("\nCorrect")
        else:
            print(f"\nYou guessed {guessed_letter}, that's not in the word. You lose a life.")
            print(stages[counter])
            counter += 1

    if revealed.lower() == chosen.lower():
        print(f"\nThe word was '{chosen}'.\nYou win!")
        break
    
    if counter == len(stages):
        print(f"\nThe word was '{chosen}'.\nGame Over.")
        break
    
    for letter in revealed.capitalize():
        print(letter, end=" ")
    print('\n')
