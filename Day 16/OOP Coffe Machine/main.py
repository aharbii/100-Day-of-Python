"""
Description : Part of 100 Days of Code - The Complete
Python Pro Bootcamp for 2022

Day 16 Project: OOP Coffee Machine Program

Author: Ahmed Harbi
Date: December 2021
"""


from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
drinks = menu.get_items()

turn_on = True
while (turn_on):
    order = input("What would you like? (espresso/latte/cappuccino): ")
    order = order.lower()
    if order == "report":
        coffee_maker.report()
        money_machine.report()
    elif order == "off":
        turn_on = False
    elif order in drinks:
        drink = menu.find_drink(order)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
    else:
        drink = menu.find_drink(order)
