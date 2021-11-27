"""
Description : Part of 100 Days of Code - The Complete
Python Pro Bootcamp for 2022

Day 9 : Dictionaries, Nesting and the Secret Auction

Day 9 Project: Blind Auction


Author: Ahmed Harbi
Date: November 2021

"""

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

# Starting the program
print(logo)
print("Welcome to the secret auction program.")
run = True
bidders = {}

# Start bidding
while(run):

    # Taking bidder name and value
    bidder = input("What is your name?  ")
    bid = int(input("What is your bid?  $"))

    # saving bidder's inforamtion into bidders dictionary
    bidders[bidder] = bid

    # checking if there any other bidders 
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.     ").lower()
    if other_bidders == 'yes':
        run = True
    elif other_bidders == 'no':
        run = False
    else:
        print("Sorry, no a valid answer.")
        run = True


# getting heighst bid value 
highest_bid = 0
winner = ""
for bidder in bidders:
    if bidders[bidder] > highest_bid:
        highest_bid = bidders[bidder]
        winner = bidder

# showing the result
print(f"The winner is {winner} with a bid of ${highest_bid}.")