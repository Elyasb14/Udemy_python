import turtle
import pandas as pd
import time

'''
TO DO:
    - make it so the turtle doesn't flash every time its created
'''

score = 0
guessed_states = []

# initialize screen
screen = turtle.Screen()
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# turn into dataframe
data = pd.read_csv("50_states.csv")
print(type(data))
# conditional for game
game_is_on = True
while game_is_on:
    screen.title(f"US States Game: {score}/50")
    
    # check if you've won the game
    if score == 50:
            # print you win on the screen
            drawing = turtle.Turtle()
            drawing.ht()
            drawing.penup()
            drawing.goto((0, 300))
            drawing.write(arg = "You Win!", align = "Center", font = ("Arial", 24, "normal"))
            # Do a countdown til screen exits
            for num in [5, 4, 3, 2, 1]:
                count = turtle.Turtle()
                count.ht()
                count.penup()
                count.goto((0, 270))
                count.write(arg = f"{num}", align = "Center", font = ("Arial", 24, "normal"))
                time.sleep(1)
                count.clear()
            # end game 
            game_is_on = False
    # if haven't won game, keep asking for inputs
    else:
        # prompt input
        answer_state = screen.textinput(title = "Guess the State" , prompt = "Enter State:")
        # check if user wants to exit and write remaining states to a csv
        if answer_state == "exit":
            remaining_states = [state for state in data["state"] if state not in guessed_states]
            data_df = pd.DataFrame(remaining_states)
            data_df.to_csv("remaining_states.csv")
            game_is_on = False
        # check if input is a state
        if (data["state"] == f"{answer_state}").any():
            guessed_states.append(answer_state)
            score += 1
            state = data[data["state"] == f"{answer_state}"]
            x = int(state["x"])
            y = int(state["y"])
            drawing = turtle.Turtle()
            drawing.hideturtle()
            drawing.penup()
            drawing.goto((x, y))
            drawing.write(arg = f"{answer_state}", move = True)
        # if not, continue
        else:
            continue    