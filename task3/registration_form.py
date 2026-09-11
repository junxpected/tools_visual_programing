import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry


class RegistrationForm(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Реєстрація студента")
        self.geometry("400x420")
        self.resizable(False, False)

        self.groups = [
            "ІПЗ-41", "ІПЗ-42", "КН-41", "КІ-41", "СП-41"
        ]

        self._build_ui()

    def _build_ui(self):
        pad = {"padx": 10, "pady": 6}

        # --- ПІБ ---
        tk.Label(self, text="ПІБ:").grid(row=0, column=0, sticky="w", **pad)
        self.entry_name = tk.Entry(self, width=30)
        self.entry_name.grid(row=0, column=1, **pad)

        # --- Дата народження ---
        tk.Label(self, text="Дата народження:").grid(row=1, column=0, sticky="w", **pad)
        self.date_birth = DateEntry(
            self, width=27, date_pattern="dd.mm.yyyy",
            background="darkblue", foreground="white", borderwidth=2
        )
        self.date_birth.grid(row=1, column=1, **pad)

        # --- Група / спеціальність ---
        tk.Label(self, text="Група / спеціальність:").grid(row=2, column=0, sticky="w", **pad)
        self.combo_group = ttk.Combobox(
            self, values=self.groups, state="readonly", width=27
        )
        self.combo_group.grid(row=2, column=1, **pad)

        # --- Стать ---
        tk.Label(self, text="Стать:").grid(row=3, column=0, sticky="w", **pad)
        self.gender_var = tk.StringVar(value="")
        gender_frame = tk.Frame(self)
        gender_frame.grid(row=3, column=1, sticky="w", **pad)
        tk.Radiobutton(gender_frame, text="Чоловіча", variable=self.gender_var,
                        value="Чоловіча").pack(side="left")
        tk.Radiobutton(gender_frame, text="Жіноча", variable=self.gender_var,
                        value="Жіноча").pack(side="left")

        # --- Згода на обробку даних ---
        self.consent_var = tk.BooleanVar(value=False)
        tk.Checkbutton(
            self, text="Згоден(на) на обробку персональних даних",
            variable=self.consent_var, wraplength=350, justify="left"
        ).grid(row=4, column=0, columnspan=2, sticky="w", **pad)

        # --- Кнопка ---
        tk.Button(
            self, text="Зареєструвати", command=self.on_register,
            width=20, bg="#4CAF50", fg="white"
        ).grid(row=5, column=0, columnspan=2, pady=20)

    def on_register(self):
        name = self.entry_name.get().strip()
        group = self.combo_group.get()
        gender = self.gender_var.get()
        consent = self.consent_var.get()
        birth_date = self.date_birth.get_date()

        # --- Валідація ---
        errors = []
        if not name:
            errors.append("Не вказано ПІБ")
        if not group:
            errors.append("Не обрано групу/спеціальність")
        if not gender:
            errors.append("Не обрано стать")
        if not consent:
            errors.append("Не надано згоду на обробку даних")

        if errors:
            messagebox.showerror(
                "Помилка валідації",
                "Виправте наступні поля:\n\n- " + "\n- ".join(errors)
            )
            return

        summary = (
            f"ПІБ: {name}\n"
            f"Дата народження: {birth_date.strftime('%d.%m.%Y')}\n"
            f"Група/спеціальність: {group}\n"
            f"Стать: {gender}\n"
            f"Згода на обробку даних: Так"
        )
        messagebox.showinfo("Реєстрація успішна", summary)


if __name__ == "__main__":
    app = RegistrationForm()
    app.mainloop()