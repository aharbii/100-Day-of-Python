MOVE_STEP = 25
WIDTH = 5
LENGTH = 1


from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.shapesize(stretch_wid=WIDTH, stretch_len=LENGTH)
        self.goto(x_pos, y_pos)

    def go_up(self):
        new_y = self.ycor() + MOVE_STEP
        self.goto(self.xcor(), new_y)


    def go_down(self):
        new_y = self.ycor() - MOVE_STEP
        self.goto(self.xcor(), new_y)
