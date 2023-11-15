lista1 = [5, 3, 1, 4, 2]
lista2 = [1, 3]

def czy_zawiera(lis1, lis2):
    ile_zawiera = 0
    for x2 in lis2:
        for x1 in lis1:
            if x2 == x1:
                ile_zawiera += 1
                break
    if ile_zawiera == len(lis2):
        return True
    else:
        return False

print(lista1)
print(lista2)
print(czy_zawiera(lista1, lista2))
