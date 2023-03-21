from time import sleep


len = 100
pos = 50
for i in range(len + 1 - pos):
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
