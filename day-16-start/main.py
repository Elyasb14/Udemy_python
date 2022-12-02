
'''from turtle import Turtle, Screen


timmy = Turtle()
print(timmy)
timmy.shape('turtle')

my_screen = Screen()

print(my_screen.canvheight)

timmy.color('Green', 'Red')

timmy.forward(100)

my_screen.exitonclick()'''

import prettytable

table = prettytable.PrettyTable()

table.add_column('Pokemon name', ['Pikachu', 'Squirtle', 'Charmander'])
table.add_column('Type', ['electric', 'water', 'fire'])
table.align = 'l'
print(table)