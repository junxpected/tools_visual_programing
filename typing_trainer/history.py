import tkinter as tk
from tkinter import ttk
from config import HISTORY_FILE, UI
from utils import load_json, save_json

class HistoryPage(tk.Frame):
    def __init__(self, app):
        self.app = app; super().__init__(app.page_host, bg=app.colors["bg"]); self.build()
    def build(self):
        c = self.app.colors; tk.Label(self, text=UI[self.app.language]["history"], bg=c["bg"], fg=c["fg"], font=("Inter", 24, "bold")).pack(anchor="w"); tk.Label(self, text="Your recent practice sessions", bg=c["bg"], fg=c["muted"]).pack(anchor="w", pady=(4, 20)); self.table = ttk.Treeview(self, columns=("date", "language", "level", "wpm", "accuracy", "errors"), show="headings")
        for key, title in zip(("date", "language", "level", "wpm", "accuracy", "errors"), ("Date", "Language", "Level", "WPM", "%", "Errors")): self.table.heading(key, text=title); self.table.column(key, width=130)
        self.table.pack(fill="both", expand=True); ttk.Button(self, text="Clear history", command=self.clear_history).pack(anchor="w", pady=12); self.refresh_table()
    def refresh_table(self):
        for item in self.table.get_children(): self.table.delete(item)
        for row in load_json(HISTORY_FILE, []): self.table.insert("", "end", values=(row.get("date", ""), row.get("language", ""), row.get("level", ""), row.get("wpm", 0), f"{row.get('accuracy', 0)}%", row.get("errors", 0)))
    def clear_history(self): save_json(HISTORY_FILE, []); self.refresh_table()
