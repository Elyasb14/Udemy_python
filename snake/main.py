import turtle

screen = turtle.Screen()
screen.setup(height= 600, width = 600)
screen.bgcolor('black')
screen.title("Snake")

positions = [(-40, 0), (-20, 0), (0,0)]
segments = []
for position in positions:
    segment = turtle.Turtle('square')
    segment.penup()
    segment.color('white')
    segment.goto(position)
    segments.append(segment)

game_is_on = True   
while game_is_on:
    for seg in segments:
        seg.forward(20)
    
screen.exitonclick()

