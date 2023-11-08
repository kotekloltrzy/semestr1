def czy_zawiera(lista1, lista2):  # czy lista 1 zawiera w sobie liste 2
    lista_1 = [1, 2, 3, 4, 5, 6 ,7 ,8 ,9 ,10]
    lista_2 = [5, 7, 8 ,9]
    for e in lista2:
        if not czy_zawiera(lista1, e):
            return False

    return True