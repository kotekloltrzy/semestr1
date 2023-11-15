"""
1. czy należy
2. czy zawiera
3. ile ujemnych
"""

lista1 = [1, -2, 3, -4, 5, 6, -7, 8, 9]
lista2 = [9, -2]

print("czy należy")


def czy_nalezy(lista, element):
    for e in lista:
        if e == element:
            return True
    return False


print(czy_nalezy(lista1, 3))

print("ile ujemnych")


def ile_ujemnych(lista):
    ile = 0
    for e in lista:
        if e < 0:
            ile = ile + 1
    print(ile)


ile_ujemnych(lista1)

print("czy zawiera")


def czy_zawiera(lista, podlista):
    for item in podlista:
        if not czy_nalezy(lista, item):
            return False
    return True


print(czy_zawiera(lista1, lista2))
