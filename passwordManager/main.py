import tkinter
from tkinter import messagebox
import random
import pyperclip
import random
import json

# ---------------------------- SEARCH ------------------------------------------- #
def search():
    user_entry = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            if user_entry in data:
                messagebox.showinfo(title=f"{website_entry.get()}", message=f"{data[user_entry]}")
            else:
                messagebox.showinfo(title="info", message="No details for website")
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="File does not exist")



# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
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
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="You forgot to fill out all fields")
    else:
        # try and open "data.json" in read mode
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        # if file does not exist, create it, and dump new_data into it
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        # continue try block if no errors are found
        else:
            # update data variable
            data.update(new_data)
            # open data.json and dump the new information into it
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        # delete website and password entry
        finally:
            website_entry.delete(0, "end")
            pass_entry.delete(0, "end")
            
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
website_entry = tkinter.Entry()
website_entry.grid(row=1, column=1)

# email username label
user_label = tkinter.Label(text="Email/Username:")
user_label.grid(row=2, column=0)

# email username entry
user_entry = tkinter.Entry()
user_entry.grid(row=2, column=1, columnspan=2)

# password label
pass_label = tkinter.Label(text="Password:")
pass_label.grid(row=3, column=0)

# password entry
pass_entry = tkinter.Entry()
pass_entry.grid(row=3, column=1)

# generate password button
gen_pass_button = tkinter.Button(text="Generate Password", command=pass_gen)
gen_pass_button.grid(row=3, column=2)

# add button
add_button = tkinter.Button(text="add", command=save)
add_button.grid(row=4, column=1, columnspan=2)

# search button
search_button = tkinter.Button(text="Search", command=search)
search_button.grid(row=1, column=2)



window.mainloop()

