from __future__ import annotations
import random
import time
import tkinter as tk
from tkinter import ttk
from config import KEYBOARD_LAYOUT_EN, KEYBOARD_LAYOUT_UA, TEXTS, UI, FONT_TEXT, FONT_STAT, FONT_LABEL, FONT_BUTTON
from keyboard_widget import VirtualKeyboard
from utils import calculate_accuracy, calculate_wpm

class TrainingPage(tk.Frame):
    def __init__(self, app):
        self.app = app; super().__init__(app.page_host, bg=app.colors["bg"]); self.target = ""; self.started_at = 0; self.running = False; self.finished = False; self.errors = 0; self.duration = 60; self.build(); self.reset_test()
    def t(self, key): return UI[self.app.language].get(key, key)
    def build(self):
        c = self.app.colors; controls = tk.Frame(self, bg=c["bg"]); controls.pack(fill="x", pady=(0, 18)); tk.Label(controls, text=UI[self.app.language]["language"], bg=c["bg"], fg=c["muted"], font=("Inter", 9)).pack(side="left"); self.language_box = ttk.Combobox(controls, values=list(TEXTS), state="readonly", width=15); self.language_box.set(self.app.language); self.language_box.pack(side="left", padx=(8, 22)); self.language_box.bind("<<ComboboxSelected>>", self.change_language); tk.Label(controls, text=UI[self.app.language].get("level", "Level"), bg=c["bg"], fg=c["muted"], font=("Inter", 9)).pack(side="left"); self.level_box = ttk.Combobox(controls, values=list(TEXTS[self.app.language]), state="readonly", width=14); self.level_box.set(self.app.level); self.level_box.pack(side="left", padx=8); self.level_box.bind("<<ComboboxSelected>>", self.change_level)
        top = tk.Frame(self, bg=c["bg"]); top.pack(fill="x", pady=(5, 20)); self.stats = {}
        for key in ("speed", "accuracy", "errors", "time"):
            box = tk.Frame(top, bg=c["panel"], width=145, height=72, highlightbackground=c["panel2"], highlightthickness=1); box.pack(side="left", fill="x", expand=True, padx=(0, 10)); box.pack_propagate(False); tk.Label(box, text=self.t(key), bg=c["panel"], fg=c["muted"], font=("Inter", 8)).pack(anchor="w", padx=12, pady=(10, 0)); var = tk.StringVar(value="0"); self.stats[key] = var; tk.Label(box, textvariable=var, bg=c["panel"], fg=c["fg"], font=("Inter", 20, "bold")).pack(anchor="w", padx=12)
        panel = tk.Frame(self, bg=c["panel"], padx=28, pady=22); panel.pack(fill="x"); tk.Label(panel, text=self.t("type"), bg=c["panel"], fg=c["muted"], font=("Inter", 9)).pack(anchor="w")
        self.text_view = tk.Text(panel, height=4, wrap="word", bg=c["panel"], fg=c.get("pending", c["muted"]), relief="flat", font=FONT_TEXT); self.text_view.pack(fill="x", pady=(12, 17)); self.text_view.configure(state="disabled"); self.text_view.tag_configure("done", foreground=c["correct"]); self.text_view.tag_configure("wrong", foreground=c["error"]); self.text_view.tag_configure("next", foreground=c["accent"] , underline=True)
        self.input = tk.Text(panel, height=3, wrap="word", bg=c["panel2"], fg=c["fg"], insertbackground=c["accent"], relief="flat", font=FONT_TEXT, padx=12, pady=10); self.input.pack(fill="x"); self.input.bind("<KeyPress>", self.on_key_press); self.input.bind("<KeyRelease>", self.update_stats)
        self.progress = ttk.Progressbar(panel, maximum=100); self.progress.pack(fill="x", pady=(18, 5)); self.message = tk.StringVar(); tk.Label(panel, textvariable=self.message, bg=c["panel"], fg=c["muted"], font=("Inter", 9)).pack(anchor="w")
        controls = tk.Frame(self, bg=c["bg"]); controls.pack(fill="x", pady=12); ttk.Button(controls, text=self.t("start"), command=self.start_test).pack(side="left", padx=(0, 7)); ttk.Button(controls, text=self.t("stop"), command=self.stop_test).pack(side="left", padx=(0, 7)); ttk.Button(controls, text=self.t("new"), style="Accent.TButton", command=self.reset_test).pack(side="right")
        layout = KEYBOARD_LAYOUT_UA if self.app.language == "Українська" else KEYBOARD_LAYOUT_EN; self.keyboard = VirtualKeyboard(self, c); self.keyboard.pack(fill="x", pady=(10, 0)); self.keyboard.draw_keyboard(layout)
    def reset_test(self):
        lang = self.app.language
        if self.app.level not in TEXTS[lang]: self.app.level = list(TEXTS[lang])[0]
        level = self.app.level; self.target = random.choice(TEXTS[lang][level]); self.running = False; self.finished = False; self.errors = 0; self.started_at = 0; self.message.set(self.t("ready")); self.input.delete("1.0", "end"); self.progress["value"] = 0; [var.set("0" if key != "accuracy" else "100%") for key, var in self.stats.items()]; self.render_text(""); self.keyboard.reset_highlight(); self.keyboard.highlight_key(self.target[0] if self.target else "")
    def change_language(self, _event=None):
        self.app.language = self.language_box.get(); self.app.level = list(TEXTS[self.app.language])[0]; self.app.show_page("training")
    def change_level(self, _event=None):
        self.app.level = self.level_box.get(); self.reset_test()
    def start_test(self):
        if not self.running: self.running = True; self.finished = False; self.started_at = time.monotonic(); self.message.set(self.t("ready")); self.tick(); self.input.focus_set()
    def stop_test(self): self.running = False; self.message.set("Stopped" if self.app.language == "English" else "Зупинено")
    def on_key_press(self, event):
        if not self.running and event.char and not self.finished: self.start_test()
        if event.char: self.keyboard.highlight_key(event.char)
    def tick(self):
        if self.running and not self.finished:
            elapsed = int(time.monotonic() - self.started_at); self.stats["time"].set(f"{elapsed}s")
            if elapsed >= self.duration: self.finish_test(); return
            self.after(500, self.tick)
    def render_text(self, typed):
        self.text_view.configure(state="normal"); self.text_view.delete("1.0", "end"); self.text_view.insert("1.0", self.target)
        for tag in ("done", "wrong", "next"): self.text_view.tag_remove(tag, "1.0", "end")
        for i, char in enumerate(typed[:len(self.target)]): self.text_view.tag_add("done" if char == self.target[i] else "wrong", f"1.0+{i}c", f"1.0+{i+1}c")
        if len(typed) < len(self.target): self.text_view.tag_add("next", f"1.0+{len(typed)}c", f"1.0+{len(typed)+1}c")
        self.text_view.configure(state="disabled")
    def update_stats(self, _event=None):
        typed = self.input.get("1.0", "end-1c"); correct = sum(a == b for a, b in zip(self.target, typed)); self.errors = sum(a != b for a, b in zip(self.target, typed)) + max(0, len(typed) - len(self.target)); elapsed = time.monotonic() - self.started_at if self.started_at else 0; self.stats["speed"].set(f"{calculate_wpm(correct, elapsed):.0f}"); self.stats["accuracy"].set(f"{calculate_accuracy(correct, len(typed)):.0f}%"); self.stats["errors"].set(str(self.errors)); self.progress["value"] = min(100, len(typed) / max(1, len(self.target)) * 100); self.render_text(typed)
        if len(typed) >= len(self.target): self.finish_test()
    def finish_test(self):
        if self.finished: return
        self.finished = True; self.running = False; self.message.set(self.t("done")); self.app.save_result(self.stats)
