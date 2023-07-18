#Mile to Kilometers Converter Project
from tkinter import *
#function to create miles to kilometer
def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    kilometer_res_label.config(text=f"{km}")
#Creating a new window and configurations
window = Tk()
window.title("Miles to Kilometers Converter")
window.minsize(width=200, height=120)
window.config(padx=20, pady=20)
miles_input = Entry(width=7)
#creating labels
miles_label = Label(text="Miles")
is_equal = Label(text="is equal to")
kilometer_res_label = Label(text="0")
kilometer_label = Label(text="Km")
#Button
calculate = Button(text="Calculate", command=miles_to_km)
#Layout
miles_input.grid(column=1, row=0)
miles_label.grid(column=2, row=0)
is_equal.grid(column=0, row=1)
kilometer_res_label.grid(column=1, row=1)
kilometer_label.grid(column=2, row=1)
calculate.grid(column=1, row=2)