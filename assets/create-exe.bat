@echo off
pyinstaller --clean --onefile -i icon.ico main.py
cd ..
rmdir build /s /q
del main.spec /q
cd dist
move /y main.exe ..
cd ..
rmdir dist /s /q