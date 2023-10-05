import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


# Function to check login credentials
def check_login():
    username = username_entry.get()
    password = password_entry.get()

    # Replace this with your actual authentication logic
    if username == "your_username" and password == "your_password":
        messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")


# Create the main window
root = tk.Tk()
root.title("Modern Login")
root.geometry("400x300")  # Set window size

# Use the 'ttkthemes' library to apply a dark theme
style = ttk.Style()
style.theme_use("clam")

# Increase the font size
style.configure("TLabel", font=("Helvetica", 16))
style.configure("TEntry", font=("Helvetica", 16))

# Add padding to labels and entry fields
style.configure("TLabel", padding=10)
style.configure("TEntry", padding=10)

# Create and place labels with a dark blue background
username_label = ttk.Label(root, text="Username:", style="TLabel")
username_label.pack()

password_label = ttk.Label(root, text="Password:", style="TLabel")
password_label.pack()

# Create and place entry fields
username_entry = ttk.Entry(root, style="TEntry")
username_entry.pack()

password_entry = ttk.Entry(root, show="*", style="TEntry")  # Show asterisks for password
password_entry.pack()

# Create and place login button
login_button = ttk.Button(root, text="Login", command=check_login, style="TButton")
login_button.pack()

# Start the Tkinter main loop
root.mainloop()
