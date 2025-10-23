from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_wid=0.8, stretch_len=0.8)
        self.color("green")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        pos_x = randint(-280, 280)
        pos_y = randint(-280, 280)
        self.goto(pos_x, pos_y)


