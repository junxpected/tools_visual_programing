from __future__ import annotations
import tkinter as tk
from config import FONT_KEY

class VirtualKeyboard(tk.Canvas):
    def __init__(self, master, colors, **kwargs):
        super().__init__(master, height=150, highlightthickness=0, bg=colors["panel"], **kwargs); self.colors = colors; self.layout = []; self.key_items = {}; self.bind("<Configure>", self.on_resize)
    def draw_keyboard(self, layout):
        self.layout = layout; self.delete("all"); self.key_items.clear(); width = max(self.winfo_width(), 600); key_w = min(52, max(30, (width - 60) / max(map(len, layout)) - 5)); x0 = (width - max(map(len, layout)) * (key_w + 5)) / 2
        for row, keys in enumerate(layout):
            x = x0 + row * key_w * .45
            for char in keys:
                item = self.create_rectangle(x, 12 + row * 32, x + key_w, 39 + row * 32, fill=self.colors["panel2"], outline="", tags=("key", char)); self.create_text(x + key_w / 2, 25 + row * 32, text=char, fill=self.colors["muted"], font=FONT_KEY, tags=("label", char)); self.key_items[char] = item; x += key_w + 5
    def highlight_key(self, char: str):
        self.reset_highlight(); char = char.lower();
        if char in self.key_items: self.itemconfigure(self.key_items[char], fill=self.colors["accent"])
    def reset_highlight(self):
        for item in self.key_items.values(): self.itemconfigure(item, fill=self.colors["panel2"])
    def on_resize(self, _event=None):
        if self.layout: self.after_idle(lambda: self.draw_keyboard(self.layout))
