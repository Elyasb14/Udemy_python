BACKGROUND_COLOR = "#B1DDC6"
import pandas as pd
import time 
import tkinter


# --------------------------------------------- UI -------------------------------------------- #

# create window
window = tkinter.Tk()
window.title("Flash Card App")
window.config(width=2000, height=2000, padx=50, pady=50, bg=BACKGROUND_COLOR)

# create canvas
# canvas
canvas = tkinter.Canvas(width=800, height=526)
logo_img = tkinter.PhotoImage(file="images/card_front.png")
canvas.create_image(800/2, 526/2, image=logo_img)
canvas.grid(row=0, column=0, columnspan=2)

# right button
right_img = tkinter.PhotoImage(file="images/right.png")
right_button = tkinter.Button(image=right_img, highlightthickness=0)
right_button.grid(row=1, column=1)

# left button
wrong_img = tkinter.PhotoImage(file="images/wrong.png")
wrong_button = tkinter.Button(image=wrong_img, highlightthickness=0)
wrong_button.grid(row=1, column=0)

# language label
lang_label = tkinter.Label(text="LANG", ("Ariel", 40, "italic")).place(x = 400, y = 150)

# word label
word_label = tkinter.Label(text="word", fg="white").place(x = 400, y = 263)







window.mainloop()