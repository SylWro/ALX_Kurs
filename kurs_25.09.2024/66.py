lista = [15, 65, 10, 2, 3, 6, 12, 79, 7, 20]


def calc(list):
    max = list[0]
    min = list[0]
    suma = 0
    parzyste = []
    nieparzyste = []

    for x in list:
        if x > max:
            max = x

        if x < min:
            min = x

        if x % 2 == 0:
            parzyste.append(x)
        else:
            nieparzyste.append(x)

        suma += x
    średnia = suma / len(list)

    return max, min, średnia, len(parzyste), len(nieparzyste)


print(calc(lista))




