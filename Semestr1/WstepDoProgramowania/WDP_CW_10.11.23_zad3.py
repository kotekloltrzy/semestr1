
# 3. Napisz funkcję ile_ujemnych, która zwraca jako swój wynik liczbę ujemnych
# elementów listy podanej jako jedyny argument tej funkcji. Przetestuj tę funkcję w
# funkcji main.


def ile_ujemnych(lista):
    ile = 0
    for e in lista:
        if e < 0:
            ile = ile + 1
    print(ile)


ile_ujemnych([1, 7, -2])
