import turtle
import random


timmy = turtle.Turtle()
timmy.shape('turtle')
turtle.colormode(255)

'''
for _ in range(4):
    timmy.forward(100)
    timmy.left(90)
'''

'''
for _ in range(15):
    timmy.forward(10)
    timmy.pu()
    timmy.forward(10)
    timmy.pd()
'''

'''
def draw_polygon(sides, timmy):
    for _ in range(sides):
        timmy.forward(30)
        timmy.left(360 / sides)
 '''       
        
'''        
for i in range(3, 11):
    red = random.randint(0,255)
    blue = random.randint(0,255)
    green = random.randint(0, 255)
    timmy.pencolor(red, blue, green)
    draw_polygon(i, timmy)
'''

'''
timmy.speed(10)
timmy.pensize(15)
while True:
    red = random.randint(0,255)
    blue = random.randint(0,255)
    green = random.randint(0, 255)
    timmy.color((red, blue, green))
    direction = random.choice([0, 90, 180, 270, 360])
    timmy.setheading(direction)
    timmy.forward(20)
'''

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color
timmy.speed(100000)
def draw_graph(size_of_gap, timmy):
    for i in range(int(360 / size_of_gap)):
        timmy.color(random_color())
        heading = timmy.heading()
        timmy.setheading(heading + size_of_gap)
        timmy.circle(100)

draw_graph(5, timmy)


screen = turtle.Screen()
screen.exitonclick()

