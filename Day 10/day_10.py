"""
Description : Part of 100 Days of Code - The Complete
Python Pro Bootcamp for 2022

Day 10 : Functions with Output

Day 10 Project: Calculator


Author: Ahmed Harbi
Date: November 2021

"""

import os

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


def calc(first_number, second_number, operation):
    """Taking first number, second number and operation. 
        perform the desired operation of addition, subtraction, multiplication or division.
        In case of a not valid input returns 0
    """

    if operation == '+':
        return (first_number + second_number)
    elif operation == '-':
        return (first_number - second_number)
    elif operation == '*':
        return (first_number * second_number)
    elif operation == '/':
        return (first_number / second_number)
    else:
        print("Sorry, not a valid operation.")
        return 0


# Start progam
print(logo)
run = True
save_answer = 's'


def get_parameters(first_number):
    """Taking first number as input, get the second number and
       operation from the user, perform calculations and print the result.
       it returns two variables:
                - save_answer: determine what is the next phase of the program
                - answer: contains the final answer.
    """

    # Take user inputs
    operation = input("Which operation do you want to do? '+', '-', '*', '/'.   ")
    second_number = float(input("What is the second number?     "))

    # perform calculations
    answer = calc(first_number, second_number, operation)
    print(f"\n{first_number} {operation} {second_number} = {answer}\n")

    # select upcoming phase of the application
    save_answer = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start new calculation. Enter 'q' to quit.     ")

    # return phase, and final answer
    return save_answer, answer


while(run):

    # in case of taking final result as the first number for upcoming operation
    if save_answer == 'y':
        first_number = answer
        save_answer, answer = get_parameters(first_number)
        run = True

    # in case of start new operation with new numbers
    elif save_answer == 'n':

        # clear the terminal and reshow logo
        os.system('cls' if os.name == 'nt' else 'clear')
        print(logo)
        first_number = first_number = float(input("What is the first number?   "))
        save_answer, answer = get_parameters(first_number)
        run = True

    # the starting phase of the program
    elif save_answer == 's':
        first_number = first_number = float(input("What is the first number?   "))
        save_answer, answer = get_parameters(first_number)
        run = True

    # case of quitting the program
    elif save_answer == 'q':
        run = False

    # case of not valid choise
    else:
        print("Sorry, not a valid answer.")
        save_answer = 'y'

