lista1 = [9, 4, 5, 8, 10]
lista2 = [10, 5, 4]

print("Lista1: " + str(lista1))
print("Lista2: " + str(lista2))

a = 0
if all(wyrazy in lista1 for wyrazy in lista2):
    a = 1

if a == 1:
    print("Lista1 zawiera w sobie Listę2.")
else:
    print("Lista1 nie zawiera w sobie Listy2.")
