"""
Description : Part of 100 Days of Code - The Complete
Python Pro Bootcamp for 2022

Day 5 : Python Loops

Day 5 Project: Create a Password Generator


Author: Ahmed Harbi
Date: November 2021

"""

import random

letters_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
                'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers_list = ['1', '2', '4', '5', '6', '7', '8', '9', '0']

symbols_list = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', ',',
                '.', '<', '>', '/', '?', ':', ';', '"', "'", '[', ']', '{', '}', '`', '~']

charchters = [letters_list, numbers_list, symbols_list]

letters_required = int(input("How many letters would you like in your password?     "))
numbers_required = int(input("How many numbers would you like in your password?     "))
symbols_required = int(input("How many symbols would you like in your password?     "))

password_length = letters_required + numbers_required + symbols_required

password = ""

for charchter in range(password_length):
    if letters_required > 0:
        if numbers_required > 0:
            if symbols_required > 0:
                password += random.choice(charchters[random.randint(0, 2)])
            else:
                password += random.choice(charchters[random.randint(0, 1)])
        else:
            if symbols_required > 0:
                password += random.choice(charchters[random.randint(-1, 0)])
            else:
                password += random.choice(charchters[0])
    else:
        if numbers_required > 0:
            if symbols_required > 0:
                password += random.choice(charchters[random.randint(1, 2)])
            else:
                password += random.choice(charchters[1])
        else:
            password += random.choice(charchters[-1])

    if password[-1] in numbers_list:
        numbers_required -= 1
    elif password[-1] in symbols_list:
        symbols_required -= 1
    elif password[-1] in letters_list:
        letters_required -= 1


print(f"Your password is:  {password}")
    
