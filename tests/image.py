import os
try:
    import requests, sys, ctypes, warnings
    from bs4 import BeautifulSoup, MarkupResemblesLocatorWarning
    from time import sleep
    from pystyle import Colors, Colorate, Write, Center, Anime, System
except (ImportError, ModuleNotFoundError):
    print('   >> Instalando dependencias...')
    os.sys('python -m pip install -r requirements.txt')
    
System.Size(120, 30)

banner = ''' ██▓▓█████▄  ▄████▄   ██▀███ ▓██   ██▓ ██▓███  ▄▄▄█████▓▓█████  ██▀███  
▓██▒▒██▀ ██▌▒██▀ ▀█  ▓██ ▒ ██▒▒██  ██▒▓██░  ██▒▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒
▒██▒░██   █▌▒▓█    ▄ ▓██ ░▄█ ▒ ▒██ ██░▓██░ ██▓▒▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒
░██░░▓█▄   ▌▒▓▓▄ ▄██▒▒██▀▀█▄   ░ ▐██▓░▒██▄█▓▒ ▒░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄  
░██░░▒████▓ ▒ ▓███▀ ░░██▓ ▒██▒ ░ ██▒▓░▒██▒ ░  ░  ▒██▒ ░ ░▒████▒░██▓ ▒██▒
░▓   ▒▒▓  ▒ ░ ░▒ ▒  ░░ ▒▓ ░▒▓░  ██▒▒▒ ▒▓▒░ ░  ░  ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░
 ▒ ░ ░ ▒  ▒   ░  ▒     ░▒ ░ ▒░▓██ ░▒░ ░▒ ░         ░     ░ ░  ░  ░▒ ░ ▒░
 ▒ ░ ░ ░  ░ ░          ░░   ░ ▒ ▒ ░░  ░░         ░         ░     ░░   ░ 
 ░     ░    ░ ░         ░     ░ ░                          ░  ░   ░     
     ░      ░                 ░ ░'''

# print(Colorate.Vertical(Colors.purple_to_red, Center.Center(f'\n{banner}\n\n\n\n')))

Anime.Fade(Center.Center(f'\n{banner}\n\n\n\n'), Colors.purple_to_blue, Colorate.Vertical, time=2)
input()