import tkinter as tk
from tkinter import messagebox
import random
import string

window = tk.Tk()
window.title("Генератор паролів")
window.geometry("350x350")

tk.Label(window, text="Довжина паролю:").pack(pady=(15, 0))
spin_length = tk.Spinbox(window, from_=4, to=64, increment=1)
spin_length.pack()

var_digits = tk.BooleanVar(value=True)
var_upper = tk.BooleanVar(value=True)
var_special = tk.BooleanVar(value=False)

tk.Checkbutton(window, text="Цифри (0-9)", variable=var_digits).pack(pady=(15, 0), anchor="w", padx=80)
tk.Checkbutton(window, text="Великі літери (A-Z)", variable=var_upper).pack(anchor="w", padx=80)
tk.Checkbutton(window, text="Спецсимволи (!@#$...)", variable=var_special).pack(anchor="w", padx=80)

label_result = tk.Label(window, text="", font=("TkDefaultFont", 12, "bold"))
label_result.pack(pady=25)


def generate_password():
    length = int(spin_length.get())

    chars = string.ascii_lowercase

    if var_upper.get():
        chars += string.ascii_uppercase
    if var_digits.get():
        chars += string.digits
    if var_special.get():
        chars += "!@#$%^&*()_+-="

    password = "".join(random.choice(chars) for _ in range(length))
    label_result.config(text=password)


tk.Button(window, text="Згенерувати пароль", command=generate_password).pack(pady=10)

window.mainloop()