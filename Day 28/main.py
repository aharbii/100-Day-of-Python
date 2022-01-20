from tkinter import *
import time
import math
# ---------------------------- CONSTANTS ------------------------------- #
BLACK = "#191919"
RED = "#C84B31"
SKIN_TONE = "#ECDBBA"
BLUE = "#2D4263"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
work_done = ""
my_timer = NONE

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps
    global work_done

    reps = 0
    work_done = ""

    window.after_cancel(my_timer)
    timer.config(text="TIMER", fg=BLACK)
    canvas.itemconfig(timer_text, text="00:00")
    check_marks.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    global work_done

    reps += 1
    if (reps % 2):
        timer.config(text="WORK", fg=RED)
        count_down(WORK_MIN * 60)
    elif ((reps % 8) == 0):
        timer.config(text="BREAK", fg=BLUE)
        count_down(LONG_BREAK_MIN * 60)
        work_done += "✔️"
        check_marks.config(text=work_done)
    else:
        timer.config(text="BREAK", fg=BLUE)
        count_down(SHORT_BREAK_MIN * 60)
        work_done += "✔️"
        check_marks.config(text=work_done)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global my_timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_min < 10:
        count_min = f"0{count_min}"
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        my_timer = window.after(1, count_down, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=SKIN_TONE)

# Timer
timer = Label(text="Timer", fg=BLUE,
              font=(FONT_NAME, 50, "bold"), bg=SKIN_TONE)
timer.grid(row=0, column=1)

# Canvas
canvas = Canvas(width=200, height=224, bg=SKIN_TONE, highlightthickness=0)
tomato_img = PhotoImage(file="Day 28/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white",
                                font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# Check Marks
check_marks = Label(text=work_done, fg=BLUE, bg=SKIN_TONE)

check_marks.grid(row=3, column=1)

# Start Button
start_btn = Button(text="Start", highlightthickness=0, command=start_timer)
start_btn.grid(row=2, column=0)

# Reset Buttong
reset_btn = Button(text="Rest", highlightthickness=0, command=reset_timer)
reset_btn.grid(row=2, column=2)

window.mainloop()
