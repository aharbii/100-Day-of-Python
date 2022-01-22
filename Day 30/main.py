# FileNotFound
# with open("a_file.txt") as file:
#     file.read()

# try:
#     file = open("Day 30/a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["sdfsdf"])
# except FileNotFoundError:
#     file = open("Day 30/a_file.txt", mode="w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File was closed.")
#     raise TypeError("This is the error that I made up.")

height = float(input("Height: "))
weight = float(input("Weight: "))
if height > 3:
    raise ValueError("Human height should not be over 3 meters.")
    
bmi = weight / height ** 2
print(bmi)

# KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existent_key"]

# IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

# TypeError
# text = "abc"
# print(text + 5)
