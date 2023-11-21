lista1 = [1, 2, 3, 4, 5, 6, 6, 7, 8, 9, 10]


def unikalnosc(lista):
    wynik = []
    for element in lista:
        if element not in wynik:
            wynik.append(element)
    return wynik


print(unikalnosc(lista1))
