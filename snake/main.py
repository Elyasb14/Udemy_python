import turtle
import time
import snake
import food
import scoreboard


# initialize screen and add some properties
screen = turtle.Screen()
screen.setup(height= 600, width = 600)
screen.bgcolor('black')
screen.title("Snake")
screen.tracer(0)

# initialize snake object and food object
snake = snake.Snake()
food = food.Food()

# telling screen to listen for keystrokes
screen.listen()

# methods to use when a key is clicked
screen.onkey(fun = snake.up, key = 'Up')
screen.onkey(fun = snake.left, key = 'Left')
screen.onkey(fun = snake.right, key = 'Right')
screen.onkey(fun = snake.down, key = 'Down')

# boolean to keep track of game status and initialize scoreboard object
game_is_on = True
scoreboard = scoreboard.Scoreboard()

# main while loop
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    # detect collowion with food
    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        food.refresh()
        snake.add_segment()
        
    # detect colosion with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()
        
    # detect tail collision
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


# screen exits on click 
screen.exitonclick()
