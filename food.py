from random import randint
from turtle import Turtle

class Food(Turtle):
    def __init__(self):
        super().__init__() # we inherit the Turtle class
        self.shape("circle") # make the food circular
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5) # make the food 10px by 10px
        self.color("red")
        self.speed("fastest")
        self.move_food()
    
    def move_food(self):
        rand_x = randint(-280, 280)
        rand_y = randint(-280, 280)
        self.goto(rand_x, rand_y)