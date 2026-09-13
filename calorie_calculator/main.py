import tkinter as tk
from tkinter import ttk, messagebox

window = tk.Tk()
window.title("Калорії за день")
window.geometry("380x450")

total_calories = 0
daily_norm = 2000

# --- Денна норма ---
tk.Label(window, text="Денна норма (ккал):").pack(pady=(15, 0))
entry_norm = tk.Entry(window)
entry_norm.insert(0, "2000")
entry_norm.pack()


def set_norm():
    global daily_norm
    try:
        daily_norm = float(entry_norm.get().replace(",", "."))
    except ValueError:
        messagebox.showerror("Помилка", "Введіть коректне число")
        return
    update_progress()


tk.Button(window, text="Встановити норму", command=set_norm).pack(pady=5)

# --- Додавання прийому їжі ---
tk.Label(window, text="Продукт:").pack(pady=(15, 0))
entry_product = tk.Entry(window)
entry_product.pack()

tk.Label(window, text="Калорійність (ккал):").pack(pady=(10, 0))
entry_calories = tk.Entry(window)
entry_calories.pack()

listbox = tk.Listbox(window, width=45, height=8)
listbox.pack(pady=15)


def add_meal():
    global total_calories
    product = entry_product.get().strip()
    try:
        calories = float(entry_calories.get().replace(",", "."))
    except ValueError:
        messagebox.showerror("Помилка", "Введіть коректну калорійність")
        return

    if not product:
        messagebox.showerror("Помилка", "Введіть назву продукту")
        return

    listbox.insert(tk.END, f"{product} — {calories:.0f} ккал")
    total_calories += calories

    entry_product.delete(0, tk.END)
    entry_calories.delete(0, tk.END)

    update_progress()


tk.Button(window, text="Додати прийом їжі", command=add_meal).pack(pady=5)

# --- Прогрес ---
label_total = tk.Label(window, text="Спожито: 0 / 2000 ккал", font=("TkDefaultFont", 10, "bold"))
label_total.pack(pady=(20, 5))

progress = ttk.Progressbar(window, length=300, maximum=100)
progress.pack()


def update_progress():
    label_total.config(text=f"Спожито: {total_calories:.0f} / {daily_norm:.0f} ккал")

    percent = (total_calories / daily_norm) * 100 if daily_norm > 0 else 0
    progress["value"] = min(percent, 100)


window.mainloop()