import random
import colorgram
import turtle

rgb_colors = []
colors = colorgram.extract(
    '/Users/aharbii/Data/Computer Vision/Python/100 Days of Python/Day 18/image.jpg', 30)
for color in colors:
    rgb_colors.append(color.rgb)


def random_color():
    color = random.choice(rgb_colors)
    R = int(color[0])
    G = int(color[1])
    B = int(color[2])
    color = (R, G, B)
    return color


tim = turtle.Turtle()
turtle.colormode(255)
tim.speed("fastest")


def move(col, raw):
    tim.penup()
    tim.hideturtle()
    tim.goto(col, raw)
    tim.pendown()


def draw():
    tim.color(random_color())
    tim.begin_fill()
    tim.circle(10)
    tim.end_fill()


for raw in range(-200, 200, 40):
    for col in range(-200, 200, 40):
        move(col, raw)
        draw()

screen = turtle.Screen()
screen.exitonclick()
