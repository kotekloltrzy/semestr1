```python
d = {}
e = {5: 3, -1: 15}
print(e[5])
d[2000] = 8
print(d)
```

```python
lista1 = [1, 7, 5, 4, 1, 3, 5, -3, 8, 12, 6, 4, 8, 9]


def czestosc(lista):
    wynik = {}
    for e in lista:
        if e in wynik:
            wynik[e] += 1
        else:
            wynik[e] = 1
    return wynik


print(czestosc(lista1))
```
```python
lista1 = 'abrakadabra!'



def same_literki(litera):
    if len(litera) != 1:
        return False
    for i in litera:
        return('A' <= i and i <= 'Z') or ('a' <= i and i <= 'z')


def czestosc(lista):
    wynik = {}
    for e in lista:
        if same_literki(e):
            if e in wynik:
                wynik[e] += 1
            else:
                wynik[e] = 1
    return wynik



print(czestosc(lista1))

```