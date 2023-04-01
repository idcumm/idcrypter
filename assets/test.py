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
color_shade = 'yellow_to_red'
color = 'yellow'
url = 'https://superpatanegra.com/texto/index.php'
url2 = 'https://cifraronline.com/pad'
enc_types = ['asc2bin', 'asc2hex', 'urlenc', 'backwards', 'b64enc', 'caesarbf', 'entityenc', 'rot-13', 'l33t', 'igpay']
enc_types2 = ['aes', 'des', 'rijndael192', 'rijndael256', 'serpent', 'tripledes', 'twofish', 'blowfish', 'cast5', 'cast6', 'gost', 'loki97', 'saferplus', 'xtea']
after_keyword = ''
soup = ''
page = 1

def fun1(_numb, _type):
   global number
   global url
   global enc_types
   global soup
   global text
   try: 
     if text == '':
         text = after_keyword
     if Dec == True:
         r = requests.post(
             url, data={'text': text, 'cryptmethod': _type, 'submit': 'OK'})
     else:
         r = requests.post(
             url, data={'text': text, 'cryptmethod': enc_types[_numb], 'submit': 'OK'})  
     soup = BeautifulSoup(r.text, features='html.parser')
     data = [item.text for item in soup.select('p')]
     keyword = 'TEXTO PROCESADO:'
     before_keyword, keyword, after_keyword = data[1].partition(
         keyword)
     if color == 'yellow':
          print(Colors.yellow, f'\n    Binario: {after_keyword}')
     elif color == 'purple':
          print(Colors.purple, f'\n    Binario: {after_keyword}')
     elif color == 'light_green':
          print(Colors.light_green, f'\n    Binario: {after_keyword}')
   except IndexError:
     print()

if True == True:
   number = 25
   Dec = False
   if number == 25:
      encrypt = Write.Input(
             '    >> Desea [C] Cifrar o [D] Descifrar el mensaje?: ', Colors.light_gray, interval=0.01)
      if encrypt == 'C' or encrypt == 'c' or encrypt == 'Cifrar' or encrypt == 'cifrar':
         encrypt = 'encrypt'
         print()
         text = Write.Input(
                 '    >> Escriba el mensaje que desea cifrar: ', Colors.light_gray, interval=0.01)
      elif encrypt == 'D' or encrypt == 'd' or encrypt == 'Descifrar' or encrypt == 'descifrar':
         encrypt = 'decrypt'
         print()
         Dec = True
         text = Write.Input(
                 '    >> Escriba el mensaje que desea descifrar: ', Colors.light_gray, interval=0.01)
      else:
         encrypt = 'encrypt'
         print()
         text = Write.Input(
                 '    >> Escriba el mensaje que desea cifrar: ', Colors.light_gray, interval=0.01)
      print()
      password = Write.Input(
                        '    >> Escriba una contraseña: ', Colors.light_gray, interval=0.01)
      
      fun1(0, 'bin2asc')
      fun1(1, 'hex2asc')
      fun1(2, 'urldec')
      try:
        if text == '':
            text = after_keyword
        r = requests.post(
            url, data={'text': text, 'cryptmethod': enc_types[3], 'submit': 'OK'})  
        soup = BeautifulSoup(r.text, features='html.parser')
        data = [item.text for item in soup.select('p')]
        keyword = 'TEXTO PROCESADO:'
        before_keyword, keyword, after_keyword = data[1].partition(
            keyword)
        if color == 'yellow':
                print(Colors.yellow, f'\n    Texto al revés: {after_keyword}')
        elif color == 'purple':
                print(Colors.purple, f'\n    Texto al revés: {after_keyword}')
        elif color == 'light_green':
                print(Colors.light_green, f'\n    Texto al revés: {after_keyword}')
      except IndexError:
        print()
        
      try: 
        if text == '':
            text = after_keyword
        if Dec == True:
            r = requests.post(
                url, data={'text': text, 'cryptmethod': "b64dec", 'submit': 'OK'})
        else:
            r = requests.post(
                url, data={'text': text, 'cryptmethod': enc_types[4], 'submit': 'OK'})  
        soup = BeautifulSoup(r.text, features='html.parser')
        data = [item.text for item in soup.select('p')]
        keyword = 'TEXTO PROCESADO:'
        before_keyword, keyword, after_keyword = data[1].partition(
            keyword)
        if color == 'yellow':
             print(Colors.yellow, f'\n    Base 64: {after_keyword}')
        elif color == 'purple':
             print(Colors.purple, f'\n    Base 64: {after_keyword}')
        elif color == 'light_green':
             print(Colors.light_green, f'\n    Base 64: {after_keyword}')
      except IndexError:
        print()
        
      try:
         if text == '':
           text = after_keyword
         r = requests.post(
           url, data={'text': text, 'cryptmethod': 'caesarbf', 'submit': 'OK'})
         soup = BeautifulSoup(r.text, features='html.parser')
         data = [item.text for item in soup.select('td')]
         keyword = ': '
         before_keyword, keyword, after_keyword = data[1].partition(
           keyword)
         if color == 'yellow':
               print(Colors.yellow, '\n    Cifrado César: ')
         elif color == 'purple':
               print(Colors.purple, '\n    Cifrado César: ')
         elif color == 'light_green':
               print(Colors.light_green, '\n    Cifrado César: ')
         for i in range(len(data)):
            keyword = ': '
            before_keyword, keyword, after_keyword = data[i].partition(
               keyword)
            if color == 'yellow':
               print(Colors.yellow, f'    [+{i+1}]:\t\t{after_keyword}')
            elif color == 'purple':
               print(Colors.purple, f'    [+{i+1}]:\t\t{after_keyword}')
            elif color == 'light_green':
               print(Colors.light_green, f'    [+{i+1}]:\t\t{after_keyword}')    
      except IndexError:
         print()
         
      try: 
        if text == '':
            text = after_keyword
        if Dec == True:
            r = requests.post(
                url, data={'text': text, 'cryptmethod': "entitydec", 'submit': 'OK'})
        else:
            r = requests.post(
                url, data={'text': text, 'cryptmethod': enc_types[6], 'submit': 'OK'})  
        soup = BeautifulSoup(r.text, features='html.parser')
        data = [item.text for item in soup.select('p')]
        keyword = 'TEXTO PROCESADO:'
        before_keyword, keyword, after_keyword = data[1].partition(
            keyword)
        if color == 'yellow':
             print(Colors.yellow, f'\n    Entidades HTML: {after_keyword}')
        elif color == 'purple':
             print(Colors.purple, f'\n    Entidades HTML: {after_keyword}')
        elif color == 'light_green':
             print(Colors.light_green, f'\n    Entidades HTML: {after_keyword}')
      except IndexError:
        print()
        
      try:
        if text == '':
            text = after_keyword
        r = requests.post(
            url, data={'text': text, 'cryptmethod': enc_types[7], 'submit': 'OK'})  
        soup = BeautifulSoup(r.text, features='html.parser')
        data = [item.text for item in soup.select('p')]
        keyword = 'TEXTO PROCESADO:'
        before_keyword, keyword, after_keyword = data[1].partition(
            keyword)
        if color == 'yellow':
                print(Colors.yellow, f'\n    ROT-13: {after_keyword}')
        elif color == 'purple':
                print(Colors.purple, f'\n    ROT-13: {after_keyword}')
        elif color == 'light_green':
                print(Colors.light_green, f'\n    ROT-13: {after_keyword}')
      except IndexError:
        print()
        
      try: 
        if text == '':
            text = after_keyword
        if Dec == True:
            r = requests.post(
                url, data={'text': text, 'cryptmethod': "del33t", 'submit': 'OK'})
        else:
            r = requests.post(
                url, data={'text': text, 'cryptmethod': enc_types[8], 'submit': 'OK'})  
        soup = BeautifulSoup(r.text, features='html.parser')
        data = [item.text for item in soup.select('p')]
        keyword = 'TEXTO PROCESADO:'
        before_keyword, keyword, after_keyword = data[1].partition(
            keyword)
        if color == 'yellow':
             print(Colors.yellow, f'\n    l33t 5p34k: {after_keyword}')
        elif color == 'purple':
             print(Colors.purple, f'\n    l33t 5p34k: {after_keyword}')
        elif color == 'light_green':
             print(Colors.light_green, f'\n    l33t 5p34k: {after_keyword}')
      except IndexError:
        print()
        
      try: 
        if text == '':
            text = after_keyword
        if Dec == True:
            r = requests.post(
                url, data={'text': text, 'cryptmethod': "unigpay", 'submit': 'OK'})
        else:
            r = requests.post(
                url, data={'text': text, 'cryptmethod': enc_types[9], 'submit': 'OK'})  
        soup = BeautifulSoup(r.text, features='html.parser')
        data = [item.text for item in soup.select('p')]
        keyword = 'TEXTO PROCESADO:'
        before_keyword, keyword, after_keyword = data[1].partition(
            keyword)
        if color == 'yellow':
             print(Colors.yellow, f'\n    Pig Latin: {after_keyword}')
        elif color == 'purple':
             print(Colors.purple, f'\n    Pig Latin: {after_keyword}')
        elif color == 'light_green':
             print(Colors.light_green, f'\n    Pig Latin: {after_keyword}')
      except IndexError:
        print()
        
        
input()