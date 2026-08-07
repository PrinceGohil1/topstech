#Build a simple login form using Tkinter with two labels and two entry fields for 'Username' and 'Password', and a 'Login' button. When the button is clicked, display a message below saying 'Login Successful' if both fields are non-empty.<br><br><em><strong>Hint:</strong> Use the get() method of Entry widgets to read the input values.</em>

# 4.Build a simple login form using Tkinter with two labels and two entry fields for 'Username' and 'Password', and a 'Login' button. When the button is clicked, display a message below saying 'Login Successful' if both fields are non-empty.<br><br><em><strong>Hint:</strong> Use the get() method of Entry widgets to read the input values.</em>

import tkinter as tk

root = tk.Tk()
root.title("Login Form")
root.geometry("350x200")

username_label = tk.Label(root, text="Username")
username_label.grid(row=0, column=0, padx=10, pady=10)

username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=10, pady=10)

password_label = tk.Label(root, text="Password")
password_label.grid(row=1, column=0, padx=10, pady=10)

password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=10)

message_label = tk.Label(root, text="")
message_label.grid(row=3, column=0, columnspan=2, pady=10)

def login():
    username = username_entry.get()
    password = password_entry.get()

    if username != "" and password != "":
        message_label.config(text="Login Successful")
    else:
        message_label.config(text="Please fill all fields")

login_button = tk.Button(root, text="Login", command=login)
login_button.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()