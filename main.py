from assets.plugins import *

setTitle('Erección Espontanea')
idcrypter()
progress_bar(30, 0, 0.03)

url = 'https://superpatanegra.com/texto/index.php'
enc_types = ['asc2bin', 'bin2asc', 'asc2hex', 'hex2asc', 'bin2hex', 'hex2bin', 'backwards', 'b64enc', 'b64dec', 'caesarbf', 'crypt', 'entityenc', 'entitydec', 'l33t', 'del33t', 'md5', 'igpay', 'unigpay', 'rot-13', 'urlenc', 'urldec']

while True:
    try:
        requests.get(url)
        print('\n')
        Write.Print(f'    >> [{requests.get(url).status_code}] Conexión Establecida.', Colors.green, interval=0.01)
        sleep(1)
        break
    except (ConnectionError, ConnectionAbortedError, ConnectionRefusedError, ConnectionResetError, Exception):
        print('\n')
        Write.Print('    >> [404] Error de conexión. Reintentando Conexión en 10 segundos...', Colors.red, interval=0.01)
        sleep(10)

def __main__():
    clear()
    enc_options()
    while True:
        try:
            number = int(Write.Input("    >> [#] Elección: ", Colors.light_gray, interval=0.01)) - 1
            print()
            break
        except (TypeError, ValueError):
            print()
            Write.Print('    >> Porvafor, escriba un número válido.', Colors.light_red, interval=0.01)
            print('\n')
            sleep(0.5)

    if number == 9 or number > 20 or number < -1:
        Write.Print('    >> En desarrollo... ', Colors.light_red, interval=0.01)
        print()
    elif number == -1:
        config()
    else:
        while True:
            try:
                text = Write.Input('    >> Escriba el mensaje que desea encriptar/desencriptar: ', Colors.light_gray, interval=0.01)
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

while True:
    __main__()