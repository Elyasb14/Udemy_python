import tkinter

window = tkinter.Tk()
window.title("My first GUI")
window.minsize(width = 500, height = 300)


def button_clicked():
    my_label.config(text = Input.get())

# label
my_label = tkinter.Label(font = ("arial", 24, "bold"))
my_label.config(text = "new text")
my_label.grid(column=0, row=0)


# button
button = tkinter.Button(text = "click me", command = button_clicked)
button.grid(column=1, row=1)

# new button
new_button = tkinter.Button(text = "new button")
new_button.grid(column=2, row=0)

# entry
Input = tkinter.Entry(width = 10)
Input.grid(column=3, row=3)



window.mainloop()
