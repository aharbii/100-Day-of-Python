"""
Description : Part of 100 Days of Code - The Complete
Python Pro Bootcamp for 2022

Day 8 : Function Parameters and Caesar Cipher

Day 8 Project: Caesar Cipher


Author: Ahmed Harbi
Date: November 2021

"""

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

lower_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def encoding(message, shift):
    encoded = ""
    for letter in message:
        if letter in lower_letters or letter in upper_letters:
            if letter in lower_letters:
                letters_list = lower_letters
            else:
                letters_list = upper_letters
            index = letters_list.index(letter)
            shifted = index + shift
            if shifted < len(letters_list):
                encoded += letters_list[shifted]
            else:
                shifted -= len(letters_list)
                encoded += letters_list[shifted]
        else:
            encoded += letter

    return encoded

def decoding(message, shift):
    decoded = ""
    for letter in message:
        if letter in lower_letters or letter in upper_letters:
            if letter in lower_letters:
                letters_list = lower_letters
            else:
                letters_list = upper_letters
            index = letters_list.index(letter)
            shifted = index - shift
            decoded += letters_list[shifted]
        else:
            decoded += letter

    return decoded

print(logo)
run = True

def get_message():
    input_message = input("Type your message:     ")
    input_shift = int(input("Type the shift number:    "))

    return input_message, input_shift

while (run):
    mode = input("\nType 'encode' to encrypt, type 'decode' to decrypt:   ").lower()

    if mode == 'encode':
        input_message, input_shift = get_message() 
        encoded_message = encoding(input_message, input_shift)
        print(f"Here's the encoded result:   {encoded_message}")
    elif mode == 'decode':
        input_message, input_shift = get_message()
        decoded_message = decoding(input_message, input_shift)
        print(f"Here's the decoded result:   {decoded_message}")
    else:
        print ("Not valid input.")
        run = True
        continue

    run_again = input("\nType 'yes' if you want to go again. Otherwise type 'no':     ").lower()

    if run_again == 'yes':
        run = True
    elif run_again == 'no':
        run = False
    else:
        print("\nSorry did not get that.")
        run = True
