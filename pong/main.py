import turtle
import paddle
import time
import ball
import scoreboard

# initialize a 800x800 screen
screen = turtle.Screen()
screen.setup(width = 800, height = 600)
screen.bgcolor('Black')
screen.title('Pong')
screen.tracer(0)

# create left and right paddles
r_paddle = paddle.Paddle((350, 0))
l_paddle = paddle.Paddle((-350, 0))
ball = ball.Ball()
scoreboard = scoreboard.Scoreboard()

# move paddle up and down with Up and Down arrows
screen.listen()
screen.onkeypress(fun = l_paddle.up, key = 'w')
screen.onkeypress(fun = l_paddle.down, key = 's')
screen.onkeypress(fun = r_paddle.up, key = 'Up')
screen.onkeypress(fun = r_paddle.down, key = 'Down')

# main while loop
game_is_on = True
while game_is_on:
    time.sleep(ball.velocity)
    screen.update()
    ball.move()
    
    # detect collosion with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()
    
    # detect colision with paddles
    if ball.distance(r_paddle) < 60 and ball.xcor() > 325  or ball.distance(l_paddle) < 60 and ball.xcor() < -325:
        ball.bounde_paddle()
    
    
    if ball.xcor() < -380:
        scoreboard.increase_right_score()
        ball.reset_position()
    
    if ball.xcor() > 380:
        scoreboard.increase_left_score()
        ball.reset_position()
        

screen.exitonclick()
