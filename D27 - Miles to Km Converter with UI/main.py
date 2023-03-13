from tkinter import *


def button_clicked():
    my_label.config(text=my_input.get())


window = Tk()
window.title("My 1st GUI")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# Label

my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label["text"]="My new text"
my_label.config(text="my newest text")
my_label.grid(row=1, column=1)

# Button

my_button = Button(text="Click me", command=button_clicked)
my_button.grid(row=2, column=2)

# Entry

my_input = Entry(width=10)
my_input.grid(row=3, column=4)

# New button

new_button = Button(text="I'm the new button",)
new_button.grid(row=1, column=3)

window.mainloop()
