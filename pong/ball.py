from turtle import Turtle
import random

class Ball(Turtle):
    # initialize attributes 
    def __init__(self):
        super().__init__() 
        self.color("white")
        self.penup()
        self. goto(0, 0)
        self.shape("circle")
        self.x_move = 10
        self.y_move = 10
        self.velocity = 0.1
    
    
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
    
    def bounce_wall(self):
        self.y_move *= -1
        
    def bounde_paddle(self):
        self.x_move *= -1
        self.velocity *= 0.9
    
    def reset_position(self):
        self.goto(0, 0)
        self.velocity = 0.1
        self.x_move *= -1