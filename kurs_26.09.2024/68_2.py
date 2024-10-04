class Student:

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
        self.oceny = []

    def dodajOcene(self, ocena):
        self.oceny.append(ocena)

    def wypiszOceny(self):
        for x in self.oceny:
            print(x)

    def policzSrednia(self):
        suma = 0
        ile = len(self.oceny)
        for x in self.oceny:
            suma += x
        return suma/ile


listaStudentow = []

while True:

    menu = int(input("1-dodaj studenta, 2-pokaz studentow, 3-usun studenta, "
                     "4-dodaj ocene studentowi, 5-wypisz oceny studenta, 6-wypisz srednia studenta"
                     "7-koniec: "))

    if menu == 1:
        imie = input("Podaj imie: ")
        nazwisko = input("Podaj nazwisko: ")
        nowy_student = Student(imie, nazwisko)
        listaStudentow.append(nowy_student)

    elif menu == 2:
        for x in listaStudentow:
            print(f"Imie: {x.imie} Naziwsko: {x.nazwisko}")

    elif menu == 3:
        nazwisko = input("Podaj nazwisko: ")
        znalezione = False
        for x in listaStudentow:
            if nazwisko == x.nazwisko:
                listaStudentow.remove(x)
                znalezione = True
                print("Usunieto studenta")
                break
        if not znalezione:
            print(f"Nie znaleziono studenta {nazwisko}.")

    elif menu == 4:
        nazwisko = input("Podaj nazwisko: ")
        ocena = int(input("Podaj ocene: "))
        znalezione = False
        for x in listaStudentow:
            if nazwisko == x.nazwisko:
                x.dodajOcene(ocena)
                znalezione = True
                print("dodano ocene")
                break
        if not znalezione:
            print(f"Nie znaleziono studenta {nazwisko}.")

    elif menu == 5:
        nazwisko = input("Podaj nazwisko: ")
        znalezione = False
        for x in listaStudentow:
            if nazwisko == x.nazwisko:
                x.wypiszOceny()
                znalezione = True
                break
        if not znalezione:
            print(f"Nie znaleziono studenta {nazwisko}.")

    elif menu == 6:
        nazwisko = input("Podaj nazwisko: ")
        znalezione = False
        for x in listaStudentow:
            if nazwisko == x.nazwisko:
                print(x.policzSrednia())
                znalezione = True
                break
        if not znalezione:
            print(f"Nie znaleziono studenta {nazwisko}.")

    elif menu == 7:
        break

