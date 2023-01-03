import tkinter

window = tkinter.Tk()
window.title("Miles to Kilometers")
window.config(padx=20, pady=20)

def button_clicked():
    km_value.config(text=float(miles_entry.get()) * 1.609)

# miles entry
miles_entry = tkinter.Entry(width=10)
miles_entry.grid(column=1, row=1)

# calculate button
calculate_button = tkinter.Button(text="Calculate", command=button_clicked)
calculate_button.grid(column=1, row=3)

# miles label
miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=2, row=1)

# is equal to label
equal_label = tkinter.Label(text="is equal to")
equal_label.grid(column=0, row=2)

# km value
km_value = tkinter.Label(text=0)
km_value.grid(column=1, row=2)

# km label
km_label = tkinter.Label(text="Km")
km_label.grid(column=2, row=2)


window.mainloop()