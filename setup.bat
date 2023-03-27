@echo off
cd others
python -m pip install -r requirements.txt
cd ..
del start.bat
echo @echo off >> start.bat
echo cd assets >> start.bat
echo python main.py >> start.bat
exit