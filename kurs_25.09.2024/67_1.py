lista = []
indeks = None


while True:

    try:
        liczba1 = int(input("Podaj 1 liczbę całkowitą: "))
    except ValueError:
        print("Podaj poprawną liczbę całkowitą. ")
    else:
        lista.append(liczba1)
        break

while True:
    try:
        liczba2 = float(input("Podaj 2 liczbę rzeczywistą: "))
    except ValueError:
        print("Podaj poprawną liczbę rzeczywistą. ")
    else:
        lista.append(liczba2)
        break

try:
    indeks = int(input("Podaj jaki indeks chcesz pdczytać?"))
except ValueError:
    print("Podaj liczbę 0 lub 1.")
finally:
    print(lista[indeks])


