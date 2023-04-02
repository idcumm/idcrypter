import os
try:
    import requests, sys, ctypes, warnings
    from bs4 import BeautifulSoup, MarkupResemblesLocatorWarning
    from time import sleep
    from pystyle import Colors, Colorate, Write, Center
except (ImportError, ModuleNotFoundError):
    print('   >> Instalando dependencias...')
    os.sys('python -m pip install -r requirements.txt')


print(Colorate.Vertical(Colors.purple_to_red, Center.Center('''                                                           
 ██▓▓█████▄  ▄████▄   ██▀███ ▓██   ██▓ ██▓███  ▄▄▄█████▓▓█████  ██▀███  
▓██▒▒██▀ ██▌▒██▀ ▀█  ▓██ ▒ ██▒▒██  ██▒▓██░  ██▒▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒
▒██▒░██   █▌▒▓█    ▄ ▓██ ░▄█ ▒ ▒██ ██░▓██░ ██▓▒▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒
░██░░▓█▄   ▌▒▓▓▄ ▄██▒▒██▀▀█▄   ░ ▐██▓░▒██▄█▓▒ ▒░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄  
░██░░▒████▓ ▒ ▓███▀ ░░██▓ ▒██▒ ░ ██▒▓░▒██▒ ░  ░  ▒██▒ ░ ░▒████▒░██▓ ▒██▒
░▓   ▒▒▓  ▒ ░ ░▒ ▒  ░░ ▒▓ ░▒▓░  ██▒▒▒ ▒▓▒░ ░  ░  ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░
 ▒ ░ ░ ▒  ▒   ░  ▒     ░▒ ░ ▒░▓██ ░▒░ ░▒ ░         ░     ░ ░  ░  ░▒ ░ ▒░
 ▒ ░ ░ ░  ░ ░          ░░   ░ ▒ ▒ ░░  ░░         ░         ░     ░░   ░ 
 ░     ░    ░ ░         ░     ░ ░                          ░  ░   ░     
     ░      ░                 ░ ░                                       
                                                                          ''')))
input()