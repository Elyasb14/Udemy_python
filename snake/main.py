import turtle
import time
import snake

screen = turtle.Screen()
screen.setup(height= 600, width = 600)
screen.bgcolor('black')
screen.title("Snake")
screen.tracer(0)

snake = snake.Snake()

screen.listen()

screen.onkey(fun = snake.up, key = 'Up')
screen.onkey(fun = snake.left, key = 'Left')
screen.onkey(fun = snake.right, key = 'Right')
screen.onkey(fun = snake.down, key = 'Down')
screen.onkey(fun = snake.move, key = 'space')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
screen.exitonclick()