import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Скільки ти витрачаєш")
window.geometry("450x500")

# Назва товару — приблизна ціна в грн
items = {
    "iPhone 16": 45000,
    "PlayStation 5": 22000,
    "Відпустка в Єгипет": 35000,
    "Ноутбук MacBook Air": 55000,
    "Річна підписка на спортзал": 12000
}

tk.Label(
    window,
    text="Щоденна витрата (кава, таксі, цигарки...):"
).pack(pady=(15, 0))

entry_daily = tk.Entry(window)
entry_daily.pack()

label_month = tk.Label(window, text="За місяць: —")
label_month.pack(pady=(15, 0))

label_year = tk.Label(window, text="За рік: —")
label_year.pack()

label_5years = tk.Label(window, text="За 5 років: —")
label_5years.pack()

tk.Label(
    window,
    text="За ці гроші (5 років) можна купити:"
).pack(pady=(15, 0))

result_box = tk.Listbox(window, width=45, height=8)
result_box.pack(pady=5)


def calculate():
    try:
        daily = float(entry_daily.get())

        if daily < 0:
            messagebox.showerror("Помилка", "Витрата не може бути від'ємною")
            return

        month = daily * 30
        year = daily * 365
        five_years = daily * 365 * 5

        # Виводимо витрати
        label_month.config(text=f"За місяць: {month:.2f} грн")
        label_year.config(text=f"За рік: {year:.2f} грн")
        label_5years.config(text=f"За 5 років: {five_years:.2f} грн")

        # Очищуємо список
        result_box.delete(0, tk.END)

        # Перевіряємо, що можна купити
        found = False

        for item, price in items.items():
            if five_years >= price:
                result_box.insert(
                    tk.END,
                    f"{item} — {price} грн"
                )
                found = True

        if not found:
            result_box.insert(
                tk.END,
                "Поки що нічого зі списку"
            )

    except ValueError:
        messagebox.showerror(
            "Помилка",
            "Введіть число, наприклад 25"
        )


button = tk.Button(
    window,
    text="Розрахувати",
    command=calculate
)
button.pack(pady=10)

window.mainloop()