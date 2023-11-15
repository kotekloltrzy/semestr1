lista1 = [5, 7, 2, 5, 8, 4]


def unikalnosc(lista):
    wynik = []
    for item in lista:
        if not czy_nalezy(wynik, item):
            for e in wynik:
                if e == item:
                    wynik.append(item)
    return wynik


print(unikalnosc(lista1))
