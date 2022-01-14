from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.color("blue")
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        x_pos = random.randint(-270, 270)
        y_pos = random.randint(-270, 270)
        self.goto(x_pos, y_pos)

    def refresh(self):
        x_pos = random.randint(-270, 270)
        y_pos = random.randint(-270, 270)
        self.goto(x_pos, y_pos)