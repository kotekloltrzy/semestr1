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
# d = {}
# e = {5: 3, -1: 15}
# print(e[5])
# d[2000] = 8
# print(d)


lista1 = 'abrakadabra!'


def czestosc(lista):
    wynik = {}
    for e in lista:
        if e in wynik:
            wynik[e] += 1
        else:
            wynik[e] = 1
    return wynik


print(czestosc(lista1))


def same_literki(litera):
    if len(litera) != 1:
        return False
    for i in litera:
        return('A' <= i and i <= 'Z') or ('a' <= i and i <= 'z')


def zadanie(lista):
    wynik = {}
    for i in lista:
        if same_literki(i):
            wynik[i] = czestosc(i)
    return wynik


print(zadanie(lista1))
```
