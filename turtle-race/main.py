from turtle import Turtle, Screen
import turtle
import random
is_race_on = False
screen = Screen()
screen.setup(width = 500, height = 400)
user_bet = screen.textinput('Make your bet', 'Which turtle will win: ')
number_of_turtles = int(screen.textinput('How many turtles', 'How many turtles do you want?'))

turtle.colormode(255)

turtle_list = []

for turtle_index in range(0,number_of_turtles):
    new_turtle = Turtle(shape = 'turtle')
    new_turtle.penup()
    new_turtle.color((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    new_turtle.goto(-230, 100 - (int(200 / number_of_turtles) * turtle_index))
    turtle_list.append(new_turtle)

if user_bet:
    is_race_on = True 

while is_race_on:
    for turtle in turtle_list:
        if turtle.xcor() > 230:
            print(turtle.pencolor())
            is_race_on = False
        turtle.forward(random.randint(0, 10))

screen.listen()
screen.exitonclick()
