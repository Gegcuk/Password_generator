from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #


windows = Tk()
windows.title("Password manager")
windows.config(pady=20, padx=20)


canvas = Canvas(width=200, height=200)
photo_image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=photo_image)
canvas.grid(column=1, row=0)

website_label = Label(text='Website:', padx=5, pady=5)
username_label = Label(text='Username: ', padx=5, pady=5)
password_label = Label(text='Password: ', pady=5)

website_label.grid(column=0, row=1)
username_label.grid(column=0, row=2)
password_label.grid(column=0, row=3)

website_entry = Entry(width=55)
username_entry = Entry(width=55)
password_entry = Entry(width=35)

website_entry.grid(row=1, column=1, columnspan=2)
username_entry.grid(row=2, column=1, columnspan=2)
password_entry.grid(row=3, column=1)

generate_button = Button(text='Generate password', width=15)
add_button = Button(text='Add', width=46, padx=5, pady=5)

generate_button.grid(column=2, row=3)
add_button.grid(row=4, column=1, columnspan=2)





windows.mainloop()
