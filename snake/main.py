import turtle
import time
import snake
import food
import scoreboard

screen = turtle.Screen()
screen.setup(height= 600, width = 600)
screen.bgcolor('black')
screen.title("Snake")
screen.tracer(0)

snake = snake.Snake()
food = food.Food()

screen.listen()

screen.onkey(fun = snake.up, key = 'Up')
screen.onkey(fun = snake.left, key = 'Left')
screen.onkey(fun = snake.right, key = 'Right')
screen.onkey(fun = snake.down, key = 'Down')
screen.onkey(fun = snake.move, key = 'space')



game_is_on = True

board = scoreboard.Scoreboard()
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    # detect collowion with food
    if snake.head.distance(food) < 15:
        food.refresh()
        board.score += 1
        snake.add_segment()
screen.exitonclick()