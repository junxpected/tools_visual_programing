import tkinter as tk
from tkinter import ttk, messagebox

window = tk.Tk()
window.title("Розрахунок сну")
window.geometry("350x400")

# норми сну по вікових категоріях (мінімум, максимум) у годинах
sleep_norms = {
    "Дитина (6-12)": (9, 12),
    "Підліток (13-17)": (8, 10),
    "Дорослий (18-64)": (7, 9),
    "Похилий вік (65+)": (7, 8),
}

tk.Label(window, text="Час засинання (год:хв):").pack(pady=(15, 0))
frame_sleep = tk.Frame(window)
frame_sleep.pack()
spin_sleep_hour = tk.Spinbox(frame_sleep, from_=0, to=23, width=3, format="%02.0f")
spin_sleep_hour.pack(side="left")
tk.Label(frame_sleep, text=":").pack(side="left")
spin_sleep_min = tk.Spinbox(frame_sleep, from_=0, to=59, width=3, format="%02.0f")
spin_sleep_min.pack(side="left")

tk.Label(window, text="Час пробудження (год:хв):").pack(pady=(15, 0))
frame_wake = tk.Frame(window)
frame_wake.pack()
spin_wake_hour = tk.Spinbox(frame_wake, from_=0, to=23, width=3, format="%02.0f")
spin_wake_hour.pack(side="left")
tk.Label(frame_wake, text=":").pack(side="left")
spin_wake_min = tk.Spinbox(frame_wake, from_=0, to=59, width=3, format="%02.0f")
spin_wake_min.pack(side="left")

tk.Label(window, text="Вікова категорія:").pack(pady=(15, 0))
combo_age = ttk.Combobox(window, values=list(sleep_norms.keys()), state="readonly")
combo_age.current(2)
combo_age.pack()

label_result = tk.Label(window, text="", font=("TkDefaultFont", 11, "bold"), justify="left")
label_result.pack(pady=25)


def calculate_sleep():
    try:
        sleep_h = int(spin_sleep_hour.get())
        sleep_m = int(spin_sleep_min.get())
        wake_h = int(spin_wake_hour.get())
        wake_m = int(spin_wake_min.get())
    except ValueError:
        messagebox.showerror("Помилка", "Введіть коректний час")
        return

    sleep_minutes_total = sleep_h * 60 + sleep_m
    wake_minutes_total = wake_h * 60 + wake_m

    duration = wake_minutes_total - sleep_minutes_total
    if duration <= 0:
        duration += 24 * 60  # пробудження наступного дня

    duration_hours = duration / 60

    age_category = combo_age.get()
    min_norm, max_norm = sleep_norms[age_category]

    if duration_hours < min_norm:
        verdict = "Недосип"
    elif duration_hours > max_norm:
        verdict = "Пересип"
    else:
        verdict = "Норма"

    label_result.config(
        text=(
            f"Тривалість сну: {duration_hours:.1f} год\n"
            f"Норма для категорії: {min_norm}-{max_norm} год\n"
            f"Висновок: {verdict}"
        )
    )


tk.Button(window, text="Порахувати", command=calculate_sleep).pack(pady=10)

window.mainloop()