```python
import random


def macierze(liczba_wierszy, liczba_kolumn):
    macierz = []
    if czy_kwadratowa(liczba_wierszy, liczba_kolumn):
        for a in range(1, liczba_wierszy + 1):
            wiersz = []
            for kolumny in range(1, liczba_kolumn + 1):
                wiersz.append(random.randint(0, 10))
            macierz.append(wiersz)
    else:
        print('Maciersz nie jest kwadratowa więc nie może być symetryczna')
    return macierz


def czy_kwadratowa(w, k):
    if w == k:
        return True
    else:
        return False


def czy_symetryczna(macierz):
    sprawdzacz1 = []
    sprawdzacz2 = []
    a = 0
    for wiersz in macierz:
        wiersz.pop(a)
        a += 1
        for liczba in wiersz:
            sprawdzacz1.append(liczba)
            sprawdzacz2.append(liczba)
    sprawdzacz2.reverse()
    if sprawdzacz2 == sprawdzacz1:
        print('Są symetryczne')
    else:
        print('Nie są symetryczne')


print(czy_symetryczna(macierze(int(input(f'Podaj liczbę wierszy: ')), int(input(f'Podaj liczbę kolumn: ')))))
```
