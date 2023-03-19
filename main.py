import requests, os
from bs4 import BeautifulSoup
from time import sleep

os.system('@echo off')
os.system('color c')

print("""
                             ____  ___      __  ____   __ __  ____  ______    ___  ____  
                            l    j|   \    /  ]|    \ |  T  T|    \|      T  /  _]|    \ 
                             |  T |    \  /  / |  D  )|  |  ||  o  )      | /  [_ |  D  )
                             |  | |  D  Y/  /  |    / |  ~  ||   _/l_j  l_jY    _]|    / 
                             |  | |     /   \_ |    \ l___, ||  |    |  |  |   [_ |    \ 
                             j  l |     \     ||  .  Y|     !|  |    |  |  |     T|  .  Y
                            |____jl_____j\____jl__j\_jl____/ l__j    l__j  l_____jl__j\_j

                                                            
""")

os.system('title idcum - Encrypter')

spacing = '                                                 '
starting_message = '▌░░░░░░░░░░░░'
lenght = len(starting_message)
last_digit = starting_message[lenght-1]
print(f'\r{spacing}|{starting_message}{last_digit}|',end='')
position = starting_message.find('▌') + 1
contra2 = False
contra = False
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

    final = lenght - position

    for i in range(final):
        message = message + '░'
    position = position + 1
    sleep(0.05)
    print(f'\r{spacing}|{message}|',end='')

url = 'https://superpatanegra.com/texto/index.php'

enc_types = ['asc2bin', 'bin2asc', 'asc2hex', 'hex2asc', 'bin2hex', 'hex2bin', 'backwards', 'b64enc', 'b64dec', 'caesarbf', 'crypt', 'entityenc', 'entitydec', 'l33t', 'del33t', 'md5', 'igpay', 'unigpay', 'rot-13', 'urlenc', 'urldec']

def __main__():
    os.system('cls')
    print(f"""


    [1] Texto a Binario                      [2] Binario a Texto               [3] Texto a Hexadecimal

    [4] Hexadecimal a Texto                  [5] Binario a Hexadecimal         [6] Hexadecimal a Binario

    [7] Texto al revés                       [8] Base 64 (codificar)           [9] Base 64 (descodificar)

    [10] Cifrado César                       [11] Encriptación DES             [12] Entidades HTML (codificar)

    [13] Entidades HTML (descodificar)       [14] Texto a l33t 5p34k           [15] l33t 5p34k a Texto

    [16] Encriptación MD5                    [17] Texto a Pig Latin            [18] Pig Latin a Texto

    [19] Texto a ROT-13                      [20] Codificar URL                [21] Descodificar URL


    """)

    number = int(input('[#] Elección: ')) - 1

    text = input(f'Escriba el texto que desea encriptar/desencriptar: ')
    r = requests.post(url, data={'text': text, 'cryptmethod': enc_types[number], 'submit': 'OK'})
    soup = BeautifulSoup(r.text, features='html.parser')
    data = [item.text for item in soup.select('p')]
    keyword = 'TEXTO PROCESADO:'
    before_keyword, keyword, after_keyword = data[1].partition(keyword)

    print(f"""
    {after_keyword}
    """)

    input('Pulsa cualquier tecla para continuar: ')

true = True
while true == True:
    __main__()