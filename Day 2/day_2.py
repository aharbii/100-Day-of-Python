"""
Description : Part of 100 Days of Code - The Complete
Python Pro Bootcamp for 2022

Day 2 : Understanding Data Types and How to Manipulate
Strings

Day 2 Project: Tip Calculator


Author: Ahmed Harbi
Date: November 2021

"""

print("Welcome to the tip calculator.")

total_bill = float(input("What was the total bill? $      "))
tip_percentage = (float(input("What percentage tip would you like to give? 10, 12 or 15?     ")) / 100) + 1
people_number = int(input("How many people to split the bill?     "))

total_value = total_bill * tip_percentage
person_value = round(total_value / people_number, 2)

print(f"Each person should pay: ${person_value}")
