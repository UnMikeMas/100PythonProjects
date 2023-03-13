import pandas as pd
import random
from tkinter import *

# Data reading
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data/french_words.csv")
    to_learn = data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
card_shown = {}
# Functions


def next_card():
    global card_shown, flip_timer
    window.after_cancel(flip_timer)
    card_shown = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_text, text=card_shown["French"], fill="black")
    canvas.itemconfig(white_image, image=front_image)
    flip_timer = window.after(3000, func=time_flip)


def learned_word():
    global card_shown, flip_timer
    to_learn.remove(card_shown)
    words_to_learn = pd.DataFrame(to_learn)
    words_to_learn.to_csv("data/words_to_learn.csv", index=False)
    next_card()


def time_flip():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_text, text=card_shown["English"], fill="white")
    canvas.itemconfig(white_image, image=back_image)


# Variables
BACKGROUND_COLOR = "#B1DDC6"

# Ventana
window = Tk()
window.title("FlashCard App")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=time_flip)

# Canvas blanco
canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
white_image = canvas.create_image(400, 263, image=front_image)
card_text = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))

canvas.grid(column=0, row=0, columnspan=2)

# R / W buttons
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=learned_word)
right_button.grid(column=1, row=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

next_card()

window.mainloop()
