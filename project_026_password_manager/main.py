from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
from password_letters import letters, symbols, numbers
import pyperclip

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
    
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered : \nEmail : {email_username} " f"\nPassword : {password} \nIs it ok to save?")
        
        if is_ok:
            with open("data.txt", mode="a") as data:
                data.write(f"{website} | {email_username} | {password}\n")
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
website_input = Entry(width=38)
website_input.grid(column=1, row=1, columnspan=2)
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






window.mainloop()