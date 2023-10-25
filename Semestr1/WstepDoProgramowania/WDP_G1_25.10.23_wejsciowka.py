def main():  # suma kwadratów od 1 do n

    suma = 0
    n = int(input('Podaj liczbę naturalna: '))
    for i in range(n+1):
        suma += i**2

    print(f'Suma kwadratów od 1 do {n} rowna się: {suma}')
    return suma


main()


def kwadraty(n):
    suma = 0
    for i in range(n+1):
        suma += i**2
    return suma


print(kwadraty(100))
