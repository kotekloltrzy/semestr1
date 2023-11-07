import random
print(random.randint(0, 100))


print("losowa lista")


def losowa_lista(len, start, end):
    lista = []
    for i in range(len):
        tmp = random.randint(start, end)
        lista.append(tmp)
    print(lista)
    return lista


losowa_lista(10, 1, 100)


""""
Zadanie domowe:
lista = generuj(20, 0, 100)
print(lista)
napisać funkcję za pomocą pentli for by się wygenerowała lista
"""
