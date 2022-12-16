import turtle
import paddle
import time
import puck

# initialize a 800x800 screen
screen = turtle.Screen()
screen.setup(width = 800, height = 800)
screen.bgcolor('Black')
screen.title('Pong')
screen.tracer(0)

# create left and right paddles
left_paddle = paddle.Paddle((-350, 0))
right_paddle = paddle.Paddle((350, 0))

# create puck and tell screen to listen
puck = puck.Puck()

# move paddle up and down with Up and Down arrows
screen.listen()
screen.onkey(fun = left_paddle.up, key = 'w')
screen.onkey(fun = left_paddle.down, key = 's')
screen.onkey(fun = right_paddle.up, key = 'Up')
screen.onkey(fun = right_paddle.down, key = 'Down')

# main while loop
game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()
