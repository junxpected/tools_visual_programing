@echo off
setlocal
cd /d "%~dp0"
py -m pip install pyinstaller
if errorlevel 1 exit /b 1
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
py -m PyInstaller --noconfirm --clean --onefile --windowed --name TypeFlow main.py
echo Ready: dist\TypeFlow.exe
