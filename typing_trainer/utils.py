from __future__ import annotations
import json
from pathlib import Path

def load_json(path: Path, default):
    try: return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError): return default

def save_json(path: Path, data) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

def calculate_wpm(chars_typed: int, seconds: float) -> float:
    return chars_typed / 5 / max(seconds / 60, 1 / 60)

def calculate_accuracy(correct: int, total: int) -> float:
    if total <= 0:
        return 100
    return correct / total * 100
