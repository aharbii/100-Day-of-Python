from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

def end_game():
    game_is_on = False

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(end_game, "space")


game_is_on = True
while(game_is_on):
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect collision with food.
    if(snake.head.distance(food) < 15):
        scoreboard.increase_score()
        snake.extend()
        food.refresh()

    # Detect collision with wall.
    if(snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280):
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 5:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
