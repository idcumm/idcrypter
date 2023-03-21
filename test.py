from time import sleep

len = 50
pos = 0
for i in range(len + 1):
    num = 0
    message = ''
    while num < pos:
        message += '█'
        num += 1
    for i in range(len - pos):
        message += '░'
    pos+= 1
    print(f'\r|{message}|', end='')
    sleep(0.02)
print(' Done!')
