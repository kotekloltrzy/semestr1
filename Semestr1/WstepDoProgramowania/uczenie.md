```py
import random


def suma_kwadratow(a):
    suma = 0
    for i in range(a+1):
        suma += i*i
    return suma


print(suma_kwadratow(int(input(f'Podaj zakres liczb: '))))


def ciag_liczb(lista):
    for i in lista:
        if i == '0':
            lista.remove('0')
    lista.sort()
    print(f'Najmniejszy element ciągu: {lista[0]}\nNajwiększy element ciągu: {lista[-1]}')


ciag_liczb(list(input(f'Podaj ciąg liczb: ')))


def odw(slowo):
    wyraz = ""
    for litera in slowo:
        wyraz = litera + wyraz

    return wyraz


print(odw(input(f'Podaj napis do odwrócenia: ')))


def dzielniki(liczba):
    dzielnik = []
    for i in range(1, liczba):
        if liczba % i == 0:
            dzielnik.append(i)
    return dzielnik


def liczba_pierwsza(liczba):
    liczby_pierwsze = []
    for i in range(1, liczba):
        if dzielniki(i) == [1]:
            liczby_pierwsze.append(i)

    return liczby_pierwsze


print(liczba_pierwsza(int(input(f'Podaj zasięg: '))))


def piramida(liczba):
    cegla = 1
    szerokosc = liczba
    grubosc = 1
    for i in range(1, liczba+1):
        print(' '*szerokosc, f'{cegla}'*grubosc)
        cegla += 1
        szerokosc -= 1
        grubosc += 2


piramida(int(input(f'Podaj wysokość piramidy: ')))
n = int(input(f'Podaj liczbę N: '))


wiersz = []
for x in range(n):
    for y in range(n):
        wiersz.append(random.randint(1, 100))


def tablica(lista):
    start = 0
    koniec = n
    for e in range(n):
        for i in lista[start:koniec]:
            print(i, end='\t')
        print()
        koniec += n
        start += n


def transpozycja(lista):
    lista.reverse()
    start = 0
    koniec = n
    for e in range(n):
        for i in lista[start:koniec]:
            print(i, end='\t')
        print()
        koniec += n
        start += n


print(tablica(wiersz))
print(transpozycja(wiersz))

```
