import json
import tkinter as tk
from tkinter import messagebox
import pyperclip
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def call_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    # Use list comprehensions for better performance
    list_passwords = [random.choice(letters) for _ in range(nr_letters)]
    list_passwords += [random.choice(symbols) for _ in range(nr_symbols)]
    list_passwords += [random.choice(numbers) for _ in range(nr_numbers)]

    print(list_passwords)
    random.shuffle(list_passwords)

    final_password = "".join(list_passwords)
    return final_password

def generate_password_button_clicked():
    password_entry.delete(0, tk.END)
    finalpassword = call_password()
    pyperclip.copy(finalpassword)
    password_entry.insert(0, finalpassword)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def search_button_clicked():
    website = website_entry.get()
    try:
        with open("data.json", "r") as file:
            data_from_json = json.load(file)
        final_data_of_website = data_from_json[website]
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No data found.")
    except KeyError:
        messagebox.showerror(title="Error", message="Website not found")
    else:
        messagebox.showinfo(title="Success", message=f"Website found!\nEmail: {final_data_of_website['email']}\n"
                                                     f"Password: {final_data_of_website['password']}")
def add_button_clicked():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    data_to_add = {website :{
        "email": email,
        "password": password
    }}
    if password != "" and website != "":
        is_ok = messagebox.askokcancel(title=f"{website}",message=f"These are details entered:\n"
                                                                  f"Email: {email}\nPassword: {password}\nIs it Ok?")
        if is_ok:
            try:
                with open(file="data.json", mode="r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open(file="data.json", mode="w") as data_file:
                    json.dump(data_to_add, data_file, indent=4)
            else:
                data.update(data_to_add)
                with open(file="data.json", mode="w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, tk.END)
                password_entry.delete(0, tk.END)
                website_entry.focus()
    elif password == "":
        messagebox.showinfo(title="Password?!", message="Please enter your password")
    else:
        messagebox.showinfo(title="Oops?!", message="Please enter the details")
# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.minsize(300, 300)
window.config(padx=20, pady=20)

website_text = tk.Label(text="Website:",font=("Georgia",9,"normal"))
website_text.grid(row=1,column=0)

website_entry = tk.Entry(width=33)
website_entry.grid(row=1,column=1)
website_entry.focus()

search_button = tk.Button(text="Search", font=("Georgia",9,"normal"),width=14,command=search_button_clicked)
search_button.grid(row=1,column=2)

email_text = tk.Label(text="Email/Username:",font=("Georgia",9,"normal"))
email_text.grid(row=2,column=0)

email_entry = tk.Entry(width=53)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"madhukiran2k6@gmail.com")

password_text = tk.Label(text="Password:",font=("Georgia",9,"normal"))
password_text.grid(row=3,column=0)

password_entry = tk.Entry(width=33)
password_entry.grid(row=3,column=1)

generatePassword = tk.Button(text="Generate Password",highlightthickness=0,font=("Georgia",9,"normal"),
                             width=14,command=generate_password_button_clicked)
generatePassword.grid(row=3,column=2)

add_button = tk.Button(text="Add",width=40,highlightthickness=0,font=("Georgia",9,"normal"),command=add_button_clicked)
add_button.grid(row=4,column=1,columnspan=2)

password_img = tk.PhotoImage(file="logo.png")
canvas = tk.Canvas(width=200, height=200)
canvas.create_image(100, 105, image=password_img)
canvas.grid(row=0, column=1)

window.mainloop()