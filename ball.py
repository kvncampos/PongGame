from turtle import Turtle
import random


class Ball(Turtle):
    """Food Class with Turtle Properties"""

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color("blue")
        self.speed("normal")
        self.move()

    def move(self):
        """When food is hit, randomly places another"""
        self.setheading(180)
        self.forward(20)
