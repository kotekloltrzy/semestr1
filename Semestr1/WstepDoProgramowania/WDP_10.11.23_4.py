def czy_zawiera(lista1,lista2,element):
    for e in lista2:
        if not czy_zawiera(lista1,e):
            return False
    return True
