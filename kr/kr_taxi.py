import tkinter as tk
from tkinter import ttk, messagebox

window = tk.Tk()
window.title("Послуги таксі")
window.geometry("450x600")

label_distance = tk.Label(window, text="Введіть відстань (км):")
label_distance.pack(pady=(15, 0))

enter_distance = tk.Entry(window)
enter_distance.pack()

tarifi = {
    "Економ": (30, 15),
    "Стандарт": (50, 20),
    "Комфорт": (80, 30),
}

label_tarif = tk.Label(window, text="Виберіть тариф:")
label_tarif.pack(pady=(15, 0))

combo_tarif = ttk.Combobox(window, values=list(tarifi.keys()), state="readonly", width=35)  # <-- без tk. спереду
combo_tarif.pack()

var_night = tk.BooleanVar(value=False)
check_night = tk.Checkbutton(window, text="Нічний тариф (+20%)", variable=var_night)
check_night.pack(pady=(15, 0), anchor="w", padx=20)

var_child_seat = tk.BooleanVar(value=False)
check_child_seat = tk.Checkbutton(window, text="Дитяче крісло (+40 грн)", variable=var_child_seat)
check_child_seat.pack(anchor="w", padx=20)


def calculate():
    distance_text = enter_distance.get()

    try:
        distance = float(distance_text)
    except ValueError:
        messagebox.showerror("Помилка", "Введіть коректну відстань (число)")
        return

    if distance < 0:
        messagebox.showerror("Помилка", "Відстань не може бути відʼємною")
        return

    tariff_name = combo_tarif.get()

    if tariff_name == "":
        messagebox.showerror("Помилка", "Оберіть тариф зі списку")
        return

    tariff_values = tarifi[tariff_name]
    base_fare = tariff_values[0]
    price_per_km = tariff_values[1]

    cost = base_fare + distance * price_per_km

    if var_night.get() == True:
        cost = cost * 1.2

    if var_child_seat.get() == True:
        cost = cost + 40

    label_result.config(text=f"Вартість поїздки: {cost:.2f} грн")   


def clear_form():
    enter_distance.delete(0, tk.END)
    combo_tarif.set("")
    var_night.set(False)
    var_child_seat.set(False)
    label_result.config(text="Вартість поїздки: 0.00 грн")


button_calculate = tk.Button(window, text="Розрахувати вартість", command=calculate)
button_calculate.pack(pady=(15, 0))

button_clear = tk.Button(window, text="Очистити", command=clear_form)
button_clear.pack(pady=(10, 0))

label_result = tk.Label(window, text="Вартість поїздки: 0.00 грн")
label_result.pack(pady=(15, 0))

window.mainloop()