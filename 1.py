n = int(input("Introdu numarul de elemente"))
i = 0
v = []
pare = 0
impare = 0
while n > i :
    v.append(int(input('Introdu numarul {0}'.format(i))))
    i = i + 1
i = 0
while n > i :
    if v[i] % 2 == 0:
        pare = pare + 1
    else :
        impare = impare + 1
    i = i + 1
print('Sunt {0} numere pare si {1} numere impare'.format(pare,impare))