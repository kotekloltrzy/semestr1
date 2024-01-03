```python
d = input(f'Podaj hasło które ma co najmniej:\n1) 8 znaków\n'
          f'2) jedną dużą literkę\n3) jeden znak specjalny\n4) jedną cyfrę\nhasło: ')

if len(d) < 8:
    print("Hasło musi mieć conajmniej 8 znaków")


def duze(h):
    ile_duzych = 0
    for i in h:
        if 'A' <= i <= 'Z':
            ile_duzych += 1
    if ile_duzych < 1:
        print("Hasło musi mieć conajmniej jedną dużą literkę")


def specjalne(h):
    ile_specjalnych = 0
    for a in h:
        if '!' <= a <= '/' or ':' <= a <= '@' or '[' <= a <= '`' or '{' <= a <= '”':
            ile_specjalnych += 1
    if ile_specjalnych < 1:
        print("Hasło musi zawierać coznajmniej jeden znak specjalny")


def cyferki(h):
    ile_cyferek = 0
    for b in h:
        if b.isnumeric():
            ile_cyferek += 1
    if ile_cyferek == 0:
        print("Hasło musi zawierać conajmniej jedną cyferkę")


specjalne(d)
cyferki(d)
duze(d)
```
