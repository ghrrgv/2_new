# *выражение*
# *таблица истинности*
# результаты F все тождественно ложные (в таблице в результатах везде 0)
print('x y z w')
for x in range(2): # потому что есть только два варианта 0, 1
#таким образом переберём все варианты для каждой переменной.
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not((z*(not(x)))+w+(not(y))):
                    print(x, y, z, w)