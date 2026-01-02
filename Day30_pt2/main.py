from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

DEFAULT_USERNAME = "murilomatsuora@gmail.com"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)

    print(f"Your password is: {password}")

    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "username": username,
            "password": password
        }
    }

    if website == '' or username == '' or password == '':
        messagebox.showerror(title="Oops", message="All fields must be filled.")
        print("All fields must be filled.")
        return

    data = {}
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            data.update(new_data)
    except FileNotFoundError:
        data = new_data
    finally:
        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)

    website_entry.delete(0, END)
    password_entry.delete(0, END)

# ------------------------- FIND PASSWORD ------------------------------ #
def find_password():
    website = website_entry.get()
    if website == '':
        messagebox.showerror(title="Oops", message="Website field must be filled.")
        print("Website field must be filled.")
        return

    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        print("No Data File Found.")
    else:
        if website in data:
            messagebox.showinfo(title=f"{website} details", message=f"Website: {website}\n"
                                                                 f"Username: {data[website]["username"]}\n"
                                                                 f"Password: {data[website]["password"]}")

        else:
            messagebox.showerror(title="No details found", message=f"No details found for website {website}.")
            print("No details for the website exist")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_lbl = Label(text="Website:")
website_lbl.grid(row=1, column=0)
website_entry = Entry(width=32)
website_entry.grid(row=1, column=1, columnspan=1)
website_entry.focus()

search_btn = Button(text="Search", width=15, command=find_password)
search_btn.grid(row=1, column=2,columnspan=1)

username_lbl = Label(text="Email/Username:")
username_lbl.grid(row=2, column=0)
username_entry = Entry(width=50)
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.insert(0, DEFAULT_USERNAME)

password_lbl = Label(text="Password:")
password_lbl.grid(row=3, column=0)
password_entry = Entry(width=32)
password_entry.grid(row=3, column=1)
generate_password_btn = Button(text="Generate Password", command=generate_password)
generate_password_btn.grid(row=3, column=2)

add_btn = Button(text="Add", width=36, command=save)
add_btn.grid(row=4, column=1,columnspan=2)

window.mainloop()
