class Pracownik:

    def __init__(self, imie, nazwisko, email, telefon):

        self.imie = imie
        self.nazwisko = nazwisko
        self.email = email
        self. telefon = telefon


listaPracownikow = []

while True:

    menu = int(input("1-dodaj, 2-pokaz, 3-usun, 4-zmien, 5-koniec"))

    if menu == 1:
        imie = input("Podaj imie: ").lower()
        nazwisko = input("Podaj nazwisko: ").lower()
        email = input("Podaj email: ").lower()
        telefon = input("Podaj telefon: ").lower()

        pracownik = Pracownik(imie, nazwisko, email, telefon)
        listaPracownikow.append(pracownik)
        print("Pracownik został dodany")

    elif menu == 2:
        for prac in listaPracownikow:
            print(f"Imię:{prac.imie} , Naziwsko :{prac.nazwisko}, Email: {prac.email}, Telefon: {prac.telefon}.")

    elif menu == 3:
        nazwisko = input("Podaj nazwisko: ").lower()
        found = False
        for prac in listaPracownikow:
            if nazwisko == prac.nazwisko:
                listaPracownikow.remove(prac)
                found = True
                print(f"Pracownik {nazwisko} został usunięty.")
                break

        if not found:
            print(f"Nie znaleziono pracownika o nazwisku {nazwisko}")

    elif menu == 4:
        nazwisko = input("Podaj nazwisko: ")
        found = False
        for prac in listaPracownikow:
            if nazwisko == prac.nazwisko:
                prac.imie = input("Podaj nowe imie: ")
                prac.nazwisko = input("Podaj nowe nazwisko: ")
                prac.email = input("Podaj nowy email: ")
                prac.telefon = input("Podaj nowy telefon: ")
                found = True
                print(f"Dane pracownika {nazwisko} zostały zmienione.")
                break

        if not found:
            print(f"Nie znaleziono pracownika o nazwisku {nazwisko}")

    elif menu == 5:
        break