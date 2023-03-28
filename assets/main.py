# afegir encriptacions
# ordenar encriptaions
# modificar encriptacio DES i MD5
# Fer opcio de diferents numeros en una eleccion

from plugins import *

setTitle('Loading...')
idcrypter()
progress_bar(30, 0, 0.03)

if __name__ == '__main__':
    print(Colors.white, f'\n\n    >> Conexión con el archivo {__name__}.py establecida...')
print(Colors.white, '   >> Intentando establecer la conexión con el servidor...')
while True:
    try:
        requests.get(url)
        print(Colors.green,
              f'       >> [{requests.get(url).status_code}] Conexión con "{url}" establecida.')
        while True:
            try:
                requests.get(url2)
                print(Colors.green,
                      f'       >> [{requests.get(url2).status_code}] Conexión con "{url2}" establecida.')
                break
            except (ConnectionError, ConnectionAbortedError, ConnectionRefusedError, ConnectionResetError, Exception):
                print(Colors.red,
                      f'       >> [404] Error de conexión con {url2}. Reintentando Conexión en 10 segundos...')
                sleep(10)
        break
    except (ConnectionError, ConnectionAbortedError, ConnectionRefusedError, ConnectionResetError, Exception):
        print(Colors.red,
              f'       >> [404] Error de conexión con {url}. Reintentando Conexión en 10 segundos...')
        sleep(10)
clear()
setTitle('idcrypter')
idcrypter()
enc_options()


def __main__():
    global after_keyword
    global page
    global soup
    number = Write.Input(
        "    >> [#] Elección: ", Colors.light_gray, interval=0.01)
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
        elif number == 9:
            try:
                text = Write.Input(
                    '    >> Escriba el mensaje que desea encriptar/desencriptar: ', Colors.light_gray, interval=0.01)
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
                    print(Colors.yellow, f'[+{i+1}]:\t\t{after_keyword}')
                print()
                print()
                Write.Input('    >> Pulsa cualquier tecla para continuar: ',
                            Colors.light_gray, interval=0.01)
            except IndexError:
                print()
        elif number <= 16 and number >= 0:
            try:
                text = Write.Input(
                    '    >> Escriba el mensaje que desea encriptar/desencriptar: ', Colors.light_gray, interval=0.01)
                print()
                if text == '':
                    text = after_keyword
                r = requests.post(
                    url, data={'text': text, 'cryptmethod': enc_types[number], 'submit': 'OK'})
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
        elif number >= 17 and number <= 30:
            try:
                number -= 17
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
                    text = Write.Input(
                            '    >> Escriba el mensaje que desea desencriptar: ', Colors.light_gray, interval=0.01)
                print()
                if text == '':
                    text = after_keyword
                    if after_keyword == '':
                        text = soup
                password = Write.Input(
                        '    >> Escriba una contraseña: ', Colors.light_gray, interval=0.01)
                print()
                r = requests.post(url2, data={'c':encrypt, 'text':text, 'pass':password, 'alg':enc_types2[number], 'mode':'ecb', 'hash':'md5', 'iiv':'0'})
                soup = BeautifulSoup(r.text, features='html.parser')           
                Write.Print(f"""    {soup}
                         """, Colors.yellow, interval=0.001)
                print()
                Write.Input('    >> Pulsa cualquier tecla para continuar: ',
                            Colors.light_gray, interval=0.01)
            except IndexError:
                print()    
    clear()
    idcrypter()
    if page == 1:
        enc_options()
    else:
        enc_options2()


while True:
    __main__()
