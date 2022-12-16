from turtle import Turtle

class Paddle(Turtle):
    # initialize attributes
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_len = 5, stretch_wid = 1)
        self.color('white')
        self.penup()
        self.starting_position = self.goto(position)
        self.setheading(90)
    # method to move paddle up
    def up(self):
        self.goto(self.xcor(), self.ycor() + 20)
    # method to move paddle down
    def down(self):
        self.goto(self.xcor(), self.ycor() - 20)

