with open("Day 24/Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("Day 24/Input/Letters/starting_letter.txt") as starting_letter_file:
    starting_letter = starting_letter_file.read()
    for name in names:
        ready_letter = starting_letter.replace("[name]", name.strip())
        with open(f"Day 24/Output/ReadyToSend/letter_for_{name}.txt", mode="w") as ready:
            ready.write(ready_letter)