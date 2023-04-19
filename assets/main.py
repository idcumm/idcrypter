#             Fer tots a la vegada
# Fer servir Install Forge en comptes de pyinstaller
# Centrar tot
# Arreglar pantalla de carga
# Arreglar pujar pantalla
#             Afegir tema purple_to_red
# Log system
# if lenght > x: Open new cmd

try:
    from plugins import *
except (ImportError, ModuleNotFoundError):
    print('\n   >> Error al intentar importar las dependencias...')
    print('   >> Verifique que el archivo plugins.py se encuentre en el directorio.')
    input('   >> Por favor, presione Enter para salir...')
    exit()

setTitle('Loading...')
idcrypter_start()
sleep(2)

print('\n\n\n\n\n\n\n\n\n\n\n')
print(Colors.light_gray, f'   >> Intentando establecer {__name__}.py como archivo principal...')
if __name__ == '__main__':
    print(Colors.green, f'   >> Archivo {__name__}.py establecido correctamente como archivo principal...')
else:
    print(Colors.red, f'   >> No se ha podido establecer {__name__}.py como archivo principal...')

print(Colors.light_gray, f'   >> Intentando establecer la conexión con {url}...')
while True:
    try:
        requests.get(url)
        print(Colors.green,
              f'   >> [{requests.get(url).status_code}] Conexión con "{url}" establecida.')
        break
    except (ConnectionError, ConnectionAbortedError, ConnectionRefusedError, ConnectionResetError, Exception):
        print(Colors.red,
              f'   >> [404] Error de conexión con {url}. Reintentando conexión en 10 segundos...')
        sleep(10)

print(Colors.light_gray, f'   >> Intentando establecer la conexión con "{url2}"...')
while True:
    try:
        requests.get(url2)
        print(Colors.green,
                f'   >> [{requests.get(url2).status_code}] Conexión con "{url2}" establecida.')
        break
    except (ConnectionError, ConnectionAbortedError, ConnectionRefusedError, ConnectionResetError, Exception):
        print(Colors.red,
                f'   >> [404] Error de conexión con {url2}. Reintentando conexión en 10 segundos...')
        sleep(10)

clear()
setTitle('idcrypter')
idcrypter()
enc_options()

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
        elif color == 'light_red':
            print(Colors.light_red, f'\n    {_name}: {after_keyword}')
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
        elif color == 'light_red':
            print(Colors.light_red, f'\n    {_name}: ')
        for i in range(len(data)):
            keyword = ': '
            before_keyword, keyword, after_keyword = data[i].partition(keyword)
            if color == 'yellow':
                print(Colors.yellow, f'    [+{i+1}]:\t\t{after_keyword}')
            elif color == 'purple':
                print(Colors.purple, f'    [+{i+1}]:\t\t{after_keyword}')
            elif color == 'light_green':
                print(Colors.light_green, f'    [+{i+1}]:\t\t{after_keyword}')
            elif color == 'light_red':
                print(Colors.light_red, f'    [+{i+1}]:\t\t{after_keyword}')  
    except IndexError:
         print()

def __main__():
    global number
    global color_shade
    global color
    global url
    global url2
    global enc_types
    global enc_types2
    global text
    global after_keyword
    global soup
    global page
    global Dec
    print( Colors.light_gray, 
        "   >> [#] Elección: ", end='')
    number = input()
    try:
        number = int(number) - 1
    except (TypeError, ValueError):
        number = str(number)
    print()
    if type(number) == str:
        if number == '>':
            if not page + 1 > 2:
                page += 1
        elif number == '<':
            if not page - 1 < 1:
                page -= 1
    elif type(number) == int:
        if number == -1:
            clear()
            idcrypter()
            config_options()
            config_main()
        elif number == 0:
            num_function(number, 'bin2asc')
        elif number == 1:
            num_function(number, 'hex2asc')
        elif number == 2:
            num_function(number,'urldec')
        elif number == 3:
            num(number)
        elif number == 4:
            num_function(number,'b64dec')
        elif number == 5:
            try:
                text = Write.Input(
                    '    >> Escriba el mensaje que desea cifrar/descifrar: ', Colors.light_gray, interval=0.01)
                print()
                if text == '':
                    text = after_keyword
                r = requests.post(
                    url, data={'text': text, 'cryptmethod': enc_types[number], 'submit': 'OK'})
                soup = BeautifulSoup(r.text, features='html.parser')
                data = [item.text for item in soup.select('td')]
                keyword = ': '
                before_keyword, keyword, after_keyword = data[1].partition(
                    keyword)
                print()
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
                    elif color == 'light_red':
                        print(Colors.light_red, f'    [+{i+1}]:\t\t{after_keyword}')
                print()
                print()
                Write.Input('    >> Pulsa enter para continuar: ',
                            Colors.light_gray, interval=0.01)
            except IndexError:
                print()
        elif number == 6:
            num_function(number,'entitydec')
        elif number == 7:
            num(number)
        elif number == 8:
            num_function(number,'del33t')
        elif number == 9:
            num_function(number,'unigpay')
        elif number >= 10 and number <= 23:
            try:
                number -= len(enc_types)
                encrypt = Write.Input(
                        '    >> Desea [C] Cifrar o [D] Descifrar el mensaje?: ', Colors.light_gray, interval=0.01)
                if encrypt == 'C' or encrypt == 'c' or encrypt == 'Cifrar':
                    encrypt = 'encrypt'
                    print()
                    text = Write.Input(
                            '    >> Escriba el mensaje que desea cifrar: ', Colors.light_gray, interval=0.01)
                elif encrypt == 'D' or encrypt == 'd' or encrypt == 'Descifrar':
                    encrypt = 'decrypt'
                    print()
                    text = Write.Input(
                            '    >> Escriba el mensaje que desea descifrar: ', Colors.light_gray, interval=0.01)
                else:
                    encrypt = 'encrypt'
                    print()
                    text = Write.Input(
                            '    >> Escriba el mensaje que desea cifrar: ', Colors.light_gray, interval=0.01)
                print()
                if text == '':
                    text = after_keyword
                password = Write.Input(
                        '    >> Escriba una contraseña: ', Colors.light_gray, interval=0.01)
                print()
                r = requests.post(url2, data={'c':encrypt, 'text':text, 'pass':password, 'alg':enc_types2[number], 'mode':'ecb', 'hash':'md5', 'iiv':'0'})
                soup = BeautifulSoup(r.text, features='html.parser')
                after_keyword = soup
                if color == 'yellow':
                    Write.Print(f"""    {soup}
                         """, Colors.yellow, interval=0.001)
                elif color == 'purple':
                    Write.Print(f"""    {soup}
                         """, Colors.purple, interval=0.001)
                elif color == 'light_green':
                    Write.Print(f"""    {soup}
                         """, Colors.light_green, interval=0.001)
                elif color == 'light_red':
                    Write.Print(f"""    {soup}
                         """, Colors.light_red, interval=0.001)
                print()
                Write.Input('    >> Pulsa enter para continuar: ',
                            Colors.light_gray, interval=0.01)
            except IndexError:
                print()    
        elif number == 24:
            Dec = False
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
              
            print()
            Write.Input('    >> Pulsa enter para continuar: ',
                        Colors.light_gray, interval=0.01)
    clear()
    idcrypter()
    if page == 1:
        enc_options()
    else:
        enc_options2()


while True:
    __main__()