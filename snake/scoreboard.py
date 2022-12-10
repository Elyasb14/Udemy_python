from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.scoreboard = Turtle()
        self.score = 3
        self.color('white')
        self.shape('square')
        self.hideturtle()
        self.scoreboard.write(arg = f"Score: {self.score}", move = False)
        