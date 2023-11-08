import random


def funkcja_rng_numeracja(dlugosc_listy, przedzial_rng, maksimum_dlug):

    lista = []

    for wysylka_do_listy in range(dlugosc_listy):
        lista.append(random.randint(0, przedzial_rng))
    nieposortowana = lista
    numerowane_cyfry_lista = list(enumerate(lista))
    posortowana = sorted(numerowane_cyfry_lista, key=lambda x: x[1], reverse=True)
    bez_numeracji = list(map(lambda x: x[1], posortowana))
    najwieksze = bez_numeracji[:maksimum_dlug]
    return nieposortowana, najwieksze, bez_numeracji


n = int(input("podaj wielkosc listy: "))
rngg = int(input("podaj przedzial generowania liczb: "))
maks_ilosc = int(input("podaj ile liczb najwiekszych chcesz zobaczyc "))
wartosc_rng_funkcja = funkcja_rng_numeracja(n, rngg, maks_ilosc)

print(f'od lewej do prawej lista nie posortowana, posortowana malejaco z ograniczona iloscia,'
      f'posortowane  malejaco \n{wartosc_rng_funkcja}\n')
