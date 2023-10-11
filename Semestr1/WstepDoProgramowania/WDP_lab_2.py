"""
1. Do każdego z poniższych punktów należy napisać odpowiedni program obliczający i wypi-
sujący określoną w tym punkcie wartość:
(a) sumę wszystkich liczb parzystych od 2 do 100 (włącznie);
(b) sumę kwadratów wszystkich liczb od 1 do 100 (włącznie);
(cc) funkcję, która liczy n-tą potęgę liczby a;
(c) sumę potęg liczby 2 dla wykładników od 1 do 63 (włącznie);
(d) sumę wszystkich liczb nieparzystych pomiędzy a i b (włącznie), gdzie a i b są zmien-
nymi, do których uprzednio należy wczytać dwie liczby całkowite. Dla a > b suma
powinna wynosić zero.
"""

fruits = ["jabłko", "banan", "wiśnia"]
for fruit in fruits:
    print(fruit)
"""    
fruits - kolekcja
fruit - element
"""

word = "Python"
for letter in word:
    print(letter)

for i in range(2, 5):  # generuje liczby od 2 do 4
    print(i)

for x in range(2, 10, 2):  # generuje co drugą liczbę od 2 do 9
    print(x)

print("zadanie a")
a = 0
for zada in range(2, 101, 2):  # suma liczb parzystych od 2 do 100(włącznie)
    a += zada
print(a)

print("zadanie b")
b = 0
for zadb in range(1, 101):  # suma kwadratow wszystkih liczb od 1 do 100 (włącznie)
    b += zadb**2
print(b)

print('zadanie cc')


def pot1(cc, n):
    wynik = 1
    for zadcc in range(n):  # funkcję, która liczy n-tą potęgę liczby a
        wynik *= cc
    return wynik


print(pot1(2, 4))

print('zadanie c')  # sumę potęg liczby 2 dla wykładników od 1 do 63 (włącznie);


def pot2(c, c2):
    odp = 1
    for zadc in range(c2):
        odp *= c**63
    return odp


print(pot2(2, 4))


print("zadanie d")

"""
sumę wszystkich liczb nieparzystych pomiędzy Da i Db (włącznie), gdzie a i b są zmien-
nymi, do których uprzednio należy wczytać dwie liczby całkowite. Dla Da > Db suma
powinna wynosić zero.
"""

d = 0
Da = 10
Db = 20

if Da > Db:
    d = 0
else:
    for dd in range(Da, Db+1):
        if dd % 2 != 0:
            d += dd

print(d)

# wejściówka: jedno lub dwa zadania z listy pani Agnieszki
