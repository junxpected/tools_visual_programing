import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Підбір тарифу")
window.geometry("380x400")

# тарифи, зашиті в код: (назва, ГБ інтернету, хвилини, SMS, ціна)
tariffs = [
    ("Базовий", 5, 100, 50, 150),
    ("Стандарт", 15, 300, 200, 250),
    ("Максимум", 30, 1000, 500, 400),
    ("Безліміт", 100, 5000, 1000, 600),
]

tk.Label(window, text="Обсяг інтернету (ГБ):").pack(pady=(15, 0))
spin_internet = tk.Spinbox(window, from_=0, to=200, increment=1)
spin_internet.pack()

tk.Label(window, text="Хвилини дзвінків:").pack(pady=(15, 0))
spin_minutes = tk.Spinbox(window, from_=0, to=10000, increment=10)
spin_minutes.pack()

tk.Label(window, text="Кількість SMS:").pack(pady=(15, 0))
spin_sms = tk.Spinbox(window, from_=0, to=2000, increment=10)
spin_sms.pack()

label_result = tk.Label(window, text="", font=("TkDefaultFont", 10, "bold"), justify="left")
label_result.pack(pady=25)


def find_tariff():
    try:
        internet = float(spin_internet.get())
        minutes = float(spin_minutes.get())
        sms = float(spin_sms.get())
    except ValueError:
        messagebox.showerror("Помилка", "Введіть коректні значення")
        return

    best = None

    for name, t_internet, t_minutes, t_sms, price in tariffs:
        if internet <= t_internet and minutes <= t_minutes and sms <= t_sms:
            if best is None or price < best[4]:
                best = (name, t_internet, t_minutes, t_sms, price)

    if best is None:
        label_result.config(
            text="Жоден тариф не покриває такі потреби.\nОбери 'Безліміт' або зменш обсяги."
        )
        return

    name, t_internet, t_minutes, t_sms, price = best
    label_result.config(
        text=(
            f"Рекомендований тариф: {name}\n"
            f"Інтернет: {t_internet} ГБ\n"
            f"Хвилини: {t_minutes}\n"
            f"SMS: {t_sms}\n"
            f"Ціна: {price} грн/міс"
        )
    )


tk.Button(window, text="Підібрати тариф", command=find_tariff).pack(pady=10)

window.mainloop()