# Vito chce mieszkać w takim domu że będzie miał najmniej każdej drogi do domu i swojego z powrotem

```python
domy = [1, 2, 4, 5, 7, 10]


def suma(lista):
    wynik = 0
    for i in lista:
        wynik = wynik + i
    return wynik


def odleglosc(lista, a):
    wynik = []
    for i in lista:
        droga = abs(a - i)
        wynik.append(droga)
    return wynik


def rozne_domy(lista):
    wynik = []
    for a in lista:
        wynik.append([suma(odleglosc(lista, a)), a])
    return wynik


print("Odległość, numer domu:", min(rozne_domy(domy)))

```
