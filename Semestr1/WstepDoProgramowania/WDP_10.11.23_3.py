def czy_nalezy(element, lista):
    e = 0
    for e in lista:
        if e == element:
            return True
        elif e != element:
            e = e + 1
    if e > len(lista):
        return False


print(czy_nalezy(3, [1, 3, 7]))
