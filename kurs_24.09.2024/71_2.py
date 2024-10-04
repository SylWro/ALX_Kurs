sklep = {"sok":2.20, "woda":3.30, "cola":5.50}
koszyk = {}
kwota = 0

while True:

    menu = input("D-dodaj produkt do koszyka, P-podglad koszyka, U-usun produkt z koszyka, K-kasa/koniec: ").upper()

    if menu == "D":
        print(sklep)
        produkt = input("Podaj nazwe produktu:")
        if produkt in sklep:
            ile = int(input(f"Ile sztuk produktu {produkt} chciałbyś dodać?"))
            if produkt in koszyk:
                aktualny_stan = koszyk[produkt]
                koszyk[produkt] += ile
            else:
                koszyk[produkt] = ile
        else:
            print("Produktu nie ma w sklepie")

    elif menu == "P":
        if len(koszyk) == 0:
            print("Koszyk jest pusty")
        else:
            for prod in koszyk:
                print(f"{prod} : {koszyk[prod]}")

    elif menu == "U":
        print(koszyk)
        produkt = input("Który produkt chcesz usunąć? ")
        if produkt in koszyk:
            ile = int(input(f"Ile sztuk produktu {produkt} chciałbyś usunąć?"))
            if koszyk[produkt] == ile:
                koszyk.pop(produkt)
            elif koszyk[produkt] > ile:
                aktualny_stan = koszyk[produkt]
                koszyk[produkt] -= ile
            else:
                print(f"Nie ma wystarczającej ilości produktu {produkt}. Ilość {produkt} w koszyku to {koszyk[produkt]}.")
        else:
            print("Nie ma tego produktu w koszyku")

    elif menu == "K":
        for prod in koszyk:
            print(f"Produkt: {prod} : Ilość: {koszyk[prod]} : Cena: {sklep[prod]} : Wartość: {round(sklep[prod] * koszyk[prod],2)}")
            kwota += sklep[prod] * koszyk[prod]
        print(f"Do zapłaty {round(kwota, 2)}")

    else:
        print("Zła komenda.")
