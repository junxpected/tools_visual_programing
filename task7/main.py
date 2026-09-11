import tkinter as tk
from tkinter import ttk, messagebox

window = tk.Tk()
window.title("Облік доходів і витрат")
window.geometry("420x520")

categories = ["Зарплата", "Їжа", "Транспорт", "Розваги", "Комуналка", "Інше"]

operations = []


tk.Label(window, text="Тип:").pack(pady=(10, 0))
combo_type = ttk.Combobox(window, values=["Дохід", "Витрата"], state="readonly")
combo_type.current(0)
combo_type.pack()

tk.Label(window, text="Категорія:").pack(pady=(10, 0))
combo_category = ttk.Combobox(window, values=categories, state="readonly")
combo_category.current(0)
combo_category.pack()

tk.Label(window, text="Сума:").pack(pady=(10, 0))
entry_amount = tk.Entry(window)
entry_amount.pack()


def add_operation():
    op_type = combo_type.get()
    category = combo_category.get()
    try:
        amount = float(entry_amount.get().replace(",", "."))
    except ValueError:
        messagebox.showerror("Помилка", "Введіть коректну суму")
        return

    if amount <= 0:
        messagebox.showerror("Помилка", "Сума має бути більше нуля")
        return

    operations.append((op_type, category, amount))
    entry_amount.delete(0, tk.END)
    refresh_list()


tk.Button(window, text="Додати операцію", command=add_operation).pack(pady=10)

tk.Label(window, text="Фільтр за категорією:").pack(pady=(10, 0))
combo_filter = ttk.Combobox(window, values=["Усі"] + categories, state="readonly")
combo_filter.current(0)
combo_filter.pack()


def refresh_list():
    listbox.delete(0, tk.END)
    filter_value = combo_filter.get()

    for op_type, category, amount in operations:
        if filter_value != "Усі" and category != filter_value:
            continue
        sign = "+" if op_type == "Дохід" else "-"
        listbox.insert(tk.END, f"{op_type} | {category} | {sign}{amount:.2f} грн")

    update_balance()


combo_filter.bind("<<ComboboxSelected>>", lambda e: refresh_list())

listbox = tk.Listbox(window, width=50, height=10)
listbox.pack(pady=10)

label_balance = tk.Label(window, text="Баланс: 0.00 грн", font=("TkDefaultFont", 10, "bold"))
label_balance.pack(pady=10)


def update_balance():
    balance = 0.0
    for op_type, category, amount in operations:
        balance += amount if op_type == "Дохід" else -amount
    label_balance.config(text=f"Баланс: {balance:.2f} грн")


def save_to_file():
    with open("operations.txt", "w", encoding="utf-8") as f:
        for op_type, category, amount in operations:
            f.write(f"{op_type};{category};{amount:.2f}\n")
    messagebox.showinfo("Збережено", "Дані збережено у operations.txt")


tk.Button(window, text="Зберегти у файл", command=save_to_file).pack(pady=5)

window.mainloop()
