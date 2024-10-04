class Kursant:

    def __init__(self, imie, nazwsiko, telefon):
        self.imie = imie
        self.nazwisko = nazwsiko
        self.telefon = telefon


class Kurs:

    def __init__(self, nazwa, termin):
        self.nazwa = nazwa
        self.termin = termin
        self.listaKursantów = []


listaKursów = []


while True:

    menu = int(input("1-dodaj kurs, 2- pokaz kursy, 3- usun kurs, 4- dodaj kursanta do kursu, 5- wyswietl kursantow z danego kursu, 6- usun kursanta, 7- koniec"))

    if menu == 1:
        nazwa = input("Podaj nazwe kursu: ").lower()
        termin = input("Podaj termin kursu: ").lower()
        nowy_kurs = Kurs(nazwa,termin)
        listaKursów.append(nowy_kurs)

    elif menu == 2:
        for obiekt in listaKursów:
            print(f"Kurs: {obiekt.nazwa}, termin: {obiekt.termin}.")

    elif menu == 3:
        nazwa = input("Podaj nazwe kursu: ")
        znaleziono = False
        for obiekt in listaKursów:
            if nazwa == obiekt.nazwa:
                if len(obiekt.listaKursantów) == 0:
                    listaKursów.remove(obiekt)
                    znaleziono = True
                    print("Usunięto")
                    break
                else:
                    print(f"Kurs {nazwa} ma już zapisanych kursantów")
                    znaleziono = True
        if znaleziono == False:
            print("Nie można znaleźć kursu.")

    elif menu == 4:
        nazwa = input("Podaj nazwe kursu: ")
        znaleziono = False
        for obiekt in listaKursów:
            if nazwa == obiekt.nazwa:
                znaleziono = True
                imie = input("Podaj imie: ")
                nazwisko = input("Podaj naziwsko: ")
                telefon = input("Podaj telefon: ")
                nowy_kursant = Kursant(imie, nazwisko, telefon)
                obiekt.listaKursantów.append(nowy_kursant)
                print(f"Pomyślanie dodano kursanta {imie} {nazwisko} do kursu {nazwa}.")
                break
        if not znaleziono:
            print("Nie znaleziono podanego kursu.")

    elif menu == 5:
        nazwa = input("Podaj nazwe kursu: ")
        znaleziono = False
        for obiekt in listaKursów:
            if obiekt.nazwa == nazwa:
                lista = obiekt.listaKursantów
                znaleziono = True
                for osoba in lista:
                    print(f"Imie: {osoba.imie}, Nazwisko: {osoba.nazwisko}, telefon: {osoba.telefon}.")
                break
        if not znaleziono:
            print("Nie znaleziono takiego kursu.")

    elif menu == 6:
        nazwa = input("Podaj nazwe kursu: ")
        znaleziono = False
        for obiekt in listaKursów:
            if obiekt.nazwa == nazwa:
                nazwisko = input("Podaj naziwsko: ")
                znaleziono = True
                lista = obiekt.listaKursantów
                for osoba in lista:
                    osoba_znaleziona = False
                    if osoba.nazwisko == nazwisko:
                        lista.remove(osoba)
                        print(f"Osoba {osoba.imie} {osoba.nazwisko} została usunięta z kursu {obiekt.nazwa}.")
                        osoba_znaleziona = True
                        break
                break
        if not znaleziono:
            print("Nie znaleziono takiego kursu.")
        elif not osoba_znaleziona:
            print("W wybranym kursie nie ma takiego kursanta.")

    elif menu == 7:
        break

