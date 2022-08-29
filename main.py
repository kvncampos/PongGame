# 1. setup screen
# 2. scoreboard
# 3. ball movement
# 4. player movements
# 4a. computer will move up and down if no two player

import time
from turtle import Turtle, Screen
from paddles import Paddle
from paddle2 import Paddle2
from scoreboard import Scoreboard
from ball import Ball

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game v1")

screen.tracer(0)

ball = Ball()
paddle1 = Paddle()
paddle2 = Paddle2()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle1.up, "Up")
screen.onkey(paddle1.down, "Down")

game_is_on = True

# Score Tracker
score = 0
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()
    paddle1.move()
    paddle2.move()

screen.exitonclick()
