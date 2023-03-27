@echo off
cd ..
pyinstaller --clean --onefile -i icon.ico main.py
rmdir build /s /q
del main.spec /q
cd dist
move /y main.exe ..
cd ..
rmdir dist /s /q