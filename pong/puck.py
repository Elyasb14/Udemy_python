from turtle import Turtle
import random

class Puck(Turtle):
    # initialize attributes 
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(stretch_wid = 0.5, stretch_len = 0.5)
        self.color('white')
        self.penup()
    # method to have puck move
    def move(self):
        self.setheading(random.randint(0, 360))
        
        
