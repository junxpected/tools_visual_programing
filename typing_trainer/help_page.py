import tkinter as tk
from config import UI

class HelpPage(tk.Frame):
    def __init__(self, app):
        super().__init__(app.page_host, bg=app.colors["bg"]); c = app.colors; lang = app.language; tk.Label(self, text=UI[lang]["help"], bg=c["bg"], fg=c["fg"], font=("Inter", 24, "bold")).pack(anchor="w"); tk.Label(self, text="TypeFlow — typing practice", bg=c["bg"], fg=c["muted"]).pack(anchor="w", pady=(4, 20))
        for number, heading, text in (("01", "Start", "Choose language and difficulty, then press Start or type the first character."), ("02", "Accuracy", "Correct characters become green, mistakes become red, and the next character is underlined."), ("03", "WPM", "WPM is calculated from correct five-character groups per minute."), ("04", "Fullscreen", "Press F11 to enter fullscreen and Escape to leave it.")):
            box = tk.Frame(self, bg=c["panel"], padx=20, pady=15); box.pack(fill="x", pady=5); tk.Label(box, text=f"{number}  {heading}", bg=c["panel"], fg=c["accent"], font=("Inter", 11, "bold")).pack(anchor="w"); tk.Label(box, text=text, bg=c["panel"], fg=c["muted"], font=("Inter", 10)).pack(anchor="w", pady=(6, 0))
