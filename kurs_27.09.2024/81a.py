class Pracownik():

    def __init__(self, imie, nazwisko, wynagrodzenie):
        self.__imie = imie
        self.__nazwisko = nazwisko
        self.__wynagrodzenie = wynagrodzenie

    def getImie(self):
        return self.__imie

    def setImie(self, imie):
        self.__imie = imie

    def getNazwisko(self):
        return self.__nazwisko

    def setNazwisko(self, nazwisko):
        self.__nazwisko = nazwisko

    def getWynagrodzenie(self):
        return self.__wynagrodzenie

    def setWynagordzenie(self, wynagrodzenie):
        self.__wynagrodzenie = wynagrodzenie

listaPracownikow = []

while True:

    menu = int(input("1-dodaj pracownika, 2-pokaz pracownikow, 3-usun pracownika"
                         "4-zmien wynagrodzenie, 5-koniec"))

    if menu == 1:
        imie = input("Podaj imie: ")
        nazwisko = input("Podaj nazwisko: ")
        wynagrodzenie = input("Podaj wynagrodzenie pracownika: ")
        nowy_pracownik = Pracownik(imie, nazwisko, wynagrodzenie)
        listaPracownikow.append(nowy_pracownik)

    elif menu == 2:
        for prac in listaPracownikow:
            imie = prac.getImie()
            nazwisko = prac.getNazwisko()
            wynagrodzenie = prac.getWynagrodzenie()
            print(f"Imie: {imie}, Naziwsko: {nazwisko}, Wynagrodzenie: {wynagrodzenie}")

    elif menu == 3:
        nazwisko = input("Podaj nazwisko: ")
        znaleziono = False
        for prac in listaPracownikow:
            if nazwisko == prac.getNazwisko():
                listaPracownikow.remove(prac)
                znaleziono = True
                print("Usunięto pracownika.")
                break
        if not znaleziono:
            print("Nie znaleziono pracownika o podanym nazwisku.")

    elif menu == 4:
        nazwisko = input("Podaj nazwisko: ")
        znaleziono = False
        for prac in listaPracownikow:
            if nazwisko == prac.getNazwisko():
                wynagrodzenie = input("Podaj nowe wynagrodzenie pracownika: ")
                prac.setWynagordzenie(wynagrodzenie)
                znaleziono = True
                print("Zmieniono wynagrodzenie")
                break
        if not znaleziono:
            print("Nie znaleziono pracownika o podanym nazwisku.")


    elif menu == 5:
        break





