def main():  # zadanie 3 z zadań pani Agnieszki
    n = int(input('Podaj długość ciągu: '))
    if n > 0:
        pierwszy = float(input('Podaj pierwszy wyraz ciągu: '))
        for p in range(n-1):
            c = float(input('Podaj kolejny wyraz ciągu: '))
            print(c)
        print(pierwszy)


main()


def main():  # zadanie 4 z zadań pani Agnieszki
    p = "Mężny bądź, chroń pułk twój i sześć flag."
    for i in range(64):
        print(p)


main()

rok = int(input('Podaj swój rok urodzenia: '))
print(f'Urodziłes się w roku {rok}.')


def suma(n):
    s = 0
    for i in range(n):
        s += i

    return s


print(suma(5))

WDP = 'WstępDoProgramowania'
print(WDP[:3])
print(WDP[3:])
print(WDP[-1])
print(WDP[-3:])
print(WDP[:-3])
print(WDP[3:2])
print(WDP[3:5])

def odw(kotek):
    w = ""
    for l in kotek:
        w = l + w


    return w
print(odw)

  # wejściówka zadanie 1 i to co było dziś
