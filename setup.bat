@echo off
pip install -r requirements.txt
del start.bat
echo @echo off >> start.bat
echo python main.py >> start.bat