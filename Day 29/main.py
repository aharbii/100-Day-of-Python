import random
from tkinter import *
from tkinter import messagebox
import json

letters_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
                'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers_list = ['1', '2', '4', '5', '6', '7', '8', '9', '0']

symbols_list = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', ',',
                '.', '<', '>', '/', '?', ':', ';', '"', "'", '[', ']', '{', '}', '`', '~']

FONT = ("Arial", 14)

charchters = [letters_list, numbers_list, symbols_list]

letters_required = 6
numbers_required = 6
symbols_required = 4

password_length = letters_required + numbers_required + symbols_required


password = ""
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    global letters_required
    global numbers_required
    global symbols_required
    global password
    global password_length

    password = ""
    letters_required = 6

    numbers_required = 6
    symbols_required = 4

    password_length = letters_required + numbers_required + symbols_required
    for charchter in range(password_length):
        if letters_required > 0:
            if numbers_required > 0:
                if symbols_required > 0:
                    password += random.choice(charchters[random.randint(0, 2)])
                else:
                    password += random.choice(charchters[random.randint(0, 1)])
            else:
                if symbols_required > 0:
                    password += random.choice(
                        charchters[random.randint(-1, 0)])
                else:
                    password += random.choice(charchters[0])
        else:
            if numbers_required > 0:
                if symbols_required > 0:
                    password += random.choice(charchters[random.randint(1, 2)])
                else:
                    password += random.choice(charchters[1])
            else:
                password += random.choice(charchters[-1])

        if password[-1] in numbers_list:
            numbers_required -= 1
        elif password[-1] in symbols_list:
            symbols_required -= 1
        elif password[-1] in letters_list:
            letters_required -= 1
    password_entry.delete(0, "end")
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():

    website = website_entry.get()
    final_password = password_entry.get()
    username = user_name_entry.get()
    email = email_entry.get()

    missing_data = 0

    if (website == "" or website == "Enter website name or URL"):
        messagebox.showwarning(message="Website is required")    
        missing_data = 1
    if (final_password == "" or final_password == "Enter password or click generate password"):
        messagebox.showwarning(message="Password is required")
        missing_data = 1
    if (username == "" or username == "Enter username"):
        messagebox.showwarning(message="Username is required")
        missing_data = 1
    if (not missing_data):
        new_data = {    
                    website: {
                        'Email': email,
                        'Username': username,
                        'Password': final_password
                        }
                    }
        try:
            with open("Day 29/data.json", "r") as data_file:
                # json.dump(new_data, data_file, indent=4)
                data = json.load(data_file)
        except FileNotFoundError:
            with open("Day 29/data.json", 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("Day 29/data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            user_name_entry.delete(0, END)
            
# ---------------------------- Search --------------------------------- #
def search():
    website = website_entry.get()
    if (website == "" or website == "Enter website name or URL"):
        messagebox.showwarning(message="Website is required")
    else:
        try:
            with open("Day 29/data.json", 'r') as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No Data File Found.")
        else:
                if website in data:
                    website_data = data[website]
                    username = website_data["Username"]
                    email = website_data["Email"]
                    password = website_data["Password"]
                    messagebox.showinfo(title=website, message=f"username:{username}\nemail:{email}\npassword:{password}", )
                else:
                    messagebox.showinfo(message=f"There is no saved password for {website}")

# ---------------------------- UI SETUP ------------------------------- #

# Window
window = Tk()
window.title("Password Generator")
window.config(padx=20, pady=20)

# Canvas
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="Day 29/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Website
website_label = Label(text="Website", font=FONT)
website_label.grid(row=1, column=0)

website_entry = Entry(width=21)
website_entry.insert(END, string="Enter website name or URL")
website_entry.grid(row=1, column=1)

search_button = Button(text="Search",
                         command=search, width=10)
search_button.grid(row=1, column=2)

# Username
user_name_label = Label(text="Username", font=FONT)
user_name_label.grid(row=2, column=0)

user_name_entry = Entry(width=35)
user_name_entry.insert(END, string="Enter username")
user_name_entry.grid(row=2, column=1, columnspan=2)

# E-mail
email_label = Label(text="E-mail", font=FONT)
email_label.grid(row=3, column=0)

email_entry = Entry(width=35)
email_entry.insert(END, string="ahmed.harbi.eg@gmail.com")
email_entry.grid(row=3, column=1, columnspan=2)

# Password
password_label = Label(text="Password", font=FONT)
password_label.grid(row=4, column=0)

password_entry = Entry(width=21)
password_entry.insert(END, string="Enter password or click generate password")
password_entry.grid(row=4, column=1)

password_button = Button(text="Generate Password",
                         command=generate_password, width=10)
password_button.grid(row=4, column=2)

# Add 
add_button = Button(text="Add", command=save_data, width=32)
add_button.grid(row=5, column=1, columnspan=2)


window.mainloop()
