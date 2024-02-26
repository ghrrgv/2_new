print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F=((x<=y)==(z<=(not(w))))and(z or y)
                print(x, y, z, w, bool(F))
