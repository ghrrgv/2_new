# выражение
# неполная таблица истинности (одной переменной нет)
# найти названия переменных
print('x y z ')
for x in range(2):
    for y in range(2):
        for z in range(2):
            if ((y+z)==(((z*(not(y))))<=(not(x)))) == False :
                print(x, y, z)