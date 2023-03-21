import requests, os, sys, ctypes
from bs4 import BeautifulSoup
from time import sleep
from pystyle import Colors, Colorate, Write, Center

def progress_bar(len, pos, interval):
    space = '                                           '
    for i in range(len - pos + 1):
        message = ''
        for i in range(pos):
            message += '█'
        for i in range(len - pos):
            message += '░'
        pos+= 1
        print(Colors.gray, f'\r{space}|{message}|', end='')
        sleep(interval)

def setTitle(_str):
    system = os.name
    if system == 'nt':
        ctypes.windll.kernel32.SetConsoleTitleW(f"{_str} - Made By idcum")
    elif system == 'posix':
        sys.stdout.write(f"\x1b]0;{_str} - Made By idcum\x07")
    else:
        pass

def config():
    system = os.name
    if system == 'nt':
        os.system('cls')
    elif system == 'posix':
        os.system('clear')
    else:
        pass

    print("""
                [1] Change Theme
    """)