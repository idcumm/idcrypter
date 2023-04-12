from pystyle import Colorate, Colors, Center

# print(Colorate.Horizontal(Colors.yellow_to_red, Center.XCenter('hola como estais?')))

banner = 'hola como estas?, yo muy bien y tu, me alegro de conocerte'
# print(Colorate.Horizontal(Colors.DynamicRGB(255,10,182, 47, 10, 255), 'holla'))

print(Colors.StaticRGB(255,10,182), f'{banner}')
print(Colorate.Horizontal(Colors.DynamicMIX(Colors.purple_to_red), Center.XCenter(f'{banner}')))
input()