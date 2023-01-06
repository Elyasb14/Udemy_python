import tkinter
import pandas as pd
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
import random
def pass_gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)


    letter_list = [random.choice(letters) for char in range(nr_letters)]
    symbol_list = [random.choice(symbols) for char in range(nr_symbols)]
    number_list = [random.choice(numbers) for char in range(nr_numbers)]
    password = letter_list + symbol_list + number_list
    random.shuffle(password)
    pass_string = "".join(password)
    pass_entry.insert(0, pass_string)
    pyperclip.copy(pass_string)



# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    website = website_entry.get()
    email = user_entry.get()
    password = pass_entry.get()
    
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="You forgot to fill out all fields")
        return

    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \n is it ok to save?")

    if is_ok:
        with open("data.txt", "a") as data:
            data.write(f"\n{website} | {email} | {password}")
        website_entry.delete(0, 'end')
        pass_entry.delete(0, 'end')

# ---------------------------- UI SETUP ------------------------------- #

# window
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# canvas
canvas = tkinter.Canvas(width=250, height=200)
logo_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# website label
website_label = tkinter.Label(text="Website:")
website_label.grid(row=1, column=0)

# website entry
website_entry = tkinter.Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)

# email username label
user_label = tkinter.Label(text="Email/Username:")
user_label.grid(row=2, column=0)

# email username entry
user_entry = tkinter.Entry(width=35)
user_entry.grid(row=2, column=1, columnspan=2)

# password label
pass_label = tkinter.Label(text="Password:")
pass_label.grid(row=3, column=0)

# password entry
pass_entry = tkinter.Entry(width=21)
pass_entry.grid(row=3, column=1)

# generate password button
gen_pass_button = tkinter.Button(text="Generate Password", command=pass_gen)
gen_pass_button.grid(row=3, column=2)

# add button
add_button = tkinter.Button(text="add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)



window.mainloop()

