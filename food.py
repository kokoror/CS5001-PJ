from turtle import Turtle
from random import randint


class Food(Turtle):
    # initialize the food with a random position
    def __init__(self):
        super().__init__() # inherit all properties from turtle class
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color('yellow')
        self.speed('fastest')
        # random_X = randint(-280, 280)
        # random_Y = randint(-280, 280)
        # self.goto(random_X, random_Y)
        # the above code can be replaced as self.move()
        self.move()

    def move(self):
        random_X = randint(-280, 280)
        random_Y = randint(-280, 280)
        self.goto(random_X, random_Y)