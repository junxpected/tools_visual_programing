#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
python3 -m pip install --user pyinstaller
rm -rf build dist
python3 -m PyInstaller --noconfirm --clean --onefile --windowed --name TypeFlow-linux main.py
chmod +x dist/TypeFlow-linux
tar -czf dist/TypeFlow-linux.tar.gz -C dist TypeFlow-linux
echo "Готово: dist/TypeFlow-linux.tar.gz"
