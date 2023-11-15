def czy_nalezy(element, lista):
    for e in lista:
        if e == element:
            return True
    return False


print(czy_nalezy(2, [1, 3, 7]))
