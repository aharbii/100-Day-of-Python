"""
Description : Part of 100 Days of Code - The Complete
Python Pro Bootcamp for 2022

Day 11 : The BlackJack Capstone

Day 11 Project: BlackJack Game


Author: Ahmed Harbi
Date: November 2021

"""

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

import random

cards = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
symbol_card = {
    'A': 1,
    'J': 10,
    'Q': 10,
    'K': 10
}

def symbol_conversion(player_cards, player=False):
    """Converts symbol cards into their value"""
    player_cards_value = []
    for i in range(len(player_cards)):
        if player_cards[i] in ['J', 'Q', 'K']:
            card_value = symbol_card[player_cards[i]]
            player_cards_value.append(card_value)
        elif player_cards[i] == 'A' and player == True:
            ace_value = int(input("You got an Ace! you want to count it as 11 or 1?     "))
            player_cards_value.append(ace_value)
        elif player_cards[i] == 'A' and player == False:
            ace_value = 1
            player_cards_value.append(ace_value)
        else:
            player_cards_value.append(player_cards[i])

    return player_cards_value

def check_bust(score):
    """"Checks if player score is greater than 21"""
    bust = False
    if score > 21:
        bust = True
    
    return bust

def decide_winner(first_player, second_player):
    first_player_diff = 21 - first_player
    second_player_diff = 21 - second_player

    if second_player_diff > first_player_diff:
        print("You win!")
    elif second_player_diff == first_player_diff:
        print("It's a draw!")
    else:
        print("You lose.")

def init_cards():
    """Creating array of two random cards"""
    return [random.choice(cards), random.choice(cards)]

def decide_ace(player_score):
    """"decides ace's value for computer 1 ot 11"""
    for i in range(len(second_player_cards)):
            if second_player_cards[i] == 'A':
                if 10 + player_score == 21:
                    player_score += 10
    return player_score

# Start the game
start_game = input("Do you want to play BlackJack Game? hit 'y' or 'n'.     ")
start_game = 'y'
while(start_game == 'y'):
    # print logo
    print(logo)
    
    # initialize cards
    first_player_cards = init_cards()
    second_player_cards = init_cards()

    # show cards
    print(f"Your cards: {first_player_cards}")
    print(f"Computer's cards: {random.choice(second_player_cards)}")

    # first player decide to draw
    draw = input("Type 'y' to get another card, type 'n' to pass.   ")
    if draw == 'y':
        first_player_cards.append(random.choice(cards))

    # get first player's cards value
    first_player_cards_value = symbol_conversion(first_player_cards, player=True)
    first_player_score = sum(first_player_cards_value)
    
    # checking for bust
    first_player_bust = check_bust(first_player_score)
    if first_player_bust:
        print(f"Your final hand: {first_player_cards}")
        print("It's a Bust, You lose.")

    # in case of no bust    
    else:
        
        # getting computer's cards value
        second_player_cards_value = symbol_conversion(second_player_cards)
        second_player_score = sum(second_player_cards_value)

        # in case of having ace
        second_player_score = decide_ace(second_player_score)

        # in case of wants to draw
        if second_player_score < 17:
            second_player_cards.append(random.choice(cards))

        # getting computer's final score
        second_player_cards_value = symbol_conversion(second_player_cards)
        second_player_score = sum(second_player_cards_value)
        second_player_score = decide_ace(second_player_score)

        # showing final scores
        print(f"Your final hand: {first_player_cards}")
        print(f"Computer's final hand: {second_player_cards}")

        # showwing winner
        decide_winner(first_player_score, second_player_score)

    # start new round or end the game
    start_game = input("Do you want to play BlackJack Game? hit 'y' or 'n'.     ")



    
