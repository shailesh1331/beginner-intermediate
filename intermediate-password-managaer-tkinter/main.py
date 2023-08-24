# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project

from tkinter import *
import csv

def clear_entry():
    password_output.delete(0, END)

def generate_password():
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(4, 6)
    nr_symbols = random.randint(2, 3)
    nr_numbers = random.randint(2, 3)

    password = []
    for x in range(0, nr_numbers):
        password.append(random.choice(numbers))
    for x in range(0, nr_letters):
        password.append(random.choice(letters))
    for x in range(0, nr_symbols):
        password.append(random.choice(symbols))
    random.shuffle(password)
    new_password = "".join(password)
    clear_entry()
    password_output.insert(0, new_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website_text = website_entry.get()
    username_text = username_entry.get()
    password_text = password_output.get()

    with open('password_data.csv', mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['Website', 'Username', 'Password'])
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow({
            'Website': website_text,
            'Username': username_text,
            'Password': password_text
        })

    website_entry.delete(0, END)
    password_output.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

FONT_NAME = "Courier"

window = Tk()
window.config(padx=20, pady=20)

canvas = Canvas()
image = PhotoImage(file='logo.png')
canvas.create_image(170, 100, image=image)
canvas.grid(column=1, row=0)

website = Label(text="Website:", font=(FONT_NAME, 10, 'bold'))
website.grid(column=0, row=1)

email_username = Label(text="Email/Username:", font=(FONT_NAME, 10, 'bold'))
email_username.grid(column=0, row=2)

password = Label(text="Password", font=(FONT_NAME, 10, 'bold'))
password.grid(column=0, row=3)

generate_button = Button(text='Generate', command=generate_password, width=15)
generate_button.grid(column=3, row=3)

add_button = Button(text='Add', width=35, command=save_password)
add_button.grid(column=1, row=4, columnspan=1)

website_entry = Entry(width=35)
website_entry.grid(columnspan=2, column=1, row=1)

username_entry = Entry(width=35)
username_entry.grid(columnspan=2, column=1, row=2)

password_output = Entry(width=21)
password_output.grid(columnspan=1, column=1, row=3)

window.mainloop()
