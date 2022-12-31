from turtle import Turtle

class Paddle(Turtle):
    # initialize attributes
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid = 5, stretch_len = 1)
        self.penup()
        self.goto(position)
    # method to move paddle up
    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
    # method to move paddle down
    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

