from __future__ import annotations
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SETTINGS_FILE = ROOT / "settings.json"
HISTORY_FILE = ROOT / "history.json"
WINDOW_MIN_SIZE = (900, 600)

THEMES = {
    "graphite": {"bg": "#0A0A0A", "panel": "#141414", "panel2": "#1C1C1C", "border": "#2A2A2A", "fg": "#F5F5F5", "muted": "#7A7A7A", "accent": "#E8B84B", "hover": "#F2C860", "accent_dim": "#5C4A1E", "correct": "#6FCF97", "error": "#EB5757", "pending": "#5A5A5A"},
    "ocean": {"bg": "#151b24", "panel": "#1d2632", "panel2": "#293648", "fg": "#e5edf8", "muted": "#8796a8", "accent": "#64a9ed", "correct": "#75d1ad", "error": "#e68181"},
    "forest": {"bg": "#151d1a", "panel": "#1d2924", "panel2": "#2a3a32", "fg": "#e8f2eb", "muted": "#899b91", "accent": "#66c58d", "correct": "#9ad69f", "error": "#e38181"},
    "violet": {"bg": "#211b2b", "panel": "#2d2439", "panel2": "#3c304c", "fg": "#f0eafa", "muted": "#a99abb", "accent": "#bd91ed", "correct": "#9fd5b7", "error": "#e98585"},
    "rose": {"bg": "#21191f", "panel": "#2d222a", "panel2": "#3b2c37", "fg": "#f4eaf1", "muted": "#aa91a1", "accent": "#e58abb", "correct": "#9fd5b7", "error": "#e98585"},
}

FONT_TITLE = ("Helvetica", 22, "bold")
FONT_NAV = ("Helvetica", 14, "normal")
FONT_NAV_ACTIVE = ("Helvetica", 14, "bold")
FONT_TEXT = ("Courier", 22, "normal")
FONT_STAT = ("Helvetica", 18, "bold")
FONT_LABEL = ("Helvetica", 10, "normal")
FONT_KEY = ("Helvetica", 11, "normal")
FONT_BUTTON = ("Helvetica", 13, "bold")

TEXTS = {
    "Українська": {
        "Легкий": ["Кожен день дає нову можливість стати кращим.", "Швидкий друк починається зі спокійного ритму.", "Маленькі кроки щодня приводять до великих результатів.", "Зручна клавіатура допомагає працювати уважно і спокійно.", "Навчання стає цікавішим, коли бачиш власний прогрес."],
        "Середній": ["Регулярна практика допомагає друкувати швидше, точніше та впевненіше.", "Точність важлива не менше за швидкість, особливо під час роботи з кодом.", "Поступове ускладнення вправ формує надійну м’язову пам’ять пальців.", "Спробуйте зберігати однаковий ритм, навіть якщо текст здається простим."],
        "Складний": ["Справжній результат з’являється тоді, коли точність залишається важливішою за поспіх.", "Програмування, навчання та спілкування стають комфортнішими, коли клавіатура більше не сповільнює думки.", "Стабільний темп, правильна посадка та короткі перерви допомагають тренуватися без перевтоми.", "Коли помилка вже не збиває ритм, друкування перетворюється на природне продовження думки."],
    },
    "English": {
        "Easy": ["Practice makes every keyboard shortcut feel natural.", "A calm rhythm is the first step to faster typing.", "Small improvements every day create strong habits over time.", "A clean desk helps you focus on the words in front of you.", "Learning is easier when you can see your progress."],
        "Medium": ["Regular practice helps you type faster, more accurately, and with greater confidence.", "Accuracy matters as much as speed when you are writing code or taking notes.", "Gradually harder exercises build reliable muscle memory for every finger.", "Try to keep the same pace even when the sentence feels simple."],
        "Hard": ["Real progress appears when accuracy remains more important than rushing through every sentence.", "Writing code and ideas becomes easier when the keyboard no longer interrupts your train of thought.", "A steady pace, good posture, and short breaks make practice productive without unnecessary fatigue.", "When a mistake no longer breaks your rhythm, typing becomes a natural extension of your thoughts."],
    },
}

KEYBOARD_LAYOUT_EN = [list("1234567890-="), list("qwertyuiop[]"), list("asdfghjkl;'") , list("zxcvbnm,./")]
KEYBOARD_LAYOUT_UA = [list("1234567890-="), list("йцукенгшщзхї"), list("фівапролджє"), list("ячсмитьбю.")]

UI = {
    "Українська": {"training": "Тренування", "history": "Історія", "settings": "Налаштування", "help": "Допомога", "new": "Новий текст", "start": "Старт", "stop": "Стоп", "language": "Мова", "level": "Рівень", "theme": "Тема", "save": "Зберегти", "reset": "Скинути", "speed": "WPM", "accuracy": "Точність", "errors": "Помилки", "time": "Час", "type": "Надрукуйте текст нижче", "ready": "Готові? Таймер стартує після першого символу.", "done": "Вправу завершено!", "fullscreen": "Повний екран", "palette": "Палітра кольорів"},
    "English": {"training": "Training", "history": "History", "settings": "Settings", "help": "Help", "new": "New text", "start": "Start", "stop": "Stop", "language": "Language", "level": "Level", "theme": "Theme", "save": "Save", "reset": "Reset", "speed": "WPM", "accuracy": "Accuracy", "errors": "Errors", "time": "Time", "type": "Type the text below", "ready": "Ready? The timer starts with your first character.", "done": "Test complete!", "fullscreen": "Fullscreen", "palette": "Color palette"},
}
