import os
try:
    import requests, sys, ctypes, warnings
    from bs4 import BeautifulSoup, MarkupResemblesLocatorWarning
    from time import sleep
    from pystyle import Colors, Colorate, Write, Center
except (ImportError, ModuleNotFoundError):
    print('   >> Instalando dependencias...')
    os.sys('python -m pip install -r requirements.txt')
    
number = 0
color_shade = 'purple_to_blue'
color = 'purple'
url = 'https://superpatanegra.com/texto/index.php'
url2 = 'https://cifraronline.com/pad'
enc_types = ['asc2bin', 'asc2hex', 'urlenc', 'backwards', 'b64enc', 'caesarbf', 'entityenc', 'rot-13', 'l33t', 'igpay']
enc_types2 = ['aes', 'des', 'rijndael192', 'rijndael256', 'serpent', 'tripledes', 'twofish', 'blowfish', 'cast5', 'cast6', 'gost', 'loki97', 'saferplus', 'xtea']
after_keyword = ''
soup = ''
page = 1

def func1(_numb, _type, _name):
    global number
    global url
    global enc_types
    global soup
    global text
    try: 
        if text == '':
            text = after_keyword
        if Dec == True:
            r = requests.post(url, data={'text': text, 'cryptmethod': _type, 'submit': 'OK'})
        else:
            r = requests.post(url, data={'text': text, 'cryptmethod': enc_types[_numb], 'submit': 'OK'})  
        soup = BeautifulSoup(r.text, features='html.parser')
        data = [item.text for item in soup.select('p')]
        keyword = 'TEXTO PROCESADO:'
        before_keyword, keyword, after_keyword = data[1].partition(keyword)
        if color == 'yellow':
            print(Colors.yellow, f'\n    {_name}: {after_keyword}')
        elif color == 'purple':
            print(Colors.purple, f'\n    {_name}: {after_keyword}')
        elif color == 'light_green':
            print(Colors.light_green, f'\n    {_name}: {after_keyword}')
    except IndexError:
        print()
        
def func2(_numb, _name):
    global number
    global url
    global enc_types
    global soup
    global text
    try:
        if text == '':
            text = after_keyword
        r = requests.post(url, data={'text': text, 'cryptmethod': enc_types[_numb], 'submit': 'OK'})  
        soup = BeautifulSoup(r.text, features='html.parser')
        data = [item.text for item in soup.select('p')]
        keyword = 'TEXTO PROCESADO:'
        before_keyword, keyword, after_keyword = data[1].partition(
        keyword)
        if color == 'yellow':
            print(Colors.yellow, f'\n    {_name}: {after_keyword}')
        elif color == 'purple':
            print(Colors.purple, f'\n    {_name}: {after_keyword}')
        elif color == 'light_green':
            print(Colors.light_green, f'\n    {_name}: {after_keyword}')
    except IndexError:
        print()

def func3(_numb, _name):
    global number
    global url
    global enc_types
    global soup
    global text
    try:
        if text == '':
            text = after_keyword
        r = requests.post(url, data={'text': text, 'cryptmethod': enc_types[_numb], 'submit': 'OK'})
        soup = BeautifulSoup(r.text, features='html.parser')
        data = [item.text for item in soup.select('td')]
        keyword = ': '
        before_keyword, keyword, after_keyword = data[1].partition(keyword)
        if color == 'yellow':
            print(Colors.yellow, f'\n    {_name}: ')
        elif color == 'purple':
            print(Colors.purple, f'\n    {_name}: ')
        elif color == 'light_green':
            print(Colors.light_green, f'\n    {_name}: ')
        for i in range(len(data)):
            keyword = ': '
            before_keyword, keyword, after_keyword = data[i].partition(keyword)
            if color == 'yellow':
                print(Colors.yellow, f'    [+{i+1}]:\t\t{after_keyword}')
            elif color == 'purple':
                print(Colors.purple, f'    [+{i+1}]:\t\t{after_keyword}')
            elif color == 'light_green':
                print(Colors.light_green, f'    [+{i+1}]:\t\t{after_keyword}')    
    except IndexError:
         print()
         

if True == True:
    number = 25
    Dec = False
    if number == 25:
        encrypt = Write.Input('    >> Desea [C] Cifrar o [D] Descifrar el mensaje?: ', Colors.light_gray, interval=0.01)
        if encrypt == 'C' or encrypt == 'c' or encrypt == 'Cifrar' or encrypt == 'cifrar':
            encrypt = 'encrypt'
            print()
            text = Write.Input('    >> Escriba el mensaje que desea cifrar: ', Colors.light_gray, interval=0.01)
        elif encrypt == 'D' or encrypt == 'd' or encrypt == 'Descifrar' or encrypt == 'descifrar':
            encrypt = 'decrypt'
            print()
            Dec = True
            text = Write.Input('    >> Escriba el mensaje que desea descifrar: ', Colors.light_gray, interval=0.01)
        else:
            encrypt = 'encrypt'
            print()
            text = Write.Input('    >> Escriba el mensaje que desea cifrar: ', Colors.light_gray, interval=0.01)
        print()
        password = Write.Input('    >> Escriba una contraseña: ', Colors.light_gray, interval=0.01)
      
        func1(0, 'bin2asc', 'Binario')
        func1(1, 'hex2asc', 'Hexadecimal')
        func1(2, 'urldec', 'Cifrado URL')
        func2(3, 'Texto al revés')
        func1(4, 'b64dec', 'Base 64')
        func3(5, 'Cifrado César')
        func1(6, 'entitydec', 'Entidades HTML')
        func2(7, 'Root 13')
        func1(8, 'del33t', 'l33t 5p34k')
        func1(9, 'unigpay', 'Pig Latin')
input()