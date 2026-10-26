from __future__ import annotations

import tempfile
import tkinter as tk
import unittest
from pathlib import Path

from config import KEYBOARD_LAYOUT_EN, KEYBOARD_LAYOUT_UA, THEMES, TEXTS, UI
from utils import calculate_accuracy, calculate_wpm, load_json, save_json


class CoreTests(unittest.TestCase):
    def test_wpm_and_accuracy(self):
        self.assertEqual(calculate_wpm(25, 60), 5)
        self.assertEqual(calculate_accuracy(9, 10), 90.0)
        self.assertEqual(calculate_accuracy(0, 0), 100)

    def test_json_roundtrip_and_invalid_file(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "data.json"
            save_json(path, {"score": 42}); self.assertEqual(load_json(path, {}), {"score": 42})
            path.write_text("not json", encoding="utf-8"); self.assertEqual(load_json(path, {"fallback": True}), {"fallback": True})

    def test_every_language_has_multiple_levels_and_texts(self):
        self.assertEqual(set(TEXTS), {"Українська", "English"})
        for levels in TEXTS.values():
            self.assertGreaterEqual(len(levels), 3)
            for texts in levels.values(): self.assertGreaterEqual(len(texts), 3); self.assertTrue(all(texts))

    def test_themes_and_translations_are_complete(self):
        required = {"bg", "panel", "panel2", "fg", "muted", "accent", "correct", "error"}
        for theme in THEMES.values(): self.assertTrue(required.issubset(theme))
        for language in ("Українська", "English"): self.assertTrue({"training", "history", "settings", "help", "language", "level"}.issubset(UI[language]))

    def test_keyboard_layouts_have_keys(self):
        self.assertGreaterEqual(sum(map(len, KEYBOARD_LAYOUT_EN)), 30)
        self.assertGreaterEqual(sum(map(len, KEYBOARD_LAYOUT_UA)), 30)


class GuiSmokeTest(unittest.TestCase):
    def test_app_can_build_pages_when_display_is_available(self):
        try:
            from app import App
            app = App()
        except tk.TclError as exc:
            self.skipTest(f"GUI display unavailable: {exc}")
        try:
            self.assertIn("training", app.nav); self.assertIn("history", app.nav); self.assertIn("settings", app.nav); self.assertIn("help", app.nav); self.assertTrue(app.page_host.winfo_children()[0].winfo_manager())
            app.show_page("history"); app.show_page("settings"); app.show_page("help"); app.show_page("training")
        finally:
            app.destroy()


if __name__ == "__main__": unittest.main(verbosity=2)
