import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Бюджет підписок")
window.geometry("350x450")

salary = 0.0
total_spent = 0.0

# --- Зарплата ---
tk.Label(window, text="Зарплата:").pack(pady=(10, 0))
entry_salary = tk.Entry(window)
entry_salary.pack()


def set_salary():
    global salary
    try:
        salary = float(entry_salary.get().replace(",", "."))
    except ValueError:
        messagebox.showerror("Помилка", "Введіть коректну суму")
        return
    update_summary()


tk.Button(window, text="Встановити зарплату", command=set_salary).pack(pady=5)

# --- Додавання підписки ---
tk.Label(window, text="Назва підписки:").pack(pady=(10, 0))
entry_name = tk.Entry(window)
entry_name.pack()

tk.Label(window, text="Ціна:").pack(pady=(5, 0))
entry_price = tk.Entry(window)
entry_price.pack()

# --- Список підписок ---
listbox = tk.Listbox(window, width=40)
listbox.pack(pady=10)


def add_subscription():
    global total_spent
    name = entry_name.get().strip()
    try:
        price = float(entry_price.get().replace(",", "."))
    except ValueError:
        messagebox.showerror("Помилка", "Введіть коректну ціну")
        return

    if not name:
        messagebox.showerror("Помилка", "Введіть назву підписки")
        return

    listbox.insert(tk.END, f"{name} — {price:.2f} грн")
    total_spent += price

    entry_name.delete(0, tk.END)
    entry_price.delete(0, tk.END)

    update_summary()


tk.Button(window, text="Додати підписку", command=add_subscription).pack(pady=5)

# --- Підсумок ---
label_total = tk.Label(window, text="Витрати: 0.00 грн")
label_total.pack(pady=(15, 0))

label_remaining = tk.Label(window, text="Залишок: —")
label_remaining.pack()


def update_summary():
    label_total.config(text=f"Витрати: {total_spent:.2f} грн")
    if salary > 0:
        remaining = salary - total_spent
        label_remaining.config(text=f"Залишок: {remaining:.2f} грн")
    else:
        label_remaining.config(text="Залишок: вкажіть зарплату")


window.mainloop()