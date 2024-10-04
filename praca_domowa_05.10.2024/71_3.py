class Przychodnia:

    def __init__(self, nazwa, miasto):
        self.nazwa = nazwa
        self.miasto = miasto
        self.lista_pacjentow = []

    def dodaj_pacjenta(self, pacjent):
        self.lista_pacjentow.append(pacjent)


class Pacjent:

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
        self.lista_chorob = []

    def dodaj_chorobe(self, choroba):
        self.lista_chorob.append(choroba)

lista_przychodni = []

while True:

    menu = int(input("1- Przychodnia, 2- Pacjent, 3- Koniec"))

    if menu == 1:
        menu1 = int(input("1- dodaj przychodnię, 2 - usuń przychodnię, 3 - dodaj pacjenta do przychodni, 4 – usuń pacjenta z przychodni, 5 - lista przychodni, 6 - lista pacjentów w przychodni"))

        if menu1 == 1:
            nazwa = input("Podaj nazwę przychodni: ")
            miasto = input("Podaj nazwę miasta: ")
            nowa_przychodnia = Przychodnia(nazwa, miasto)
            lista_przychodni.append(nowa_przychodnia)
            print(f"Dodano przychodnię {nazwa} {miasto}.")

        elif menu1 == 2:
            nazwa = input("Podaj nazwę przychodni: ")
            znaleziono = False
            for elem in lista_przychodni:
                if elem.nazwa == nazwa:
                    lista_przychodni.remove(elem)
                    print(f"Usunięto przychodnię {nazwa}.")
                    znaleziono = True
            if not znaleziono:
                print("Nie znaleziono takiej przychodni.")

        elif menu1 == 3:
            nazwa = input("Podaj nazwę przychodni: ")
            znaleziono = False
            for elem in lista_przychodni:
                if elem.nazwa == nazwa:
                    imie = input("Podaj imie pacjenta: ")
                    nazwisko = input("Podaj nazwisko pacjenta: ")
                    nowy_pacjent = Pacjent(imie, nazwisko)
                    elem.lista_pacjentow.append(nowy_pacjent)
                    print(f"Dodano pacjenta {imie} {nazwisko} do przychodni {nazwa}")
                    znaleziono = True
            if not znaleziono:
                print("Nie znaleziono takiej przychodni.")

        elif menu1 == 4:
            nazwa = input("Podaj nazwę przychodni: ")
            znaleziono_pacjenta = False
            znaleziono_przychodnie = False
            for elem in lista_przychodni:
                if elem.nazwa == nazwa:
                    imie = input("Podaj imie pacjenta: ")
                    nazwisko = input("Podaj nazwisko pacjenta: ")
                    znaleziono_przychodnie = True
                    for pacjent in elem.lista_pacjentow:
                        if pacjent.nazwisko == nazwisko and pacjent.imie == imie:
                            elem.lista_pacjentow.remove(pacjent)
                            znaleziono_pacjenta = True
                            print(f"Usunięto pacjenta {imie} {nazwisko} z przychodni {nazwa} {elem.miasto}.")
            if not znaleziono_przychodnie:
                print(f"Nie znaleziono przychodni {nazwa}.")
            elif not znaleziono_pacjenta:
                print(f"Nie znaleziono pacjenta {imie} {nazwisko} w przychodni {nazwa}.")

        elif menu1 == 5:
            for elem in lista_przychodni:
                print(f"Nazwa przychodni: {elem.nazwa}, miasto {miasto}.")

        elif menu1 == 6:
            znaleziono = False
            nazwa = input("Podaj nazwę przychodni: ")
            for elem in lista_przychodni:
                if elem.nazwa == nazwa:
                    znaleziono = True
                    for pacjent in elem.lista_pacjentow:
                        print(f"Imie: {pacjent.imie}, nazwisko: {pacjent.nazwisko}, lista chorób: {pacjent.lista_chorob}.")
            if not znaleziono:
                print(f"Nie znaleziono przychodni {nazwa}.")

    elif menu == 2:
        menu2 = int(input("1- dodaj chorobę pacjentowi, 2- lista chorob pacjenta."))

        if menu2 == 1:
            nazwa_przychodni = input("Podaj nazwę przychodni: ")
            znaleziono_pacjenta = False
            znaleziono_przychodnie = False
            for elem in lista_przychodni:
                if elem.nazwa == nazwa_przychodni:
                    imie = input("Podaj imie pacjenta: ")
                    nazwisko = input("Podaj nazwisko pacjenta: ")
                    znaleziono_przychodnie = True
                    for pacjent in elem.lista_pacjentow:
                        if pacjent.nazwisko == nazwisko and pacjent.imie == imie:
                            nazwa_choroby = input("Podaj nazwę choroby: ")
                            znaleziono_pacjenta = True
                            pacjent.lista_chorob.append(nazwa_choroby)
                            print(f"Dodano chorobę {nazwa_choroby} do listy chorob pacjenta {imie} {nazwisko} w przychodni {nazwa_przychodni}.")
            if not znaleziono_przychodnie:
                print(f"Nie znaleziono przychodni {nazwa_przychodni}.")
            elif not znaleziono_pacjenta:
                print(f"Nie znaleziono pacjenta {imie} {nazwisko} w przychodni {nazwa_przychodni}.")

        elif menu2 == 2:
            nazwa_przychodni = input("Podaj nazwę przychodni: ")
            znaleziono_pacjenta = False
            znaleziono_przychodnie = False
            for elem in lista_przychodni:
                if elem.nazwa == nazwa_przychodni:
                    imie = input("Podaj imie pacjenta: ")
                    nazwisko = input("Podaj nazwisko pacjenta: ")
                    znaleziono_przychodnie = True
                    for pacjent in elem.lista_pacjentow:
                        if pacjent.nazwisko == nazwisko and pacjent.imie == imie:
                            znaleziono_pacjenta = True
                            print(f"Lista chorob pacjenta {imie} {nazwisko}: {pacjent.lista_chorob}.")
            if not znaleziono_przychodnie:
                print(f"Nie znaleziono przychodni {nazwa_przychodni}.")
            if not znaleziono_pacjenta:
                print(f"Nie znaleziono pacjenta {imie} {nazwisko} w przychodni {nazwa_przychodni}.")

    elif menu == 3:
        break

