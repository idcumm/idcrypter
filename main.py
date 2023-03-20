import requests, os
from bs4 import BeautifulSoup
from time import sleep
from pystyle import Colors, Colorate, Write, Center

os.system('@echo off')
os.system('color c')
os.system('title Encrypter / Decrypter - Disfunción Erectil')

print(Center.XCenter(Colorate.Vertical(Colors.yellow_to_red, """




                             ____  ___      __  ____   __ __  ____  ______    ___  ____  
                            l    j|   \    /  ]|    \ |  T  T|    \|      T  /  _]|    \ 
                             |  T |    \  /  / |  D  )|  |  ||  o  )      | /  [_ |  D  )
                             |  | |  D  Y/  /  |    / |  ~  ||   _/l_j  l_jY    _]|    / 
                             |  | |     /   \_ |    \ l___, ||  |    |  |  |   [_ |    \ 
                             j  l |     \     ||  .  Y|     !|  |    |  |  |     T|  .  Y
                            |____jl_____j\____jl__j\_jl____/ l__j    l__j  l_____jl__j\_j


""", 1)))

spacing = '                                                 '
starting_message = '▌░░░░░░░░░░░░░░░░░'
lenght = len(starting_message)
last_char = starting_message[lenght-1]
position = starting_message.find('▌') + 1
contra2 = False
contra = False

print(Colors.orange, f'\r{spacing}|{starting_message}{last_char}|',end='')

while position <= lenght + 1:
    message = ''
    b = 0

    while b < position:
        if contra == True and b == position - 1:
            message = message + '▌'

            contra = False
            position = position - 1
        elif contra == False and b == position - 1:
            message = message + '█'

            contra = True
            contra2 = True
        else:
            message = message + '█'

        b = b + 1

    if contra2 == True and not position > lenght:
        message = message + '░'
        contra2 = False

    for i in range(lenght - position):
        message = message + '░'
    position = position + 1
    sleep(0.05)
    print(Colors.orange, f'\r{spacing}|{message}|',end='')

url = 'https://superpatanegra.com/texto/index.php'

enc_types = ['asc2bin', 'bin2asc', 'asc2hex', 'hex2asc', 'bin2hex', 'hex2bin', 'backwards', 'b64enc', 'b64dec', 'caesarbf', 'crypt', 'entityenc', 'entitydec', 'l33t', 'del33t', 'md5', 'igpay', 'unigpay', 'rot-13', 'urlenc', 'urldec']

def __main__():
    os.system('cls')
    print(Center.XCenter(f"""


    {Colors.yellow}[{Colors.white}1{Colors.yellow}] {Colors.white}Texto a Binario                      {Colors.yellow}[{Colors.white}2{Colors.yellow}] {Colors.white}Binario a Texto               {Colors.yellow}[{Colors.white}3{Colors.yellow}] {Colors.white}Texto a Hexadecimal

    {Colors.yellow}[{Colors.white}4{Colors.yellow}] {Colors.white}Hexadecimal a Texto                  {Colors.yellow}[{Colors.white}5{Colors.yellow}] {Colors.white}Binario a Hexadecimal         {Colors.yellow}[{Colors.white}6{Colors.yellow}] {Colors.white}Hexadecimal a Binario

    {Colors.yellow}[{Colors.white}7{Colors.yellow}] {Colors.white}Texto al revés                       {Colors.yellow}[{Colors.white}8{Colors.yellow}] {Colors.white}Base 64 (codificar)           {Colors.yellow}[{Colors.white}9{Colors.yellow}] {Colors.white}Base 64 (descodificar)

    {Colors.yellow}[{Colors.white}10{Colors.yellow}] {Colors.red}*{Colors.white}Cifrado César{Colors.red}*                     {Colors.yellow}[{Colors.white}11{Colors.yellow}] {Colors.light_gray}Encriptación DES             {Colors.yellow}[{Colors.white}12{Colors.yellow}] {Colors.white}Entidades HTML (codificar)

    {Colors.yellow}[{Colors.white}13{Colors.yellow}] {Colors.white}Entidades HTML (descodificar)       {Colors.yellow}[{Colors.white}14{Colors.yellow}] {Colors.white}Texto a l33t 5p34k           {Colors.yellow}[{Colors.white}15{Colors.yellow}] {Colors.white}l33t 5p34k a Texto

    {Colors.yellow}[{Colors.white}16{Colors.yellow}] {Colors.light_gray}Encriptación MD5                    {Colors.yellow}[{Colors.white}17{Colors.yellow}] {Colors.white}Texto a Pig Latin            {Colors.yellow}[{Colors.white}18{Colors.yellow}] {Colors.white}Pig Latin a Texto

    {Colors.yellow}[{Colors.white}19{Colors.yellow}] {Colors.white}Texto a ROT-13                      {Colors.yellow}[{Colors.white}20{Colors.yellow}] {Colors.white}Codificar URL                {Colors.yellow}[{Colors.white}21{Colors.yellow}] {Colors.white}Descodificar URL


    """))
    while True:
        try:
            number = int(Write.Input("    [#] Elección: ", Colors.light_gray, interval=0.01)) - 1
            break
        except (TypeError, ValueError):
            Write.Print('    Porvafor, escriba un número válido.', Colors.light_gray, interval=0.01)
            sleep(0.5)

    if number == 9:
        Write.Print('    En desarrollo... ', Colors.light_gray, interval=0.01)
    else:
        while True:
            try:
                text = Write.Input('    Escriba el mensaje que desea encriptar/desencriptar: ', Colors.light_gray, interval=0.01)
                r = requests.post(url, data={'text': text, 'cryptmethod': enc_types[number], 'submit': 'OK'})
                soup = BeautifulSoup(r.text, features='html.parser')
                data = [item.text for item in soup.select('p')]
                keyword = 'TEXTO PROCESADO:'
                before_keyword, keyword, after_keyword = data[1].partition(keyword)
                break
            except IndexError:
                Write.Print('    Porvafor, escriba un mensaje válido.', Colors.light_gray, interval=0.01)
                sleep(0.5)
        if len(after_keyword) > 200:
           print(Colors.yellow, f"""
            {after_keyword}
        
            """)
        else:
            Write.Print(f"""
            {after_keyword}
        
            """, Colors.yellow, interval=0.001)

    Write.Input('    Pulsa cualquier tecla para continuar: ', Colors.light_gray, interval=0.01)

while True:
    __main__()
