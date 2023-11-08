'''
1. Zakładając, iż dana jest lista lista = [], napisać jedną lub dwie instrukcje ite-
racyjne for wypełniające listę lista następującymi liczbami:
(a) 1 2 3 4 5 6 7 8 9 10
(b) 0 2 4 6 8 10 12 14 16 18 20
(c) 1 4 9 16 25 36 49 64 81 100
(d) 0 0 0 0 0 0 0 0 0 0
(e) 0 1 0 1 0 1 0 1 0 1
(f) 0 1 2 3 4 0 1 2 3 4

2. Zrób poprzednie zadanie używając instrukcji iteracyjnej while.

3. Napisz funkcję ile_ujemnych, która zwraca jako swój wynik liczbę ujemnych
elementów listy podanej jako jedyny argument tej funkcji. Przetestuj tę funkcję w
funkcji main.

4. Napisz funkcję iloczyn, która zwraca jako swój wynik iloczyn liczb będących
elementami listy podanej jako jedyny argument tej funkcji. Przetestuj tę funkcję w
funkcji main.

5. Napisz funkcję minmax, która zwraca jako swój wynik krotkę dwóch liczbi, z których
pierwsza to minimum a druga yo maksimum z listy podanej jako jedyny argument tej
funkcji. Przykładowo, dla listy a = [31, 28, 31, 30, 31, 30, 31, 31,
30, 31, 30, 31] funkcja minmax powinna zwrócić krotkę (28, 31). Przete-
stuj tę funkcję w funkcji main
'''

def a():
    lista = []
    a = 1
    for i in range(10):
        lista.append(a)
        a = a + 1
    return lista


print(a())

def b():
    lista = []
    a = 0
    for i in range(11):
        lista.append(a)
        a = a + 2
    return lista


print(b())

def c():
    lista = []
    a = 1
    for i in range(10):
        lista.append(a**2)
        a = a + 1

    return lista


print(c())

def d():
    lista = []
    a = 0
    for i in range(10):
        lista.append(a)

    return lista

print(d())

def e():
    lista = []
    a = 0
    for i in range(10):
        lista.append(a)
        if a == 0:
            a = 1
        else:
            a = 0

    return lista

print(e())

def f():
    lista = []
    a = 0
    for i in range(10):
        lista.append(a)
        if a == 4:
            a = 0
        else:
            a = a +1

    return lista

print (f())
