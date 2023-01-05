import tkinter
import pandas as pd
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

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
gen_pass_button = tkinter.Button(text="Generate Password")
gen_pass_button.grid(row=3, column=2)

# add button
add_button = tkinter.Button(text="add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)



window.mainloop()

