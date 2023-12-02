## Ile ujemnych
```python
def ile_ujemnych(lista):
    ile = 0
    for e in lista:
        if e < 0:
            ile = ile + 1
    print(ile)

ile_ujemnych(lista)
```

## Iloczyn
```python
def iloczyn(lista):
    wynik = 1
    for i in lista:
        wynik = wynik * i
    print(wynik)

iloczyn(lista)
```
## minmax
```python
def minmax(lista):
    lista.sort()
    print(f'({lista[0]}, {lista[-1]})')

minmax([lista])
```
## czy należy
```python
def czy_nalezy(element, lista):
    for e in lista:
        if e == element:
            return True
    return False


print(czy_nalezy(element,lista))
```

## czy zawiera
```python
def czy_zawiera(lista, podlista):
    ile_nalezy = 0
    for e in podlista:
        if czy_nalezy(e, lista):
            ile_nalezy += 1
        if ile_nalezy == len(podlista):
            return True
    return False

print(czy_zawiera(lista,podlista))
```
## unikalność
```python
def unikalnosc(lista):
    unikalana = []
    for i in lista:
        if i not in unikalana:
            unikalana.append(i)

    return unikalana

print(unikalnosc(lista1))
```
## dzielniki
```python
def dzielniki(liczba):
    wynik = []
    for i in range(1, liczba+1):
        if liczba % i == 0:
            wynik.append(i)
    return wynik

print(dzielniki(10))
```
## suma elementów listy
```python
def suma(lista):
    wynik = 0
    for i in lista:
        wynik = wynik + i
    return wynik
```
## czy liczba jest doskonała
```python
def czy_doskonala(liczba):
    d = dzielniki(liczba)
    s = suma(d)
    return s == liczba
```
## wszystkie liczby doskonałe od 1 do n
```python
def wszystkie_doskonale(n):
    for i in range(1, n):
        if czy_doskonala(i):
            print(i)
```
## czy liczba jest pierwsza
```python
def liczba_pierwsza(liczba):
    if dzielniki(liczba) == [1]:
        return liczba
```
