"""
Description : Part of 100 Days of Code - The Complete
Python Pro Bootcamp for 2022

Day 15 Project: Coffee Machine Program

Author: Ahmed Harbi
Date: December 2021
"""

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "Money": 0
}


def check_resources(drink):
    available = True
    for ingredient in MENU[drink]["ingredients"]:
        if resources[ingredient] != "Money":
            if MENU[drink]["ingredients"][ingredient] > resources[ingredient]:
                available = False
                break
    if available == False:
        print(f"sorry, there's no enough {ingredient}.")
    return available


def process_coins(drink):
    avialble = True
    print(f"{drink} costs ${MENU[drink]['cost']}.")
    print("Please, insert coins.")
    quarters = int(input("Quarters: "))
    dimes = int(input("Dimes: "))
    nickels = int(input("Nickels: "))
    pennies = int(input("Pennies: "))

    total_coins = (quarters * 0.25) + (dimes * 0.1) + \
        (nickels * 0.05) + (pennies * 0.01)
    cost = MENU[drink]["cost"]
    if cost > total_coins:
        print("Sorry, that's not enough money! Money refunded.")
    else:
        remains = total_coins - cost
        resources["Money"] += cost
        remains = round(remains, 2)
        print(f"Here's ${remains} in change.")
    return avialble


def make_coffee(drink):
    for ingredient in MENU[drink]["ingredients"]:
        if resources[ingredient] != "Money":
            resources[ingredient] -= MENU[drink]["ingredients"][ingredient]
    print(f"Here's your {drink} Enjoy!")

def resupply(resources):
    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
        "Money": resources["Money"]
    }
    print("Resources's now available.")
    return resources

turn_on = True
while (turn_on):
    order = input("What would you like? (espresso/latte/cappuccino): ")
    order = order.lower()
    if order == "report":
        for resource in resources:
            print(f"{resource}: {resources[resource]}")
    elif order == "off":
        turn_on = False
    elif order == "espresso" or order == "latte" or order == "cappuccino":
        if check_resources(order):
            if process_coins(order):
                make_coffee(order)
    elif order == "resupply":
        resources = resupply(resources)
    else:
        print("Unvalid input, mahcine has been restarted!")

# TODO: 1. Print report of all coffe machine resources
# TODO: 2. Check resources sufficient
# TODO: 3. Process Coins
# TODO: 4. Check transaction successful
# TODO: 5. Make Coffee
