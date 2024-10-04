lista = [10, 3, 5, 1, 3, 10, 11, 5, 56, 11]
powtorzone = set()

for i, x in enumerate(lista):
    for y in lista[i + 1:]:
        if x == y:
            powtorzone.add(y)

print(powtorzone)
