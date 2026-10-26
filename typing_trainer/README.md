# TypeFlow

Кросплатформний тренажер сліпого друку на Python/Tkinter для Fedora/Linux і Windows.

Можливості: українські та англійські тексти, три рівні, WPM, точність, помилки, таймер, підсвічування тексту, віртуальна клавіатура, fullscreen F11/Esc, історія результатів, налаштування мови та 5 тем.

## Запуск на Fedora

```bash
sudo dnf install python3-tkinter
python3 main.py
```

## Тести

```bash
python3 -m unittest discover -s tests -v
```

## Збірка

Linux: `./build_linux.sh` створює `dist/TypeFlow-linux`.

Windows: запустіть `build_windows.bat`; результат — `dist\\TypeFlow.exe`.

Готові Linux і Windows артефакти збираються GitHub Actions під час release-тега `typeflow-v*`.
