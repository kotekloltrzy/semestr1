import random


def i(ilosc, od, do):
    lista = []
    for j in range(ilosc):
        lista.append(random.randint(od, do))
    print(lista)
    return lista


i(10, 0, 9)
