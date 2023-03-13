from tkinter import *


def convert_button_clicked():
    km_conversion = float(miles_input.get()) * 1.60934
    km_label.config(text=str(km_conversion))


# Window

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=10, pady=10)

# Km Label

km_label = Label(text="0", font=("Arial", 12))
km_label.grid(row=1, column=1)

# Convert Button

c_button = Button(text="Convert", command=convert_button_clicked)
c_button.grid(row=2, column=1)

# Miles input

miles_input = Entry(width=10)
miles_input.grid(row=0, column=1)

# Miles and Km texts and = text

km_text = Label(text="Km", font=("Arial", 12))
km_text.grid(row=1, column=2)
miles_text = Label(text="Miles", font=("Arial", 12))
equal_text = Label(text="is equal to", font=("Arial", 12))

miles_text.grid(row=0, column=2)
equal_text.grid(row=1, column=0)

window.mainloop()
