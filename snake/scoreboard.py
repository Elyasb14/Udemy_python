from turtle import Turtle

#make a class Scoreboard inheriting data from Turtle
class Scoreboard(Turtle):
    # initialize attributes
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color('green')
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()
    
    # method to write scoreboard to the screen with updated score
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align = 'center', font = ('Courier', 24, 'normal'))
    
    # method to increase score by 1
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
    
    # method to write GAME OVER to screen
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()