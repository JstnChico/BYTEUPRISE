import tkinter as tk
from tkinter import messagebox

def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    
    for char in text:
        if char.isalpha():
            shift_amount = shift if mode == 'encrypt' else -shift
            ascii_offset = 65 if char.isupper() else 97
            new_char = chr((ord(char) - ascii_offset + shift_amount) % 26 + ascii_offset)
            result += new_char
        else:
            result += char
    
    return result

def on_encrypt():
    try:
        shift = int(shift_entry.get())
        message = message_entry.get()
        encrypted_message = caesar_cipher(message, shift, 'encrypt')
        result_label.config(text=f"Encrypted Message: {encrypted_message}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Shift value must be an integer.")

def on_decrypt():
    try:
        shift = int(shift_entry.get())
        message = message_entry.get()
        decrypted_message = caesar_cipher(message, shift, 'decrypt')
        result_label.config(text=f"Decrypted Message: {decrypted_message}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Shift value must be an integer.")

# Setting up the main window
root = tk.Tk()
root.title("Caesar Cipher")

# Creating the widgets and setting up the grid layout
message_label = tk.Label(root, text="Enter your message:")
message_label.grid(row=0, column=0, columnspan=2, pady=5)

message_entry = tk.Entry(root, width=50)
message_entry.grid(row=1, column=0, columnspan=2, pady=5)

shift_label = tk.Label(root, text="Enter shift value:")
shift_label.grid(row=2, column=0, columnspan=2, pady=5)

shift_entry = tk.Entry(root, width=10)
shift_entry.grid(row=3, column=0, columnspan=2, pady=5)

encrypt_button = tk.Button(root, text="Encrypt", command=on_encrypt, bg="green", fg="black")
encrypt_button.grid(row=4, column=0, pady=5)

decrypt_button = tk.Button(root, text="Decrypt", command=on_decrypt, bg="orange", fg="black")
decrypt_button.grid(row=4, column=1, pady=5)

result_label = tk.Label(root, text="")
result_label.grid(row=5, column=0, columnspan=2, pady=10)

# Set the columns to have equal weight, which centers the content
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Running the main loop
root.mainloop()