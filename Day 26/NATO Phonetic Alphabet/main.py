import pandas

nato_df = pandas.read_csv("Day 26/NATO Phonetic Alphabet/nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}

def generate_phonetic():
    name = input("Enter your name: ")
    try:
        name_phonetic = {letter:nato_dict[letter.upper()] for letter in name if (letter != " ")}
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(name_phonetic)

generate_phonetic()
