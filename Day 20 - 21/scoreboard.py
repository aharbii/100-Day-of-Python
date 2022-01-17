from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.goto(x=0, y=270)
        self.penup()
        self.score = 0
        with open("Day 20 - 21/data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if (self.score > self.high_score):
            self.high_score = self.score
            with open("Day 20 - 21/data.txt", mode="w") as data:
                data.write(f"{self.high_score}")

        self.score = 0
        self.update_scoreboard()
    