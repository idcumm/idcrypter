@echo off
python -m pip install -r requirements.txt
del start.bat
echo @echo off >> start.bat
echo python main.py >> start.bat
start start.bat
start /b "" cmd /c &exit /b