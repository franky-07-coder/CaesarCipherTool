import tkinter as tk
from tkinter import filedialog, messagebox

def caesar_cipher(text, shift, decrypt=False):
    if decrypt:
        shift = -shift
    shift = shift % 26
    result_chars = []
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result_chars.append(chr((ord(ch) - base + shift) % 26 + base))
        else:
            result_chars.append(ch)
    return "".join(result_chars)

def process_text(mode):
    in_text = entry_message.get("1.0", tk.END).strip()
    if not in_text:
        set_status("⚠ No text to process")
        return
    
    try:
        if mode == "Encrypt":
            shift = int(entry_encrypt_shift.get().strip())
        else:  # Decrypt
            shift = int(entry_decrypt_shift.get().strip())
    except ValueError:
        messagebox.showerror("Error", "Shift must be an integer!")
        return

    result = caesar_cipher(in_text, shift, decrypt=(mode == "Decrypt"))
    output.delete("1.0", tk.END)
    output.insert(tk.END, result)
    set_status(f"✅ {mode}ion successful")

def load_file():
    filepath = filedialog.askopenfilename(filetypes=[("Text Files", ".txt"), ("All files", ".*")])
    if filepath:
        with open(filepath, "r", encoding="utf-8") as f:
            entry_message.delete("1.0", tk.END)
            entry_message.insert(tk.END, f.read())
        set_status(f"📂 File loaded: {filepath.split('/')[-1]}")

def save_file():
    filepath = filedialog.asksaveasfilename(defaultextension=".txt",
                                            filetypes=[("Text Files", ".txt"), ("All files", ".*")])
    if filepath:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(output.get("1.0", tk.END).rstrip("\n"))
        set_status(f"💾 File saved: {filepath.split('/')[-1]}")

def copy_output_to_input():
    txt = output.get("1.0", tk.END).strip()
    if not txt:
        set_status("⚠ Output is empty")
        return
    entry_message.delete("1.0", tk.END)
    entry_message.insert(tk.END, txt)
    set_status("➡ Output copied to input")

def set_status(msg):
    status_label.config(text=msg)

def on_close():
    root.destroy()
    try: root.quit()
    except: pass


# ---- GUI ----
root = tk.Tk()
root.title("Caesar Cipher Encoder/Decoder (Dual Shifter)")
root.geometry("950x600")
root.config(bg="#1e1e1e")  # 🌙 Dark background
root.minsize(800, 500)
root.resizable(True, True)

root.protocol("WM_DELETE_WINDOW", on_close)

# Title / Logo
title_label = tk.Label(root, text="🌀 Caesar Cipher Tool (Dual Shifter)",
                       font=("Segoe UI", 24, "bold"),
                       bg="#222831", fg="#00adb5", pady=12)
title_label.pack(fill="x")

# Toolbar
toolbar = tk.Frame(root, bg="#2c2c2c", pady=5)
toolbar.pack(fill="x", padx=5, pady=5)

btn_style = {"font": ("Segoe UI", 11, "bold"), "relief": "flat", "padx": 10, "pady": 5}

tk.Button(toolbar, text="Encrypt", command=lambda: process_text("Encrypt"),
          bg="#27ae60", fg="white", **btn_style).pack(side=tk.LEFT, padx=5)
tk.Button(toolbar, text="Decrypt", command=lambda: process_text("Decrypt"),
          bg="#e74c3c", fg="white", **btn_style).pack(side=tk.LEFT, padx=5)
tk.Button(toolbar, text="Load File", command=load_file,
          bg="#3498db", fg="white", **btn_style).pack(side=tk.LEFT, padx=5)
tk.Button(toolbar, text="Save File", command=save_file,
          bg="#8e44ad", fg="white", **btn_style).pack(side=tk.LEFT, padx=5)
tk.Button(toolbar, text="Copy Output → Input", command=copy_output_to_input,
          bg="#f39c12", fg="white", **btn_style).pack(side=tk.LEFT, padx=5)

# Shifts Section
shift_frame = tk.Frame(root, bg="#1e1e1e")
shift_frame.pack(pady=10)

tk.Label(shift_frame, text="Encrypt Shift:", font=("Segoe UI", 12, "bold"),
         bg="#1e1e1e", fg="white").grid(row=0, column=0, padx=8)
entry_encrypt_shift = tk.Entry(shift_frame, width=6, font=("Segoe UI", 12),
                               bg="#2c2c2c", fg="white", insertbackground="white", relief="solid", bd=1)
entry_encrypt_shift.insert(0, "3")
entry_encrypt_shift.grid(row=0, column=1, padx=8)

tk.Label(shift_frame, text="Decrypt Shift:", font=("Segoe UI", 12, "bold"),
         bg="#1e1e1e", fg="white").grid(row=0, column=2, padx=8)
entry_decrypt_shift = tk.Entry(shift_frame, width=6, font=("Segoe UI", 12),
                               bg="#2c2c2c", fg="white", insertbackground="white", relief="solid", bd=1)
entry_decrypt_shift.insert(0, "3")
entry_decrypt_shift.grid(row=0, column=3, padx=8)

# Input text
entry_message = tk.Text(root, height=8, font=("Segoe UI", 12),
                        bg="#2c2c2c", fg="#f5f5f5", insertbackground="white",
                        relief="solid", bd=2, wrap="word")
entry_message.pack(fill="both", expand=True, padx=15, pady=8)

# Output
output_label = tk.Label(root, text="Output:", font=("Segoe UI", 14, "bold"),
                        bg="#1e1e1e", fg="#00adb5")
output_label.pack(pady=(10, 0))

output = tk.Text(root, height=10, font=("Segoe UI", 12),
                 bg="#2c2c2c", fg="#f5f5f5", insertbackground="white",
                 relief="solid", bd=2, wrap="word")
output.pack(fill="both", expand=True, padx=15, pady=8)

# Status bar
status_label = tk.Label(root, text="Ready", font=("Segoe UI", 10),
                        anchor="w", bg="#222831", fg="#00adb5", relief="sunken", bd=1)
status_label.pack(fill="x", side="bottom")

# Safe mainloop
try:
    root.mainloop()
except KeyboardInterrupt:
    print("Program closed safely.")