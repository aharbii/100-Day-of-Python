import random

numbers = [1, 2, 3]
new_numbers = [(number + 1) for number in numbers]
print(new_numbers)

name = "Angela"
letters_list = [letter for letter in name]
print(letters_list)

new_list = [(number * 2) for number in range(1, 5)]
print(new_list)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if (len(name) < 5)]
print(short_names)

long_names = [name.upper() for name in names if (len(name) > 5)]
print(long_names)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [(number * number) for number in numbers]
print(squared_numbers)

even_numbers = [number for number in numbers if ((number % 2) == 0)]
print(even_numbers)

with open("Day 26/file1.txt") as file1:
    first_numbers = file1.readlines()
    with open("Day 26/file2.txt") as file2:
        second_numbers = file2.readlines()
        result = [int(number.strip()) for number in first_numbers if (
            number in second_numbers)]
        print(result)

student_score = {name: random.randint(50, 100) for name in names}
print(student_score)

passed = {name: score for (name, score) in student_score.items() if score > 60}
print(passed)