from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
from pyperclip import copy
import json
commonly_used_email = "miguelgaona714@gmail.com"

# ---------------------------- SEARCH BUTTON------------------------------------- #


def search():
    website = website_input.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title='No file found', message="No data file found, add first some credentials")
    else:
        if website in data:
            messagebox.showinfo(title=website, message=f"Email: {data[website]['email']}\nPassword: {data[website]['password']}")
        elif website == "":
            messagebox.showinfo(title='Add something to search', message="Type a website to search its credentials")
        else:
            messagebox.showinfo(title='Sorry', message=f"No credentials for {website} were found, please add them")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def password_generate():
    password_input.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters_list = [choice(letters) for _ in range(randint(8, 10))]
    symbols_list = [choice(symbols) for _ in range(randint(2, 4))]
    numbers_list = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = letters_list + symbols_list + numbers_list
    shuffle(password_list)
    password = "".join(password_list)
    password_input.insert(0, password)
    copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():

    new_data = {website_input.get(): {
        "email": email_input.get(),
        "password": password_input.get(),
    }}
    if website_input.get() == "" or email_input.get() == "" or password_input.get() == "":
        messagebox.showinfo(title="Oops", message="Don't leave any fields empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            if website_input.get() in data:
                data[website_input.get()]['email'] = email_input.get()
                data[website_input.get()]['password'] = password_input.get()
                messagebox.showinfo(title="Success", message="Your Password has been securely changed!")
            else:
                messagebox.showinfo(title="Success", message="Your Password has been securely added!")
                data.update(new_data)
            with open("data.json", "w") as data_file:
                # Rewriting updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            email_input.delete(0, END)
            email_input.insert(0, commonly_used_email)
            password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# INPUTS

website_input = Entry(width=21)
website_input.grid(row=1, column=1)
website_input.focus()

email_input = Entry(width=36)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, commonly_used_email)

password_input = Entry(width=21)
password_input.grid(row=3, column=1)

# BUTTONS

generate_button = Button(text="Generate Password", highlightthickness=3, command=password_generate)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", highlightthickness=3, width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", highlightthickness=3, width=14, command=search)
search_button.grid(row=1, column=2)

# TEXTS

website_text = Label(text="Website: ", font=("Arial", 12, "bold"))
website_text.grid(row=1, column=0)

email_text = Label(text="Email/Username: ", font=("Arial", 12, "bold"))
email_text.grid(row=2, column=0)

password_text = Label(text="Password: ", font=("Arial", 12, "bold"))
password_text.grid(row=3, column=0)


window.mainloop()

# Ahora faltaria solamente hacer que lo encuentre en minuscula o mayuscula full
