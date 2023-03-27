@echo off
pyinstaller --clean --onefile -i icon.ico main.py
rmdir build /s /q
del main.spec /q
move /y dist\main.exe ..
rmdir dist /s /q
rmdir __pycache__ /s /q