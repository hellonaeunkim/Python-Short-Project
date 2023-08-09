from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
from password_letters import letters, symbols, numbers
import pyperclip
import json

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    search_website = website_input.get()
    
    try:
        with open("data.json", "r") as data_file:
            # Reading old data
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="No Data File Found")
    except json.decoder.JSONDecodeError:
        messagebox.showinfo(title="Oops", message="No Data File Found")
    else:
        if search_website in data:
            email = data[search_website]["email"]
            password = data[search_website]["password"]
            messagebox.showinfo(title=f"{search_website}", message=f"Email : {email}\nPassword : {password}")
        else:
            messagebox.showinfo(title="Oops", message=f"No details for the {search_website} exists")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_input.delete(0, END)
    
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    
    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)
    
    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)
    
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_input.get()
    email_username = email_username_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email_username,
            "password": password,
        }
    }
    
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                #Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        except json.decoder.JSONDecodeError:
            with open('data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)
            
            with open("data.json", "w") as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)
            
        

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

#Labels
website_text = Label(text="Website:")
website_text.grid(column=0, row=1)
email_username_text = Label(text="Email/Username:")
email_username_text.grid(column=0, row=2)
password_text = Label(text="Password:")
password_text.grid(column=0, row=3)

#Entries
website_input = Entry(width=21)
website_input.grid(column=1, row=1)
website_input.focus()
email_username_input = Entry(width=38)
email_username_input.grid(column=1, row=2, columnspan=2)
email_username_input.insert(0, "hellonaeunkim@gmail.com")
password_input = Entry(width=21)
password_input.grid(column=1, row=3)

#Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)
add_button = Button(text="Add", command=save_password, width=36)
add_button.grid(column=1, row=4, columnspan=2)
search_button = Button(text="Search", command=find_password, width=13)
search_button.grid(column=2, row=1)






window.mainloop()