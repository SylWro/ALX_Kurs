game_on = True
suma = 0
ile = 0

while game_on == True:
    liczba = int(input("Podaj liczbę (0, aby zakończyć): "))
    suma += liczba
    if liczba == 0:
        wynik = suma/ile
        print(wynik)
        game_on = False
    ile += 1
