from tkinter import *


def calculate():
    miles = int(input.get())
    km = miles * 1.6
    result.config(text=f"{km}")


window = Tk()
window.title("Mile to Km converter")
window.minsize(width=300, height=150)


# Entry Box
input = Entry(width=10)
input.grid(column=1, row=0)

# Label
miles_label = Label(text="Miles", font=("Arial", 24, "bold"))
miles_label.grid(column=2, row=0)

# Is Equal
is_equal = Label(text="is equal to", font=("Arial", 24, "bold"))
is_equal.grid(column=0, row=1)

# Result
result = Label(text="0", font=("Arial", 24, "bold"))
result.grid(column=1, row=1)

# Km
km_label = Label(text="KM", font=("Arial", 24, "bold"))
km_label.grid(column=2, row=1)

# Button
button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

window.mainloop()
