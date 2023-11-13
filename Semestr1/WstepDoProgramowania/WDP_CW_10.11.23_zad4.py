# 4. Napisz funkcję iloczyn, która zwraca jako swój wynik iloczyn liczb będących
# elementami listy podanej jako jedyny argument tej funkcji. Przetestuj tę funkcję w
# funkcji main.

def iloczyn(lista):
    wynik = 1
    for i in lista:
        wynik = wynik * i
    print(wynik)


iloczyn([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
