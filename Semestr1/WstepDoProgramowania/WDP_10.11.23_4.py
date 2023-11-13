def czy_zawiera(lista1, lista2):  # czy lista 1 zawiera w sobie liste 2
    print(f'Lista1: {lista1}, Lista2: {lista2}')

    a = 0
    if all(wyrazy in lista1 for wyrazy in lista2):
        a = 1

    if a == 1:
        print("Lista1 zawiera w sobie Listę2.")
    else:
        print("Lista1 nie zawiera w sobie Listy2.")


czy_zawiera([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [5, 7, 8, 9])
