import requests, os, sys, ctypes, warnings
from bs4 import BeautifulSoup, MarkupResemblesLocatorWarning
from time import sleep
from pystyle import Colors, Colorate, Write, Center

warnings.filterwarnings("ignore", category=MarkupResemblesLocatorWarning)

number = 0
color_shade = 'yellow_to_red'
color = 'yellow'
url = 'https://superpatanegra.com/texto/index.php'
url2 = 'https://cifraronline.com/pad'
enc_types = ['asc2bin', 'asc2hex', 'urlenc', 'backwards', 'b64enc', 'caesarbf', 'entityenc', 'rot-13', 'l33t', 'igpay']
enc_types2 = ['aes', 'des', 'rijndael192', 'rijndael256', 'serpent', 'tripledes', 'twofish', 'blowfish', 'cast5', 'cast6', 'gost', 'loki97', 'saferplus', 'xtea']
after_keyword = ''
soup = ''
page = 1

extract = open('data.dll', 'r')
if extract.mode == 'r':
    color_shade = extract.read()
if color_shade == 'yellow_to_red':
    color = 'yellow'
elif color_shade == 'purple_to_blue':
    color = 'purple'
elif color_shade == 'yellow_to_green':
    color = 'light_green'

def eleccion():
    global number
    print( Colors.light_gray, 
        "    >> [#] Elección: ", end='')
    number = input()
    try:
        number = int(number) - 1
    except (TypeError, ValueError):
        number = str(number)
    print()


def progress_bar(len, pos, interval):
    print('\n')
    space = '\t\t\t\t\t     '
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
    global color_shade
    if color_shade == 'yellow_to_red':
        print(Center.XCenter(Colorate.Vertical(Colors.yellow_to_red, """
                               ____  ___      __  ____   __ __  ____  ______    ___  ____  
                              l    j|   \    /  ]|    \ |  T  T|    \|      T  /  _]|    \ 
                               |  T |    \  /  / |  D  )|  |  ||  o  )      | /  [_ |  D  )
                               |  | |  D  Y/  /  |    / |  ~  ||   _/l_j  l_jY    _]|    / 
                               |  | |     /   \_ |    \ l___, ||  |    |  |  |   [_ |    \ 
                               j  l |     \     ||  .  Y|     !|  |    |  |  |     T|  .  Y
                              |____jl_____j\____jl__j\_jl____/ l__j    l__j  l_____jl__j\_j\n""", 1)))
    elif color_shade == 'purple_to_blue':
        print(Center.XCenter(Colorate.Vertical(Colors.purple_to_blue, """
                               ____  ___      __  ____   __ __  ____  ______    ___  ____  
                              l    j|   \    /  ]|    \ |  T  T|    \|      T  /  _]|    \ 
                               |  T |    \  /  / |  D  )|  |  ||  o  )      | /  [_ |  D  )
                               |  | |  D  Y/  /  |    / |  ~  ||   _/l_j  l_jY    _]|    / 
                               |  | |     /   \_ |    \ l___, ||  |    |  |  |   [_ |    \ 
                               j  l |     \     ||  .  Y|     !|  |    |  |  |     T|  .  Y
                              |____jl_____j\____jl__j\_jl____/ l__j    l__j  l_____jl__j\_j\n""", 1)))
    elif color_shade == 'yellow_to_green':
        print(Center.XCenter(Colorate.Vertical(Colors.yellow_to_green, """
                               ____  ___      __  ____   __ __  ____  ______    ___  ____  
                              l    j|   \    /  ]|    \ |  T  T|    \|      T  /  _]|    \ 
                               |  T |    \  /  / |  D  )|  |  ||  o  )      | /  [_ |  D  )
                               |  | |  D  Y/  /  |    / |  ~  ||   _/l_j  l_jY    _]|    / 
                               |  | |     /   \_ |    \ l___, ||  |    |  |  |   [_ |    \ 
                               j  l |     \     ||  .  Y|     !|  |    |  |  |     T|  .  Y
                              |____jl_____j\____jl__j\_jl____/ l__j    l__j  l_____jl__j\_j\n""", 1)))


def enc_options():
    global color
    if color == 'yellow':
        print(Center.XCenter(f"""
\n    {Colors.yellow}[{Colors.light_gray}01{Colors.yellow}] {Colors.white}Binario                             {Colors.yellow}[{Colors.light_gray}02{Colors.yellow}] {Colors.white}Hexadecimal                  {Colors.yellow}[{Colors.light_gray}03{Colors.yellow}] {Colors.white}Cifrado URL
\n    {Colors.yellow}[{Colors.light_gray}04{Colors.yellow}] {Colors.white}Texto al revés                      {Colors.yellow}[{Colors.light_gray}05{Colors.yellow}] {Colors.white}Base 64                      {Colors.yellow}[{Colors.light_gray}06{Colors.yellow}] {Colors.white}Cifrado César
\n    {Colors.yellow}[{Colors.light_gray}07{Colors.yellow}] {Colors.white}Entidades HTML                      {Colors.yellow}[{Colors.light_gray}08{Colors.yellow}] {Colors.white}Cifrado ROT-13               {Colors.yellow}[{Colors.light_gray}09{Colors.yellow}] {Colors.white}l33t 5p34k
\n    {Colors.yellow}[{Colors.light_gray}10{Colors.yellow}] {Colors.white}Pig Latin                           {Colors.yellow}[{Colors.light_gray}11{Colors.yellow}] {Colors.white}AES                          {Colors.yellow}[{Colors.light_gray}12{Colors.yellow}] {Colors.white}DES
\n    {Colors.yellow}[{Colors.light_gray}13{Colors.yellow}] {Colors.white}Rijndael 192                        {Colors.yellow}[{Colors.light_gray}14{Colors.yellow}] {Colors.white}Rijndael 256                 {Colors.yellow}[{Colors.light_gray}15{Colors.yellow}] {Colors.white}Serpent
\n    {Colors.yellow}[{Colors.light_gray}16{Colors.yellow}] {Colors.white}Triple DES                          {Colors.yellow}[{Colors.light_gray}17{Colors.yellow}] {Colors.white}TwoFish                      {Colors.yellow}[{Colors.light_gray}18{Colors.yellow}] {Colors.white}Blowfish
\n    {Colors.yellow}[{Colors.light_gray}19{Colors.yellow}] {Colors.white}CAST5                               {Colors.yellow}[{Colors.light_gray}20{Colors.yellow}] {Colors.white}CAST6                        {Colors.yellow}[{Colors.light_gray}21{Colors.yellow}] {Colors.white}GOST
\n    {Colors.yellow}[{Colors.light_gray}0{Colors.yellow}]  {Colors.light_gray}Configuración                       {Colors.yellow}[{Colors.light_gray}<{Colors.yellow}]  {Colors.light_gray}Anterior Página              {Colors.yellow}[{Colors.light_gray}>{Colors.yellow}]  {Colors.light_gray}Siguiente Página
\n\n"""))
    elif color == 'purple':
        print(Center.XCenter(f"""
\n    {Colors.purple}[{Colors.light_gray}01{Colors.purple}] {Colors.white}Binario                             {Colors.purple}[{Colors.light_gray}02{Colors.purple}] {Colors.white}Hexadecimal                  {Colors.purple}[{Colors.light_gray}03{Colors.purple}] {Colors.white}Cifrado URL
\n    {Colors.purple}[{Colors.light_gray}04{Colors.purple}] {Colors.white}Texto al revés                      {Colors.purple}[{Colors.light_gray}05{Colors.purple}] {Colors.white}Base 64                      {Colors.purple}[{Colors.light_gray}06{Colors.purple}] {Colors.white}Cifrado César
\n    {Colors.purple}[{Colors.light_gray}07{Colors.purple}] {Colors.white}Entidades HTML                      {Colors.purple}[{Colors.light_gray}08{Colors.purple}] {Colors.white}Cifrado ROT-13               {Colors.purple}[{Colors.light_gray}09{Colors.purple}] {Colors.white}l33t 5p34k
\n    {Colors.purple}[{Colors.light_gray}10{Colors.purple}] {Colors.white}Pig Latin                           {Colors.purple}[{Colors.light_gray}11{Colors.purple}] {Colors.white}AES                          {Colors.purple}[{Colors.light_gray}12{Colors.purple}] {Colors.white}DES
\n    {Colors.purple}[{Colors.light_gray}13{Colors.purple}] {Colors.white}Rijndael 192                        {Colors.purple}[{Colors.light_gray}14{Colors.purple}] {Colors.white}Rijndael 256                 {Colors.purple}[{Colors.light_gray}15{Colors.purple}] {Colors.white}Serpent
\n    {Colors.purple}[{Colors.light_gray}16{Colors.purple}] {Colors.white}Triple DES                          {Colors.purple}[{Colors.light_gray}17{Colors.purple}] {Colors.white}TwoFish                      {Colors.purple}[{Colors.light_gray}18{Colors.purple}] {Colors.white}Blowfish
\n    {Colors.purple}[{Colors.light_gray}19{Colors.purple}] {Colors.white}CAST5                               {Colors.purple}[{Colors.light_gray}20{Colors.purple}] {Colors.white}CAST6                        {Colors.purple}[{Colors.light_gray}21{Colors.purple}] {Colors.white}GOST
\n    {Colors.purple}[{Colors.light_gray}0{Colors.purple}]  {Colors.light_gray}Configuración                       {Colors.purple}[{Colors.light_gray}<{Colors.purple}]  {Colors.light_gray}Anterior Página              {Colors.purple}[{Colors.light_gray}>{Colors.purple}]  {Colors.light_gray}Siguiente Página
\n\n"""))
    elif color == 'light_green':
        print(Center.XCenter(f"""
\n    {Colors.light_green}[{Colors.light_gray}01{Colors.light_green}] {Colors.white}Binario                             {Colors.light_green}[{Colors.light_gray}02{Colors.light_green}] {Colors.white}Hexadecimal                  {Colors.light_green}[{Colors.light_gray}03{Colors.light_green}] {Colors.white}Cifrado URL
\n    {Colors.light_green}[{Colors.light_gray}04{Colors.light_green}] {Colors.white}Texto al revés                      {Colors.light_green}[{Colors.light_gray}05{Colors.light_green}] {Colors.white}Base 64                      {Colors.light_green}[{Colors.light_gray}06{Colors.light_green}] {Colors.white}Cifrado César
\n    {Colors.light_green}[{Colors.light_gray}07{Colors.light_green}] {Colors.white}Entidades HTML                      {Colors.light_green}[{Colors.light_gray}08{Colors.light_green}] {Colors.white}Cifrado ROT-13               {Colors.light_green}[{Colors.light_gray}09{Colors.light_green}] {Colors.white}l33t 5p34k
\n    {Colors.light_green}[{Colors.light_gray}10{Colors.light_green}] {Colors.white}Pig Latin                           {Colors.light_green}[{Colors.light_gray}11{Colors.light_green}] {Colors.white}AES                          {Colors.light_green}[{Colors.light_gray}12{Colors.light_green}] {Colors.white}DES
\n    {Colors.light_green}[{Colors.light_gray}13{Colors.light_green}] {Colors.white}Rijndael 192                        {Colors.light_green}[{Colors.light_gray}14{Colors.light_green}] {Colors.white}Rijndael 256                 {Colors.light_green}[{Colors.light_gray}15{Colors.light_green}] {Colors.white}Serpent
\n    {Colors.light_green}[{Colors.light_gray}16{Colors.light_green}] {Colors.white}Triple DES                          {Colors.light_green}[{Colors.light_gray}17{Colors.light_green}] {Colors.white}TwoFish                      {Colors.light_green}[{Colors.light_gray}18{Colors.light_green}] {Colors.white}Blowfish
\n    {Colors.light_green}[{Colors.light_gray}19{Colors.light_green}] {Colors.white}CAST5                               {Colors.light_green}[{Colors.light_gray}20{Colors.light_green}] {Colors.white}CAST6                        {Colors.light_green}[{Colors.light_gray}21{Colors.light_green}] {Colors.white}GOST
\n    {Colors.light_green}[{Colors.light_gray}0{Colors.light_green}]  {Colors.light_gray}Configuración                       {Colors.light_green}[{Colors.light_gray}<{Colors.light_green}]  {Colors.light_gray}Anterior Página              {Colors.light_green}[{Colors.light_gray}>{Colors.light_green}]  {Colors.light_gray}Siguiente Página
\n\n"""))


def enc_options2():
    global color
    if color == 'yellow':
        print(Center.XCenter(f"""
\n    {Colors.yellow}[{Colors.light_gray}22{Colors.yellow}] {Colors.white}Loki97                              {Colors.yellow}[{Colors.light_gray}23{Colors.yellow}] {Colors.white}Safer+                       {Colors.yellow}[{Colors.light_gray}24{Colors.yellow}] {Colors.white}XTEA
\n
\n
\n
\n
\n
\n
\n    {Colors.yellow}[{Colors.light_gray}0{Colors.yellow}]  {Colors.light_gray}Configuración                       {Colors.yellow}[{Colors.light_gray}<{Colors.yellow}]  {Colors.light_gray}Anterior Página              {Colors.yellow}[{Colors.light_gray}>{Colors.yellow}]  {Colors.light_gray}Siguiente Página
\n\n"""))
    elif color == 'purple':
        print(Center.XCenter(f"""
\n    {Colors.purple}[{Colors.light_gray}22{Colors.purple}] {Colors.white}Loki97                              {Colors.purple}[{Colors.light_gray}23{Colors.purple}] {Colors.white}Safer+                       {Colors.purple}[{Colors.light_gray}24{Colors.purple}] {Colors.white}XTEA
\n
\n
\n
\n
\n
\n
\n    {Colors.purple}[{Colors.light_gray}0{Colors.purple}]  {Colors.light_gray}Configuración                       {Colors.purple}[{Colors.light_gray}<{Colors.purple}]  {Colors.light_gray}Anterior Página              {Colors.purple}[{Colors.light_gray}>{Colors.purple}]  {Colors.light_gray}Siguiente Página
\n\n"""))
    elif color == 'light_green':
        print(Center.XCenter(f"""
\n    {Colors.light_green}[{Colors.light_gray}22{Colors.light_green}] {Colors.white}Loki97                              {Colors.light_green}[{Colors.light_gray}23{Colors.light_green}] {Colors.white}Safer+                       {Colors.light_green}[{Colors.light_gray}24{Colors.light_green}] {Colors.white}XTEA
\n
\n
\n
\n
\n
\n
\n    {Colors.light_green}[{Colors.light_gray}0{Colors.light_green}]  {Colors.light_gray}Configuración                       {Colors.light_green}[{Colors.light_gray}<{Colors.light_green}]  {Colors.light_gray}Anterior Página              {Colors.light_green}[{Colors.light_gray}>{Colors.light_green}]  {Colors.light_gray}Siguiente Página
\n\n"""))


def config_options():
    global color
    if color == 'yellow':
        print(Center.XCenter(f"""
    \n    {Colors.yellow}[{Colors.light_gray}1{Colors.yellow}]  {Colors.white}Cambiar el tema                     {Colors.yellow}[{Colors.light_gray}2{Colors.yellow}]  {Colors.white}Test                         {Colors.yellow}[{Colors.light_gray}3{Colors.yellow}]  {Colors.white}Salir
    \n
    \n
    \n
    \n
    \n
    \n
    \n
    \n\n"""))
    elif color == 'purple':
        print(Center.XCenter(f"""
    \n    {Colors.purple}[{Colors.light_gray}1{Colors.purple}]  {Colors.white}Cambiar el tema                     {Colors.purple}[{Colors.light_gray}2{Colors.purple}]  {Colors.white}Test                         {Colors.purple}[{Colors.light_gray}3{Colors.purple}]  {Colors.white}Salir
    \n
    \n
    \n
    \n
    \n
    \n
    \n
    \n\n"""))
    elif color == 'light_green':
        print(Center.XCenter(f"""
    \n    {Colors.light_green}[{Colors.light_gray}1{Colors.light_green}]  {Colors.white}Cambiar el tema                     {Colors.light_green}[{Colors.light_gray}2{Colors.light_green}]  {Colors.white}Test                         {Colors.light_green}[{Colors.light_gray}3{Colors.light_green}]  {Colors.white}Salir
    \n
    \n
    \n
    \n
    \n
    \n
    \n
    \n\n"""))


def config_main():
    global color_shade
    global color
    eleccion()
    if number == 0:
        Write.Print(
            '              [1] Sunset', Colors.orange, interval=0.01)
        print()
        Write.Print(
            '              [2] Night', Colors.purple, interval=0.01)
        print()
        Write.Print(
            '              [3] Nature', Colors.light_green, interval=0.01)
        print('\n')
        eleccion()
        if number == 0:
            color_shade = 'yellow_to_red'
            color = 'yellow'
        if number == 1:
            color_shade = 'purple_to_blue'
            color = 'purple'
        if number == 2:
            color_shade = 'yellow_to_green'
            color = 'light_green'
        storage = open('data.dll', 'w')
        storage.write(color_shade)
        storage.close()

def num_function(numb, _dec):
    global after_keyword
    global page
    global soup
    global number
    Dec = False
    try:
        encrypt = Write.Input(
                '    >> Desea [C] Cifrar o [D] Descifrar el mensaje?: ', Colors.light_gray, interval=0.01)
        if encrypt == 'C' or encrypt == 'c' or encrypt == 'Cifrar':
            encrypt = 'encrypt'
            print()
            text = Write.Input(
                    '    >> Escriba el mensaje que desea encriptar: ', Colors.light_gray, interval=0.01)
        elif encrypt == 'D' or encrypt == 'd' or encrypt == 'Descifrar':
            encrypt = 'decrypt'
            print()
            Dec = True
            text = Write.Input(
                    '    >> Escriba el mensaje que desea desencriptar: ', Colors.light_gray, interval=0.01)
        else:
            encrypt = 'encrypt'
            print()
            text = Write.Input(
                    '    >> Escriba el mensaje que desea encriptar: ', Colors.light_gray, interval=0.01)
        print()
        if text == '':
            text = after_keyword
        if Dec == True:
            r = requests.post(
                url, data={'text': text, 'cryptmethod': _dec, 'submit': 'OK'})
        else:
            r = requests.post(
                url, data={'text': text, 'cryptmethod': enc_types[numb], 'submit': 'OK'})  
        soup = BeautifulSoup(r.text, features='html.parser')
        data = [item.text for item in soup.select('p')]
        keyword = 'TEXTO PROCESADO:'
        before_keyword, keyword, after_keyword = data[1].partition(
            keyword)
        if len(after_keyword) > 200:
            print(Colors.yellow, f'\n    {after_keyword}\n\n')
        else:
            Write.Print(f"""    {after_keyword}
                        """, Colors.yellow, interval=0.001)
        print()
        Write.Input('    >> Pulsa cualquier tecla para continuar: ',
                    Colors.light_gray, interval=0.01)
    except IndexError:
        print()
        
def num(numb):
    global after_keyword
    global page
    global soup
    global number
    try:
        text = Write.Input(
                '    >> Escriba el mensaje que desea encriptar: ', Colors.light_gray, interval=0.01)
        print()
        if text == '':
            text = after_keyword
        r = requests.post(
            url, data={'text': text, 'cryptmethod': enc_types[numb], 'submit': 'OK'})  
        soup = BeautifulSoup(r.text, features='html.parser')
        data = [item.text for item in soup.select('p')]
        keyword = 'TEXTO PROCESADO:'
        before_keyword, keyword, after_keyword = data[1].partition(
            keyword)
        if len(after_keyword) > 200:
            print(Colors.yellow, f'\n    {after_keyword}\n\n')
        else:
            Write.Print(f"""    {after_keyword}
                        """, Colors.yellow, interval=0.001)
        print()
        Write.Input('    >> Pulsa cualquier tecla para continuar: ',
                    Colors.light_gray, interval=0.01)
    except IndexError:
        print()