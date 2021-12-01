"""
Description : Part of 100 Days of Code - The Complete
Python Pro Bootcamp for 2022

Day 14 Project: Higher Lower Game

Author: Ahmed Harbi
Date: December 2021
"""

# Create Dictionary of celebrities and their followers
# get two random keys from dictionary
# Ask user to guess who is higher

# if right get the right answer and compare it to another random key, count score
# keep going 
# if wrong print sorry you are wrong , view score

import random
logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

celeb = {                                           'Instagram': ['Social media platform, United States', 346],
                                                            'Cristiano Ronaldo': ['Footballer, Portugal', 215],
                                                 'Ariana Grande': ['Musician and actress, United States', 183],
                                     'Dwayne Johnson': ['Actor and professional wrestler, United States', 181],
                                                  'Selena Gomez': ['Musician and actress, United States', 174],
    'Kylie Jenner': ['Reality TV personality and businesswoman and Self-Made Billionaire, United States', 172],
                            'Kim Kardashian': ['Reality TV personality and businesswoman, United States', 167],
                                                                'Lionel Messi': ['Footballer, Argentina', 149],
                                                                   'Beyoncé': ['Musician, United States', 145],
                                                                         'Neymar': ['Footballer, Brasil', 138],
                                                       'National Geographic': ['Magazine, United States', 135],
                                                                    'Justin Bieber': ['Musician, Canada', 133],
                                                              'Taylor Swift': ['Musician, United States', 131],
                                    'Kendall Jenner': ['Reality TV personality and Model, United States', 127],
                                                'Jennifer Lopez': ['Musician and actress, United States', 119],
                                                         'Nicki Minaj': ['Musician, Trinidad and Tobago', 113],
                                                      'Nike': ['Sportswear multinational, United States', 109],
                          'Khloé Kardashian': ['Reality TV personality and businesswoman, United States', 108],
                                                   'Miley Cyrus': ['Musician and actress, United States', 107],
                                                                 'Katy Perry': ['Musician, United States', 94],
                                          'Kourtney Kardashian': ['Reality TV personality, United States', 90],
                                                       'Kevin Hart': ['Comedian and actor, United States', 89],
                                                            'Ellen DeGeneres': ['Comedian, United States', 87],
                                                                'Real Madrid CF': ['Football club, Spain', 86],
                                                                  'FC Barcelona': ['Football club, Spain', 85],
                                                       'Rihanna': ['Musician and businesswoman, Barbados', 81],
                                                    'Demi Lovato': ['Musician and actress, United States', 80],
                                                    "Victoria's Secret": ['Lingerie brand, United States', 69],
                                                        'Zendaya': ['Actress and musician, United States', 68],
                                                                         'Shakira': ['Musician, Colombia', 66],
                                                                             'Drake': ['Musician, Canada', 65],
                                                                'Chris Brown': ['Musician, United States', 64],
                                                      'LeBron James': ['Basketball player, United States', 63],
                                                                    'Vin Diesel': ['Actor, United States', 62],
                                                                    'Cardi B': ['Musician, United States', 67],
                                                           'David Beckham': ['Footballer, United Kingdom', 82],
                                                              'Billie Eilish': ['Musician, United States', 61],
                                                'Justin Timberlake': ['Musician and actor, United States', 59],
                                            'UEFA Champions League': ['Club football competition, Europe', 58],
                                                                   'NASA': ['Space agency, United States', 56],
                                                                'Emma Watson': ['Actress, United Kingdom', 56],
                                                                      'Shawn Mendes': ['Musician, Canada', 57],
                                                                       'Virat Kohli': ['Cricketer, India', 55],
                                                                    'Gigi Hadid': ['Model, United States', 54],
                                                  'Priyanka Chopra Jonas': ['Actress and musician, India', 53],
                                                                  '9GAG': ['Social media platform, China', 52],
                                                                      'Ronaldinho': ['Footballer, Brasil', 51],
                                                                          'Maluma': ['Musician, Colombia', 50],
                                                                      'Camila Cabello': ['Musician, Cuba', 49],
                                                     'NBA': ['Club Basketball Competition, United States', 47]
}

# Start Game
print(logo)
score = 0
game_end = False



def pick_choices(celeb_keys, correct_answer=[]):
    you_win = False
    if correct_answer != []:
        picked_choices = correct_answer
        if celeb_keys == []:
            you_win = True
        else:
            picked_choices.append(random.choice(celeb_keys))
            celeb_keys.remove(picked_choices[1])
            picked_choices[1] = [f"{picked_choices[1]}: {celeb[picked_choices[1]][0]}", celeb[picked_choices[1]][1]]
            you_win = False
    else:
        picked_choices = [random.choice(celeb_keys)]
        celeb_keys.remove(picked_choices[0])
        picked_choices.append(random.choice(celeb_keys))
        celeb_keys.remove(picked_choices[1])
        picked_choices = [[f"{picked_choices[0]}: {celeb[picked_choices[0]][0]}", celeb[picked_choices[0]][1]], [f"{picked_choices[1]}: {celeb[picked_choices[1]][0]}", celeb[picked_choices[1]][1]]]
        you_win = False

    return celeb_keys, picked_choices, you_win

def get_answer(choice, picked_choices, score, game_end):
    if choice == 'A' and picked_choices[0][1] > picked_choices[1][1]:
        score += 1
        picked_choices.pop()
    elif choice == 'A' and picked_choices[0][1] < picked_choices[1][1]:
        game_end = True
    elif choice == 'B' and picked_choices[0][1] < picked_choices[1][1]:
        score += 1
        picked_choices.pop(0)
    elif choice == 'B' and picked_choices[0][1] > picked_choices[1][1]:
        game_end = True
    else:
        print("Sorry invalid input, Game Over.\n")
    
    return(score, game_end)

def new_round(picked_choices, score, game_end):
    print(f"Compare A: {picked_choices[0][0]}")
    print(vs)
    print(f"Compare B: {picked_choices[1][0]}")

    choice = input("Who has more followers? Type 'A' or 'B'.    ")
    score, game_end = get_answer(choice, picked_choices, score, game_end)
    return score, game_end

celeb_keys = [i for i in celeb]
celeb_keys, picked_choices, you_win = pick_choices(celeb_keys)


# First round
score, game_end = new_round(picked_choices, score, game_end)

while(not game_end):
    print(f"You're right! Current Score: {score}\n")
    
    celeb_keys, picked_choices, you_win = pick_choices(celeb_keys, correct_answer=picked_choices)
    if (you_win):
        print("Congratulations, you guessed all choises right!\n")
        break
    score, game_end = new_round(picked_choices, score, game_end)

if(game_end):
    print(f"Sorry, wrong answer. Game Over.\n")


    