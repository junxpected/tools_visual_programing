import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Оцінка викидів CO2")
window.geometry("380x350")

# приблизні коефіцієнти викидів CO2
CO2_PER_TRIP = 2.3        # кг CO2 за одну поїздку на авто (~10 км)
CO2_PER_HOUR_DEVICE = 0.4  # кг CO2 за годину роботи електроприладу

tk.Label(window, text="Кількість поїздок на авто (за тиждень):").pack(pady=(15, 0))
entry_trips = tk.Entry(window)
entry_trips.pack()

tk.Label(window, text="Годин використання електроприладів (за тиждень):").pack(pady=(15, 0))
entry_hours = tk.Entry(window)
entry_hours.pack()

label_result = tk.Label(window, text="", font=("TkDefaultFont", 10, "bold"), justify="left")
label_result.pack(pady=20)


def calculate():
    try:
        trips = float(entry_trips.get().replace(",", "."))
        hours = float(entry_hours.get().replace(",", "."))
    except ValueError:
        messagebox.showerror("Помилка", "Введіть коректні числа")
        return

    if trips < 0 or hours < 0:
        messagebox.showerror("Помилка", "Значення не можуть бути відʼємними")
        return

    co2_trips = trips * CO2_PER_TRIP
    co2_devices = hours * CO2_PER_HOUR_DEVICE
    co2_week = co2_trips + co2_devices
    co2_year = co2_week * 52

    label_result.config(
        text=(
            f"Від поїздок: {co2_trips:.1f} кг CO2/тиждень\n"
            f"Від електроприладів: {co2_devices:.1f} кг CO2/тиждень\n"
            f"Разом за тиждень: {co2_week:.1f} кг CO2\n"
            f"Разом за рік: {co2_year:.1f} кг CO2"
        )
    )


tk.Button(window, text="Порахувати", command=calculate).pack(pady=5)

window.mainloop()