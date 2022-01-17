import turtle
import pandas
FONT = ("Courier", 14, "normal")

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "Day 25/US States Game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

us_states = pandas.read_csv("Day 25/US States Game/50_states.csv")
states = us_states["state"].to_list()
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()
score = 0

while (score < 50):
    valid_answer = 0
    answer_state = screen.textinput(
        title="Guess the State", prompt=f"{score}/50: What's another state's name?")

    if answer_state in states:
        valid_answer = 1
        states.remove(answer_state)

    if answer_state == "Exit":
        break

    if valid_answer:
        state = us_states[us_states.state == answer_state]
        score += 1
        writer.goto(x=int(state.x), y=int(state.y))
        writer.write(f"{answer_state}", align="center", font=FONT)

new_data = pandas.DataFrame(states)
new_data.to_csv("Day 25/US States Game/states_to_learn.csv")

screen.exitonclick()
