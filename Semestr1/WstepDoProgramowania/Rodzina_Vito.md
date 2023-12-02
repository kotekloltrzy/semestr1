# Vito chce mieszkać w takim domu że będzie miał najmniej każdej drogi do domu i swojego z powrotem
#### rodzina Vito
#### sprawdzić odległość podróży między domami 1, 2, 4, 5, 7, 10
#### dodać bez powtarzania
#### porównać każdą kombinajcę
#### wypluć wynik z najmniejszą odległością

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
    for a in lista:
        print("dla domu:", a, "odległość wynosi:", suma(odleglosc(lista, a)))


rozne_domy(domy)
```
