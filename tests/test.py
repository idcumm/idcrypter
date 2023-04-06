lines = ['theme = "red_to_blue"\n', 'x = "120\n"','y = "30\n"']
for i in range(len(lines)):
    lines[i] = lines[i].replace('\n', '')
color_shade = lines[0][9:-1]
x = lines[1][5:-1]
y = lines[2][5:-1]
print(color_shade)
print(x)
print(y)