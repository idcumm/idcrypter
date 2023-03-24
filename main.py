from assets.plugins import *

setTitle('Erección Espontanea')
idcrypter()
progress_bar(30, 0, 0.03)

url = 'https://superpatanegra.com/texto/index.php'
enc_types = ['asc2bin', 'bin2asc', 'asc2hex', 'hex2asc', 'bin2hex', 'hex2bin', 'backwards', 'b64enc', 'b64dec', 'caesarbf', 'crypt', 'entityenc', 'entitydec', 'l33t', 'del33t', 'md5', 'igpay', 'unigpay', 'rot-13', 'urlenc', 'urldec']
after_keyword = ''

print('\n')
Write.Print(f'    >> Intentando establecer la conexión con el servidor...', Colors.white, interval=0.01)
while True:
    try:
        requests.get(url)
        print()
        Write.Print(f'    >> [{requests.get(url).status_code}] Conexión establecida.', Colors.green, interval=0.01)
        sleep(1)
        break
    except (ConnectionError, ConnectionAbortedError, ConnectionRefusedError, ConnectionResetError, Exception):
        print('\n')
        Write.Print('    >> [404] Error de conexión. Reintentando Conexión en 10 segundos...', Colors.red, interval=0.01)
        sleep(10)

clear()
enc_options()
def __main__():
    try:
        number = int(Write.Input("    >> [#] Elección: ", Colors.light_gray, interval=0.01)) - 1
        print()
    except (TypeError, ValueError):
        number = 1000
        print()

    global after_keyword
    if number == 9:
        while True:
            try:
                text = Write.Input('    >> Escriba el mensaje que desea encriptar/desencriptar: ', Colors.light_gray, interval=0.01)
                if text == '':
                    text = after_keyword
                r = requests.post(url, data={'text': text, 'cryptmethod': enc_types[number], 'submit': 'OK'})       
                soup = BeautifulSoup(r.text, features='html.parser')
                data = [item.text for item in soup.select('td')]
                keyword = ': '
                before_keyword, keyword, after_keyword = data[1].partition(keyword)
                break
            except IndexError:
                print()
                Write.Print('    >> Porvafor, escriba un mensaje válido.', Colors.light_red, interval=0.01)
                print('\n')
                sleep(0.5)
        print()
        for i in range(len(data)):
            keyword = ': '
            before_keyword, keyword, after_keyword = data[i].partition(keyword)
            print(Colors.yellow, f'{after_keyword}')
        print()
    elif number > 20 or number < -1:
        print()
        Write.Print('    >> Porvafor, escriba un número válido.', Colors.light_red, interval=0.01)
        print('\n')
        sleep(0.5)
    elif number == -1:
        clear()
        config_options()
        config_main()
    else:
        while True:
            try:
                text = Write.Input('    >> Escriba el mensaje que desea encriptar/desencriptar: ', Colors.light_gray, interval=0.01)
                if text == '':
                    text = after_keyword
                r = requests.post(url, data={'text': text, 'cryptmethod': enc_types[number], 'submit': 'OK'})       
                soup = BeautifulSoup(r.text, features='html.parser')
                data = [item.text for item in soup.select('p')]
                keyword = 'TEXTO PROCESADO:'
                before_keyword, keyword, after_keyword = data[1].partition(keyword)
                break
            except IndexError:
                print()
                Write.Print('    >> Porvafor, escriba un mensaje válido.', Colors.light_red, interval=0.01)
                print('\n')
                sleep(0.5)
        if len(after_keyword) > 200:
           print(Colors.yellow, f'\n{after_keyword}\n\n')
        else:
            Write.Print(f"""
            {after_keyword}
            """, Colors.yellow, interval=0.001)

    print()
    Write.Input('    >> Pulsa cualquier tecla para continuar: ', Colors.light_gray, interval=0.01)
    print()
    
    clear()
    enc_options()

while True:
    __main__()