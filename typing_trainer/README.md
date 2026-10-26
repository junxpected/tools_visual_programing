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

Linux: `./build_linux.sh` створює `dist/TypeFlow-linux.tar.gz`.

Після завантаження Linux-архіву:

```bash
tar -xzf TypeFlow-linux.tar.gz
chmod +x TypeFlow-linux
./TypeFlow-linux
```

Windows: запустіть `build_windows.bat`; результат — `dist\\TypeFlow.exe`.

Готові Linux і Windows артефакти збираються GitHub Actions під час release-тега `typeflow-v*`.

## Завантаження програми

- [Завантажити TypeFlow для Windows (.exe)](https://github.com/junxpected/tools_visual_programing/releases/download/typeflow-v1.0.0/TypeFlow.exe)
- [Завантажити TypeFlow для Linux (.tar.gz)](https://github.com/junxpected/tools_visual_programing/releases/download/typeflow-v1.0.0/TypeFlow-linux.tar.gz)
- [Переглянути всі релізи](https://github.com/junxpected/tools_visual_programing/releases)

### Windows

Завантажте `TypeFlow.exe` і запустіть подвійним кліком. Інсталяція Python не потрібна.

### Linux

```bash
wget https://github.com/junxpected/tools_visual_programing/releases/download/typeflow-v1.0.0/TypeFlow-linux.tar.gz
tar -xzf TypeFlow-linux.tar.gz
chmod +x TypeFlow-linux
./TypeFlow-linux
```
