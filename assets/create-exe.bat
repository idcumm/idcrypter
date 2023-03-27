@echo off
cd ..
pyinstaller --clean --onefile -i icon.ico main.py
pause