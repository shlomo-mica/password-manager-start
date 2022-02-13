import tkinter as tk

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
root = tk.Tk()
root.title("PASSWORD")
root.config(padx=20, pady=20,bg='gray')
canvas = tk.Canvas(root, width=180, height=180, bg="#FFE873")
photo = tk.PhotoImage(file="logo.png")
canvas.create_image(90,90, image=photo)
canvas.grid(column=1, row=0)

add_button = tk.Button(root, text="ADD", bg='pink',width=36)
add_button.grid(column=1, row=4)

Generate_password_button = tk.Button(root, text="Generate Password")

Generate_password_button.config(width=14)
Generate_password_button.grid(column=2,row=3)
# ENTRY LIST
Website_entry = tk.Entry(width=35)
Website_entry.grid(column=1, row=1)

Email_username = tk.Entry(width=35)
Email_username.grid(column=1, row=2)

Password_entry = tk.Entry(width=21)
Password_entry.grid(column=1, row=3)
Password_entry.config()


label_web = tk.Label(text="Website",width=15)
label_web.grid(column=0,row=1)

email_label = tk.Label(text="Email/Username")
email_label.grid(column=0,row=2)

password_label = tk.Label(text="Password")
password_label.grid(column=0,row=3)


# canvas.create_line(80, 77, 340, 77, width=4)
# canvas.create_line(340, 340, 80, 340, width=4)
# canvas.create_line(340, 77, 340, 340, width=4)
# canvas.create_line(80, 340, 80, 77, width=4)


root.mainloop()
