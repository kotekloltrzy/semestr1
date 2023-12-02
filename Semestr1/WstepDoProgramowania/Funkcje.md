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

