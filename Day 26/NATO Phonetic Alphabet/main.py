import pandas

nato_df = pandas.read_csv("Day 26/NATO Phonetic Alphabet/nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}

name = input("Enter your name: ")

name_phonetic = {letter:nato_dict[letter.upper()] for letter in name if (letter != " ")}
print(name_phonetic)
