import tkinter as tk
from tkinter import ttk
from config import THEMES, UI

class SettingsPage(tk.Frame):
    def __init__(self, app):
        self.app = app; super().__init__(app.page_host, bg=app.colors["bg"]); self.language = tk.StringVar(value=app.language); self.theme = tk.StringVar(value=app.theme); self.build()
    def build(self):
        c = self.app.colors; tk.Label(self, text=UI[self.app.language]["settings"], bg=c["bg"], fg=c["fg"], font=("Inter", 24, "bold")).pack(anchor="w"); tk.Label(self, text="Personalize TypeFlow", bg=c["bg"], fg=c["muted"]).pack(anchor="w", pady=(4, 20)); box = tk.Frame(self, bg=c["panel"], padx=24, pady=22); box.pack(fill="x"); tk.Label(box, text=UI[self.app.language]["language"], bg=c["panel"], fg=c["fg"], font=("Inter", 11, "bold")).pack(anchor="w"); ttk.Combobox(box, textvariable=self.language, values=["Українська", "English"], state="readonly", width=22).pack(anchor="w", pady=(8, 22)); tk.Label(box, text=UI[self.app.language]["palette"], bg=c["panel"], fg=c["fg"], font=("Inter", 11, "bold")).pack(anchor="w"); row = tk.Frame(box, bg=c["panel"]); row.pack(anchor="w", pady=12)
        for name, theme in THEMES.items(): tk.Radiobutton(row, text=name, variable=self.theme, value=name, indicatoron=False, width=10, bg=theme["accent"], fg=theme["bg"], selectcolor=theme["accent"], activebackground=theme["accent"], relief="flat", font=("Inter", 9, "bold")).pack(side="left", padx=(0, 7))
        ttk.Button(box, text=UI[self.app.language]["save"], style="Accent.TButton", command=self.save_settings).pack(anchor="w", pady=(15, 0)); ttk.Button(box, text=UI[self.app.language]["reset"], command=self.reset_to_defaults).pack(anchor="w", pady=(8, 0))
    def save_settings(self): self.app.apply_preferences(self.language.get(), self.theme.get())
    def reset_to_defaults(self): self.language.set("Українська"); self.theme.set("graphite"); self.save_settings()
