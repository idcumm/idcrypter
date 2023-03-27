# afegir encriptacions (AES)
# modificar encriptacio DES i MD5
# Fer menu igual que ATIO
# Fer opcio de diferents numeros en una eleccion#
# cambiar espais per tabuladors

from assets.plugins import *

setTitle('Loading...')
idcrypter()
progress_bar(30, 0, 0.03)

url = 'https://superpatanegra.com/texto/index.php'
url2 = 'https://cifraronline.com/descifrar-aes'
enc_types = ['asc2bin', 'bin2asc', 'asc2hex', 'hex2asc', 'bin2hex', 'hex2bin', 'backwards', 'b64enc', 'b64dec',
             'caesarbf', 'crypt', 'entityenc', 'entitydec', 'l33t', 'del33t', 'md5', 'igpay', 'unigpay', 'rot-13', 'urlenc', 'urldec']
after_keyword = ''
page = 1

print(Colors.white, f'\n\n    >> Intentando establecer la conexión con el servidor...')
while True:
    try:
        requests.get(url)
        print(Colors.green,
              f'   >> [{requests.get(url).status_code}] Conexión con "{url}" establecida.')
        while True:
            try:
                requests.get(url2)
                print(Colors.green,
                      f'   >> [{requests.get(url2).status_code}] Conexión con "{url2}" establecida.')
                break
            except (ConnectionError, ConnectionAbortedError, ConnectionRefusedError, ConnectionResetError, Exception):
                print(Colors.red,
                      f'   >> [404] Error de conexión con {url2}. Reintentando Conexión en 10 segundos...')
                sleep(10)
        break
    except (ConnectionError, ConnectionAbortedError, ConnectionRefusedError, ConnectionResetError, Exception):
        print(Colors.red,
              f'   >> [404] Error de conexión con {url}. Reintentando Conexión en 10 segundos...')
        sleep(10)
clear()
setTitle('idcrypter')
idcrypter()
enc_options()


def __main__():
    global after_keyword
    global page
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
    if type(number) == int:
        if number == -1:
            clear()
            config_options()
            config_main()
        elif number == 9:
            while True:
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
                    break
                except IndexError:
                    Write.Print('    >> Porvafor, escriba un mensaje válido.',
                                Colors.light_red, interval=0.01)
                    print('\n')
                    sleep(0.5)
            for i in range(len(data)):
                keyword = ': '
                before_keyword, keyword, after_keyword = data[i].partition(
                    keyword)
                print(Colors.yellow, f'[+{i+1}]:\t\t{after_keyword}')
            print()
            print()
            Write.Input('    >> Pulsa cualquier tecla para continuar: ',
                        Colors.light_gray, interval=0.01)
        elif number <= 20 and number >= 0:
            while True:
                try:
                    text = Write.Input(
                        '    >> Escriba el mensaje que desea encriptar/desencriptar: ', Colors.light_gray, interval=0.01)
                    print('')
                    if text == '':
                        text = after_keyword
                    r = requests.post(
                        url, data={'text': text, 'cryptmethod': enc_types[number], 'submit': 'OK'})
                    soup = BeautifulSoup(r.text, features='html.parser')
                    data = [item.text for item in soup.select('p')]
                    keyword = 'TEXTO PROCESADO:'
                    before_keyword, keyword, after_keyword = data[1].partition(
                        keyword)
                    break
                except IndexError:
                    Write.Print('    >> Porvafor, escriba un mensaje válido.',
                                Colors.light_red, interval=0.01)
                    print('\n')
                    sleep(0.5)
            if len(after_keyword) > 200:
                print(Colors.yellow, f'\n    {after_keyword}\n\n')
            else:
                Write.Print(f"""    {after_keyword}
                            """, Colors.yellow, interval=0.001)
            print()
            Write.Input('    >> Pulsa cualquier tecla para continuar: ',
                        Colors.light_gray, interval=0.01)
            sleep(0.5)
    clear()
    idcrypter()
    if page == 1:
        enc_options()
    else:
        enc_options2()


while True:
    __main__()
