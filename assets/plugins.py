import requests
import os
import sys
import ctypes
from bs4 import BeautifulSoup
from time import sleep
from pystyle import Colors, Colorate, Write, Center


def progress_bar(len, pos, interval):
    print('\n')
    space = '\t\t\t\t\t  '
    for i in range(len - pos + 1):
        message = ''
        for i in range(pos):
            message += '█'
        for i in range(len - pos):
            message += '░'
        pos += 1
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


def clear():
    system = os.name
    if system == 'nt':
        os.system('cls')
    elif system == 'posix':
        os.system('clear')
    else:
        print('\n'*120)
    return


def idcrypter():
    print(Center.XCenter(Colorate.Vertical(Colors.yellow_to_red, """
                             ____  ___      __  ____   __ __  ____  ______    ___  ____  
                            l    j|   \    /  ]|    \ |  T  T|    \|      T  /  _]|    \ 
                             |  T |    \  /  / |  D  )|  |  ||  o  )      | /  [_ |  D  )
                             |  | |  D  Y/  /  |    / |  ~  ||   _/l_j  l_jY    _]|    / 
                             |  | |     /   \_ |    \ l___, ||  |    |  |  |   [_ |    \ 
                             j  l |     \     ||  .  Y|     !|  |    |  |  |     T|  .  Y
                            |____jl_____j\____jl__j\_jl____/ l__j    l__j  l_____jl__j\_j\n\n""", 1)))


def enc_options():
    print(Center.XCenter(f"""
\n    {Colors.yellow}[{Colors.light_gray}1{Colors.yellow}] {Colors.white}Texto a Binario                      {Colors.yellow}[{Colors.light_gray}2{Colors.yellow}] {Colors.white}Binario a Texto               {Colors.yellow}[{Colors.light_gray}3{Colors.yellow}] {Colors.white}Texto a Hexadecimal
\n    {Colors.yellow}[{Colors.light_gray}4{Colors.yellow}] {Colors.white}Hexadecimal a Texto                  {Colors.yellow}[{Colors.light_gray}5{Colors.yellow}] {Colors.white}Binario a Hexadecimal         {Colors.yellow}[{Colors.light_gray}6{Colors.yellow}] {Colors.white}Hexadecimal a Binario
\n    {Colors.yellow}[{Colors.light_gray}7{Colors.yellow}] {Colors.white}Texto al revés                       {Colors.yellow}[{Colors.light_gray}8{Colors.yellow}] {Colors.white}Base 64 (codificar)           {Colors.yellow}[{Colors.light_gray}9{Colors.yellow}] {Colors.white}Base 64 (descodificar)
\n    {Colors.yellow}[{Colors.light_gray}10{Colors.yellow}] {Colors.white}Cifrado César                       {Colors.yellow}[{Colors.light_gray}11{Colors.yellow}] {Colors.light_red}Encriptación DES             {Colors.yellow}[{Colors.light_gray}12{Colors.yellow}] {Colors.white}Entidades HTML (codificar)
\n    {Colors.yellow}[{Colors.light_gray}13{Colors.yellow}] {Colors.white}Entidades HTML (descodificar)       {Colors.yellow}[{Colors.light_gray}14{Colors.yellow}] {Colors.white}Texto a l33t 5p34k           {Colors.yellow}[{Colors.light_gray}15{Colors.yellow}] {Colors.white}l33t 5p34k a Texto
\n    {Colors.yellow}[{Colors.light_gray}16{Colors.yellow}] {Colors.light_red}Encriptación MD5                    {Colors.yellow}[{Colors.light_gray}17{Colors.yellow}] {Colors.white}Texto a Pig Latin            {Colors.yellow}[{Colors.light_gray}18{Colors.yellow}] {Colors.white}Pig Latin a Texto
\n    {Colors.yellow}[{Colors.light_gray}19{Colors.yellow}] {Colors.white}Texto a ROT-13                      {Colors.yellow}[{Colors.light_gray}20{Colors.yellow}] {Colors.white}Codificar URL                {Colors.yellow}[{Colors.light_gray}21{Colors.yellow}] {Colors.white}Descodificar URL
\n    {Colors.yellow}[{Colors.light_gray}0{Colors.yellow}] {Colors.green}Configuración                        {Colors.yellow}[{Colors.light_gray}<{Colors.yellow}] {Colors.green}Anterior Página               {Colors.yellow}[{Colors.light_gray}>{Colors.yellow}] {Colors.green}Siguiente Página
\n\n"""))


def enc_options2():
    print(Center.XCenter(f"""
\n    {Colors.yellow}[{Colors.light_gray}1{Colors.yellow}] {Colors.white}AES                                  {Colors.yellow}[{Colors.light_gray}2{Colors.yellow}] {Colors.white}Triple DES                    {Colors.yellow}[{Colors.light_gray}3{Colors.yellow}] {Colors.white}Test
\n
\n
\n
\n
\n
\n
\n    {Colors.yellow}[{Colors.light_gray}0{Colors.yellow}] {Colors.green}Configuración                        {Colors.yellow}[{Colors.light_gray}<{Colors.yellow}] {Colors.green}Anterior Página               {Colors.yellow}[{Colors.light_gray}>{Colors.yellow}] {Colors.green}Siguiente Página
\n\n"""))


def config_options():
    print(Center.XCenter(f"""
    \n    {Colors.yellow}[{Colors.light_gray}1{Colors.yellow}] {Colors.white}Temas                      {Colors.yellow}[{Colors.light_gray}2{Colors.yellow}] {Colors.white}Test               {Colors.yellow}[{Colors.light_gray}3{Colors.yellow}] {Colors.white}Salir
    \n
    \n
    \n
    \n
    \n
    \n
    \n
    \n\n"""))


def config_main():
    while True:
        try:
            number = int(Write.Input(
                "    >> [#] Elección: ", Colors.light_gray, interval=0.01)) - 1
            print()
            break
        except (TypeError, ValueError):
            print()
            Write.Print('    >> Porvafor, escriba un número válido.',
                        Colors.light_red, interval=0.01)
            print('\n')
            sleep(0.5)
    if number > 2 or number < -1 or number == 1:
        Write.Print('    >> En desarrollo... ',
                    Colors.light_red, interval=0.01)
        print()
    elif number == 0:
        Write.Print(
            '    >> Temas: [0] Neon, [1] Sunset, [2] White', Colors.light_red, interval=0.01)
