```python
import random


def macierze(liczba_wierszy, liczba_kolumn):
    macierz = []
    for a in range(1, liczba_wierszy + 1):
        wiersz = []
        for kolumny in range(1, liczba_kolumn + 1):
            wiersz.append(random.randint(0, 10))
        macierz.append(wiersz)
    return macierz


def czy_kwadratowa(macierz):
    ilosc_kolumn = 0
    ilosc_wierszy = 0
    for kolumny in macierz:
        ilosc_kolumn += 1
        for wiersze in kolumny:
            ilosc_wierszy += 1
    if ilosc_wierszy == ilosc_kolumn*ilosc_wierszy:
        return True
    else:
        return False


print(czy_kwadratowa(macierze(3, 3)))
```
