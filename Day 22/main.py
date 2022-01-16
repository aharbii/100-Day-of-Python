""" TODO: 
        [x] Create the screen
        [x] Create and move a paddle
        [x] Create another paddle
        [x] Create the ball and make it move
        [x] Detect collision with wall and bounde
        [] Detect collision with paddle
        [] Detect when baddle misses
        [] Keep score 
"""

from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


# Screen Setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
screen.listen()


# Paddle Setup
r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()

# Paddle Movement
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# Game Console
game_is_on = True

while(game_is_on):
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if (ball.ycor() > 280) or (ball.ycor() < -280):
        ball.bounce_y()

    # Detect collision with paddle
    if ((ball.distance(r_paddle) < 60) and (ball.xcor() > 320)) or ((ball.distance(l_paddle) < 60) and (ball.xcor() < -320)):
        ball.bounce_x()

    # Detect when r_paddle misses
    if ((ball.distance(r_paddle) >= 60) and (ball.xcor() > 320)): 
        ball.reset_position()
        scoreboard.l_point()

    if ((ball.distance(l_paddle) >= 60) and (ball.xcor() < -320)):
        ball.reset_position()
        scoreboard.r_point()

# Quit Game
screen.exitonclick()
