from turtle import Turtle

#make a class Scoreboard inheriting data from Turtle
class Scoreboard(Turtle):
    # initialize attributes
    def __init__(self):
        super().__init__()
        self.color('green')
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_scoreboard()
    
    # method to write scoreboard to the screen with updated score
    def update_scoreboard(self):
        self.write(f"{self.left_score}:{self.right_score}", align = 'center', font = ('Courier', 24, 'normal'))
    
    # method to increase score by 1
    def increase_left_score(self):
        self.left_score += 1
        self.clear()
        self.update_scoreboard()
    
    def increase_right_score(self):
        self.right_score += 1
        self.clear()
        self.update_scoreboard()
    
    # method to write GAME OVER to screen
    def game_over(self):
        self.goto(0,0)
        self.color('Red')
        self.write('GAME OVER', align = 'center', font = ('Courier', 24, 'normal'))