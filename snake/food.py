from turtle import Turtle
import random

# make a class Food
class Food(Turtle):
    # initialize attributes
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color('Blue')
        self.speed('fastest')
        self.refresh()
    
    # method to move food to a random place 
    def refresh(self):
        self.goto((random.randint(-280, 280), random.randint(-280, 280)))