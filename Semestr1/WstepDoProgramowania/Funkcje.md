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

minmax([lista)
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
    ile_zawiera = 0
    for e in podlista:
        for i in lista:
            if e == i:
                ile_zawiera += 1
                break
    if ile_zawiera == len(podlista):
        return True
    else:
        return False

print(czy_zawiera(lista,podlista))
```
