import tkinter as tk

window = tk.Tk()
window.title("Схема залу")
window.geometry("400x420")

ROWS = 5
COLS = 8
SEAT_PRICE = 150  # грн за місце

selected_seats = set()
buttons = {}


def toggle_seat(row, col):
    seat = (row, col)
    btn = buttons[seat]

    if seat in selected_seats:
        selected_seats.remove(seat)
        btn.config(bg="lightgreen")
    else:
        selected_seats.add(seat)
        btn.config(bg="red")

    update_total()


def update_total():
    total = len(selected_seats) * SEAT_PRICE
    label_total.config(text=f"Обрано місць: {len(selected_seats)} | Сума: {total} грн")


frame_hall = tk.Frame(window)
frame_hall.pack(pady=15)

for row in range(ROWS):
    for col in range(COLS):
        btn = tk.Button(
            frame_hall, text=f"{row + 1}-{col + 1}", width=4, bg="lightgreen",
            command=lambda r=row, c=col: toggle_seat(r, c)
        )
        btn.grid(row=row, column=col, padx=2, pady=2)
        buttons[(row, col)] = btn

label_total = tk.Label(window, text="Обрано місць: 0 | Сума: 0 грн", font=("TkDefaultFont", 10, "bold"))
label_total.pack(pady=20)

window.mainloop()