import tkinter as tk
from tkinter import messagebox
import winsound

def check_password():
    if entry.get() == 'STANFORD':
        messagebox.showinfo("Success", "Password is correct!")
    else:
        winsound.Beep(1000, 500)  # Frequency 1000 Hz, Duration 500 ms
        messagebox.showerror("Error", "Password is incorrect!")

# Create the main window
root = tk.Tk()
root.title("Password Prompt")

# Create and place the label and entry widget
label = tk.Label(root, text="Enter Password:")
label.pack(pady=10)

entry = tk.Entry(root, show='*')
entry.pack(pady=10)

# Create and place the button widget
button = tk.Button(root, text="Submit", command=check_password)
button.pack(pady=10)

# Run the application
root.mainloop()