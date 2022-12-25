import turtle
import pandas as pd
import time

score = 0

screen = turtle.Screen()
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

print(screen.screensize())

# turn into dataframe
data = pd.read_csv("50_states.csv")

game_is_on = True
while game_is_on:
    screen.title(f"US States Game: {score}/50")
    if score == 50:
            drawing = turtle.Turtle()
            drawing.ht()
            drawing.penup()
            drawing.goto((0, 300))
            drawing.write(arg = "You Win!", align = "Center", font = ("Arial", 24, "normal"))
            for num in [5, 4, 3, 2, 1]:
                count = turtle.Turtle()
                count.ht()
                count.penup()
                count.goto((0, 270))
                count.write(arg = f"{num}", align = "Center", font = ("Arial", 24, "normal"))
                time.sleep(1)
                count.clear()
            game_is_on = False
    else:
        answer_state = screen.textinput(title = "Guess the State" , prompt = "Enter State:")
        if (data["state"] == f"{answer_state}").any():
            score += 1
            state = data[data["state"] == f"{answer_state}"]
            x = int(state["x"])
            y = int(state["y"])
            drawing = turtle.Turtle()
            drawing.hideturtle()
            drawing.penup()
            drawing.goto((x, y))
            drawing.write(arg = f"{answer_state}", move = True)
        else:
            continue


