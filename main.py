import requests, os
from bs4 import BeautifulSoup
from time import sleep
from pystyle import Colors, Colorate, Write, Center

os.system('@echo off')
os.system('title  idcummm - Encrypter / Decrypter - Discord: lezduit#8218')

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
lenght = 18
position = 1
help2 = False
help = False

print(Colors.gray, f'\r{spacing}|░░░░░░░░░░░░░░░░░░░|',end='')
print(Colors.gray, f'\r{spacing}|▌░░░░░░░░░░░░░░░░░░|',end='')

while position <= lenght + 1:
    message = ''
    b = 0

    while b < position:
        if help == True and b == position - 1:
            message += '▌'

            help = False
            position -= 1
        elif help == False and b == position - 1:
            message += '█'

            help = True
            help2 = True
        else:
            message += '█'

        b = b + 1

    if help2 == True and not position > lenght:
        message += '░'
        help2 = False

    for i in range(lenght - position):
        message += '░'
    position += 1
    sleep(0.02)
    print(Colors.gray, f'\r{spacing}|{message}|',end='')

url = 'https://superpatanegra.com/texto/index.php'

while True:
    try:
        requests.get(url)
        print("""
        """)
        Write.Print('    >> [200] Conexión Establecida.', Colors.green, interval=0.01)
        sleep(1)
        break
    except (ConnectionError, ConnectionAbortedError, ConnectionRefusedError, ConnectionResetError, Exception):
        print("""
        """)
        Write.Print('    >> [404] Error de conexión. Reintentando Conexión en 10 segundos...', Colors.red, interval=0.01)
        sleep(10)

enc_types = ['asc2bin', 'bin2asc', 'asc2hex', 'hex2asc', 'bin2hex', 'hex2bin', 'backwards', 'b64enc', 'b64dec', 'caesarbf', 'crypt', 'entityenc', 'entitydec', 'l33t', 'del33t', 'md5', 'igpay', 'unigpay', 'rot-13', 'urlenc', 'urldec']

def __main__():
    os.system('cls')
    print(Center.XCenter(f"""


    {Colors.yellow}[{Colors.light_gray}1{Colors.yellow}] {Colors.white}Texto a Binario                      {Colors.yellow}[{Colors.light_gray}2{Colors.yellow}] {Colors.white}Binario a Texto               {Colors.yellow}[{Colors.light_gray}3{Colors.yellow}] {Colors.white}Texto a Hexadecimal

    {Colors.yellow}[{Colors.light_gray}4{Colors.yellow}] {Colors.white}Hexadecimal a Texto                  {Colors.yellow}[{Colors.light_gray}5{Colors.yellow}] {Colors.white}Binario a Hexadecimal         {Colors.yellow}[{Colors.light_gray}6{Colors.yellow}] {Colors.white}Hexadecimal a Binario

    {Colors.yellow}[{Colors.light_gray}7{Colors.yellow}] {Colors.white}Texto al revés                       {Colors.yellow}[{Colors.light_gray}8{Colors.yellow}] {Colors.white}Base 64 (codificar)           {Colors.yellow}[{Colors.light_gray}9{Colors.yellow}] {Colors.white}Base 64 (descodificar)

    {Colors.yellow}[{Colors.light_gray}10{Colors.yellow}] {Colors.light_red}Cifrado César                       {Colors.yellow}[{Colors.light_gray}11{Colors.yellow}] {Colors.gray}Encriptación DES             {Colors.yellow}[{Colors.light_gray}12{Colors.yellow}] {Colors.white}Entidades HTML (codificar)

    {Colors.yellow}[{Colors.light_gray}13{Colors.yellow}] {Colors.white}Entidades HTML (descodificar)       {Colors.yellow}[{Colors.light_gray}14{Colors.yellow}] {Colors.white}Texto a l33t 5p34k           {Colors.yellow}[{Colors.light_gray}15{Colors.yellow}] {Colors.white}l33t 5p34k a Texto

    {Colors.yellow}[{Colors.light_gray}16{Colors.yellow}] {Colors.gray}Encriptación MD5                    {Colors.yellow}[{Colors.light_gray}17{Colors.yellow}] {Colors.white}Texto a Pig Latin            {Colors.yellow}[{Colors.light_gray}18{Colors.yellow}] {Colors.white}Pig Latin a Texto

    {Colors.yellow}[{Colors.light_gray}19{Colors.yellow}] {Colors.white}Texto a ROT-13                      {Colors.yellow}[{Colors.light_gray}20{Colors.yellow}] {Colors.white}Codificar URL                {Colors.yellow}[{Colors.light_gray}21{Colors.yellow}] {Colors.white}Descodificar URL


    """))
    while True:
        try:
            number = int(Write.Input("    [#] Elección: ", Colors.light_gray, interval=0.01)) - 1
            print()
            break
        except (TypeError, ValueError):
            print()
            Write.Print('    Porvafor, escriba un número válido.', Colors.light_gray, interval=0.01)
            print("""
            """)
            sleep(0.5)

    if number == 9:
        Write.Print('    En desarrollo... ', Colors.light_gray, interval=0.01)
        print()
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
                print()
                Write.Print('    Porvafor, escriba un mensaje válido.', Colors.light_gray, interval=0.01)
                print("""
                """)
                sleep(0.5)
        if len(after_keyword) > 200:
           print(Colors.yellow, f"""
            {after_keyword}
        
            """)
        else:
            Write.Print(f"""
            {after_keyword}
            """, Colors.yellow, interval=0.001)

    print()
    Write.Input('    Pulsa cualquier tecla para continuar: ', Colors.light_gray, interval=0.01)

while True:
    __main__()
