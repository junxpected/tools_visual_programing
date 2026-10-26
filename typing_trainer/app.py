from __future__ import annotations
import json
import tkinter as tk
from datetime import datetime
from config import HISTORY_FILE, SETTINGS_FILE, THEMES, UI, WINDOW_MIN_SIZE, FONT_NAV, FONT_NAV_ACTIVE, FONT_LABEL
from help_page import HelpPage
from history import HistoryPage
from settings_page import SettingsPage
from training import TrainingPage
from utils import load_json, save_json

class App(tk.Tk):
    def __init__(self):
        super().__init__(); self.title("TypeFlow"); self.geometry("1200x800"); self.minsize(*WINDOW_MIN_SIZE); self.settings = load_json(SETTINGS_FILE, {"language": "Українська", "theme": "graphite"}); self.language = self.settings.get("language", self.settings.get("ui_language", "Українська")); self.theme = self.settings.get("theme", self.settings.get("palette", "graphite")); self.language = self.language if self.language in UI else "Українська"; self.theme = self.theme if self.theme in THEMES else "graphite"; self.level = "Легкий" if self.language == "Українська" else "Easy"; self.colors = THEMES[self.theme]; self.page_host = tk.Frame(self, bg=self.colors["bg"]); self.fullscreen = True; self.nav = {}; self.build_shell(); self.show_page("training"); self.attributes("-fullscreen", True); self.bind("<F11>", self.toggle_fullscreen); self.bind("<Escape>", self.exit_fullscreen); self.protocol("WM_DELETE_WINDOW", self.on_close)
    def build_shell(self):
        c = self.colors; self.configure(bg=c["bg"]); self.side = tk.Frame(self, bg=c["panel"], width=200); self.side.pack(side="left", fill="y"); self.side.pack_propagate(False); tk.Label(self.side, text="TypeFlow", bg=c["panel"], fg=c["accent"], font=("Inter", 18, "bold")).pack(anchor="w", padx=22, pady=(24, 35))
        for key, text in (("training", "training"), ("history", "history"), ("settings", "settings"), ("help", "help")):
            button = tk.Button(self.side, text=UI[self.language][text], anchor="w", relief="flat", bd=0, bg=c["panel"], fg=c["muted"], activebackground=c.get("accent_dim", c["panel2"]), activeforeground=c["accent"], font=FONT_NAV, command=lambda page=key: self.show_page(page)); button.pack(fill="x", padx=10, pady=2, ipady=8); self.nav[key] = button
        tk.Button(self.side, text=UI[self.language]["fullscreen"], command=self.toggle_fullscreen, relief="flat", bd=0, bg=c["panel"], fg=c["muted"], activebackground=c.get("accent_dim", c["panel2"]), font=FONT_LABEL).pack(side="bottom", anchor="w", padx=18, pady=22)
        self.page_host = tk.Frame(self, bg=c["bg"], padx=38, pady=28); self.page_host.pack(side="left", fill="both", expand=True)
    def show_page(self, name):
        for child in self.page_host.winfo_children(): child.destroy()
        pages = {"training": TrainingPage, "history": HistoryPage, "settings": SettingsPage, "help": HelpPage}; page = pages[name](self); page.pack(fill="both", expand=True)
        for key, button in self.nav.items(): button.configure(bg=self.colors["accent"] if key == name else self.colors["panel"], fg=self.colors["bg"] if key == name else self.colors["muted"], font=FONT_NAV_ACTIVE if key == name else FONT_NAV)
    def apply_preferences(self, language, theme):
        self.language, self.theme = language, theme; self.colors = THEMES[theme]; self.settings.update({"language": language, "theme": theme}); save_json(SETTINGS_FILE, self.settings); self.rebuild(); self.show_page("settings")
    def rebuild(self):
        for child in self.winfo_children(): child.destroy()
        self.nav = {}; self.build_shell()
    def toggle_fullscreen(self, _event=None): self.fullscreen = not self.fullscreen; self.attributes("-fullscreen", self.fullscreen)
    def exit_fullscreen(self, _event=None): self.fullscreen = False; self.attributes("-fullscreen", False)
    def save_result(self, stats):
        records = load_json(HISTORY_FILE, []); records.insert(0, {"date": datetime.now().strftime("%Y-%m-%d %H:%M"), "language": self.language, "level": getattr(self, "level", ""), "wpm": stats["speed"].get(), "accuracy": stats["accuracy"].get().replace("%", ""), "errors": stats["errors"].get()}); save_json(HISTORY_FILE, records[:50])
    def on_close(self): save_json(SETTINGS_FILE, self.settings); self.destroy()
