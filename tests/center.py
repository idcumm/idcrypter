import os
try:
    import requests, sys, ctypes, warnings
    from bs4 import BeautifulSoup, MarkupResemblesLocatorWarning
    from time import sleep
    from pystyle import Colors, Colorate, Write, Center
except (ImportError, ModuleNotFoundError):
    print('   >> Instalando dependencias...')
    os.sys('python -m pip install -r requirements.txt')

# print(Colorate.Vertical(Colors.yellow_to_green, Center.Center(f"""
# {Colors.yellow}[{Colors.light_gray}01{Colors.yellow}] {Colors.white}Binario                               {Colors.yellow}[{Colors.light_gray}02{Colors.yellow}] {Colors.white}Hexadecimal                           {Colors.yellow}[{Colors.light_gray}03{Colors.yellow}] {Colors.white}Cifrado URL
# """)))
print(Colorate.Horizontal(Colors.blue_to_red, Center.XCenter(f"""
    [01] Binario                               [02] Hexadecimal                           [03] Cifrado URL
""")))