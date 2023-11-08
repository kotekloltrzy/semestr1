import random


def i(od, do):
    lista = []
    ilosc = int(input("Podaj ilosc wyrazow w liscie: "))
    for j in range(ilosc):
        lista.append(random.randint(od, do))
    return lista


print(i(0, 9))
