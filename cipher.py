import tkinter as tk
from tkinter import filedialog, messagebox

def caesar_cipher(text, shift, decrypt=False):
    result = ""
    if decrypt:
        shift = -shift
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def process_text(mode):
    text = entry_message.get("1.0", tk.END).strip()
    shift = entry_shift.get()

    if shift == "":
        messagebox.showerror("Error", "Please enter a shift value!")
        return

    try:
        shift = int(shift)
    except ValueError:
        messagebox.showerror("Error", "Shift must be an integer!")
        return

    result = caesar_cipher(text, shift, decrypt=(mode == "Decrypt"))

    output.delete("1.0", tk.END)
    output.insert(tk.END, result)

def load_file():
    filepath = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if filepath:
        with open(filepath, "r") as f:
            entry_message.delete("1.0", tk.END)
            entry_message.insert(tk.END, f.read())

def save_file():
    filepath = filedialog.asksaveasfilename(defaultextension=".txt",
                                            filetypes=[("Text Files", "*.txt")])
    if filepath:
        with open(filepath, "w") as f:
            f.write(output.get("1.0", tk.END).strip())


root = tk.Tk()
root.title("Caesar Cipher Tool")
root.geometry("700x550")
root.config(bg="#1e1e2f")  # Dark background

title_label = tk.Label(root, text="🔐 Caesar Cipher", font=("Arial", 22, "bold"),
                       bg="#1e1e2f", fg="#ffffff")
title_label.pack(pady=15)


entry_message = tk.Text(root, height=8, width=80, font=("Courier", 12),
                        bg="#2c2c3c", fg="#ffffff", insertbackground="white")
entry_message.pack(pady=10)

shift_frame = tk.Frame(root, bg="#1e1e2f")
shift_frame.pack(pady=5)
tk.Label(shift_frame, text="Shift Value:", font=("Arial", 12),
         bg="#1e1e2f", fg="#ffffff").pack(side=tk.LEFT, padx=5)
entry_shift = tk.Entry(shift_frame, width=10, font=("Arial", 12),
                       bg="#2c2c3c", fg="#ffffff", insertbackground="white")
entry_shift.insert(0, "3")
entry_shift.pack(side=tk.LEFT)


frame = tk.Frame(root, bg="#1e1e2f")
frame.pack(pady=15)

tk.Button(frame, text="Encrypt", command=lambda: process_text("Encrypt"),
          width=14, height=2, bg="#27ae60", fg="white").grid(row=0, column=0, padx=10)
tk.Button(frame, text="Decrypt", command=lambda: process_text("Decrypt"),
          width=14, height=2, bg="#e74c3c", fg="white").grid(row=0, column=1, padx=10)
tk.Button(frame, text="📂 Load File", command=load_file,
          width=14, height=2, bg="#2980b9", fg="white").grid(row=0, column=2, padx=10)
tk.Button(frame, text="💾 Save File", command=save_file,
          width=14, height=2, bg="#8e44ad", fg="white").grid(row=0, column=3, padx=10)


output_label = tk.Label(root, text="Output:", font=("Arial", 14, "bold"),
                        bg="#1e1e2f", fg="#ffffff")
output_label.pack()
output = tk.Text(root, height=10, width=80, font=("Courier", 12),
                 bg="#2c2c3c", fg="#ffffff", insertbackground="white")
output.pack(pady=10)

root.mainloop()
