# 5. Napisz funkcję minmax, która zwraca jako swój wynik krotkę dwóch liczb, z których
# pierwsza to minimum a druga to maksimum z listy podanej jako jedyny argument tej
# funkcji. Przykładowo, dla listy a = [31, 28, 31, 30, 31, 30, 31, 31,
# 30, 31, 30, 31] funkcja minmax powinna zwrócić krotkę (28, 31). Przetestuj tę funkcję w funkcji main

def minmax(lista):
    lista.sort()
    print(f'({lista[0]}, {lista[-1]})')


minmax([1, 5, 3,  4, 89, 12, 123, 2])
