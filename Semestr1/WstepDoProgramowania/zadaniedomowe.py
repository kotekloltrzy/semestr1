import math

# 1a: sumę wszystkich liczb parzystych od 2 do 100 (włącznie)


def a1(z1, z2):
    odpa1 = 0
    for a in range(z2+1):
        odpa1 += z1
        z1 = z1+2
        if z1 > z2:
            return odpa1


print("zadanie 1a")
print(a1(2, 100))


# sumę kwadratów wszystkich liczb od 1 do 100 (włącznie)

def b1(z3, z4):
    odpb1 = 0
    for b in range(z4+1):
        odpb1 += z3**2
        z3 = z3+1
        if z3 > z4:
            return odpb1


print("zadanie 1b")
print(b1(1, 100))


# sumę potęg liczby 2 dla wykładników od 1 do 63 (włącznie);

def c1(z5, z6):
    odpc1 = 0
    for c in range(z6+1):
        odpc1 += 2**z5
        z5 = z5+1
        if z5 > z6:
            return odpc1


print("zadanie 1c")
print(c1(1, 63))


# sumę wszystkich liczb nieparzystych pomiędzy z9 i z10 (włącznie), gdzie z9 i z10 są zmiennymi, do których
# uprzednio należy wczytać dwie liczby całkowite. Dla z9 > z10 suma powinna wynosić zero.

print("zadanie 1d")


def d1(z9, z10):
    odpd1 = 0
    for d in range(z9, z10, 2):
        odpd1 += z9
        if z9 % 2 == 0:
            z9 = z9 + 1
        else:
            z9 = z9 + 2
    return odpd1


print(d1(1, 14))

"""
Do każdego z poniższych punktów należy napisać odpowiedni program. W każdym z tych
programów wczytać liczbę naturalną n, a następnie wczytując kolejno n liczb rzeczywistych
obliczyć wartość odpowiednich wyrażeń:
"""

print("zadanie 2a")  # a1 + a2 + . . . + an


def zad2a(z11, z12):
    odpa2 = 0
    n = z12
    for a2 in range(n+1):
        odpa2 += z11
        z11 = z11 + 1
    return odpa2


print(zad2a(1, 10))


print("zadanie 2b")  # a1 · a2 · . . . · an


def zad2b(z13, z14):
    odp2b = 1
    n = z14
    for b2 in range(n+1):
        odp2b *= z13
        z13 = z13 + 1
    return odp2b


print(zad2b(1, 10))


print("zadanie 2c")  # |a1| + |a2| + . . . + |an|


def zad2c(z15, z16):
    odp2c = 0
    n = z16
    a = z15
    for c2 in range(n+1):
        odp2c += abs(a)
        a = a + 1
    return odp2c


print(zad2c(-10, 10))


print("zadanie 2d")  # p|a1| +p|a2| + . . . +p|an|


def zad2d(z17, z18):
    odp2d = 0
    n = z18
    a = z17
    for d2 in range(n+1):
        odp2d += a**(1/2)
        a = a + 1
    return odp2d


print(zad2d(1, 10))


print("zadanie 2e")  # |a1| · |a2| · . . . · |an|


def zad2e(z19, z20):
    odp2e = 1
    n = z20
    a = z19
    for e2 in range(n+1):
        odp2e *= abs(a)
        a = a + 1
    return odp2e


print(zad2e(-10, 5))


print("zadanie 2f")  # a1^2 + a2^2 + . . . + an^2


def zad2f(z19, z20):
    odp2f = 0
    n = z20
    a = z19
    for f2 in range(n+1):
        odp2f += a**2
        a = a + 1
    return odp2f


print(zad2f(1, 10))


print("zadanie 2g")  # a1 + a2 + . . . + an oraz a1 · a2 · . . . · an


def zad2g(z21, z22):
    odp2g1 = 0
    odp2g2 = 1
    n1 = z22
    ag1 = z21
    n2 = z22
    ag2 = z21
    for g2_1 in range(n1+1):
        odp2g1 += ag1
        ag1 = ag1 + 1
    for g2_2 in range(n2+1):
        odp2g2 *= ag2
        ag2 = ag2 + 1
    return odp2g1, odp2g2


print(zad2g(1, 10))


print("zadanie 2h")  # a1 − a2 + a3 − . . . + (−1)^n+1· an

# def zad2h(z23, z24):
#     n = z24
#     a = z23
#     iterator = 0
#     odp2h = 0
#     for i in range(a, n+1):
#          if(iterator%2==0):
#            odp2h+=i
#          else:
#            odp2h-=i
#          iterator+=1
#
#     return odp2h
#
# print(zad2h(1, 10))


print("zadanie 2hh")


def zad2hh(zh23, zh24):
    odp2hh = 0
    n = zh24
    a = zh23
    for hh2 in range(n+1):
        if a % 2 == 0:
            odp2hh += a
            a = a+1
        else:
            odp2hh -= a
            a = a+1
    return odp2hh


print(zad2hh(1, 10))


print("zadanie 2i")


def zad2i(z25, z26):
    odp2i = 0
    n = z26
    a = z25
    s = 1
    p = 0
    for i2 in range(n+1):
        if p == 0:
            odp2i += -(a/math.factorial(s))
            s = s + 1
            a = a + 1
            p = p + 1
        elif p == 1:
            odp2i -= -(a/math.factorial(s))
            s = s + 1
            a = a + 1
            p = p - 1
    return odp2i


print(zad2i(1, 5))


print("zadanie 3")
"""
Wczytać liczbę naturalną n, a następnie wczytując kolejno ciąg n liczb rzeczywistych
a1, a2, . . . , an wypisać w kolejnych liniach liczby tego ciągu w następującej kolejności:
a2, a3, . . . , an, a1.
"""


def zad3(n, a3z):
    for trzy in range(n+1):
        a3z = a3z + a3z
        print(a3z)
    return a3z


print("ciąg:", zad3(10, 10))
