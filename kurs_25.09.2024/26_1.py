lista1 = [2, 5, 7, 9, 12]
lista2 = [66, 5, 23, 11, 9, 100, 2]
powtorzone = []

for x in lista1:
    for y in lista2:
        if x == y:
            powtorzone.append(x)

print(powtorzone)
