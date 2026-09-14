import tkinter as tk


window = tk.Tk()
window.title("Times Devices")
window.geometry("400x300")

label_hours = tk.Label(window, text="Скільки годин в день ти сидиш в телефоні?:")
label_hours.pack(pady=10)

entry_hours = tk.Entry(window)
entry_hours.pack()

def calculate():
    try:
        hours_per_day = float(entry_hours.get())
    except ValueError:
        label_result.config(text="Введіть коректне число!")
        return
        
    hours_per_week = hours_per_day * 7
    hours_per_year = hours_per_day * 365
    
    
    warning = " "
    if hours_per_day > 10:
        warning = "\n\n АГОВ! Ти проводиш забагато часу в телефоні!"
    label_result.config(
        text=f"За тиждень: {hours_per_week:.1f} год\nЗа рік: {hours_per_year:.1f} год{warning}"
    )


button_calc = tk.Button(window, text="Порахувати", command=calculate)
button_calc.pack(pady=15)

label_result = tk.Label(window, text="", justify="left")
label_result.pack(pady=15)


window.mainloop()