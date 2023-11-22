def dzielniki(liczba):
    lista = []
    for i in range(1, liczba):
        if liczba % i == 0:
            lista.append(i)
    return lista


def suma(lista):
    wynik = 0
    for i in lista:
        wynik = wynik + i
    return wynik


def czy_doskonala(liczba):
    d = dzielniki(liczba)
    s = suma(d)
    return s == liczba


def zad1b(n):
    for i in range(1, n):
        if czy_doskonala(i):
            print(i)


print(zad1b(int(input(f'Podaj liczbę n: '))))
