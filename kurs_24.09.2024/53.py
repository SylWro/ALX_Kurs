słownik = {0 : "zero", 1 : "jeden", 2 : "dwa", 3 : "trzy", 4 : "cztery", 5 : "pięć", 6 : "sześć", 7 : "siedem", 8 : "osiem", 9 : "dziewięć"}

liczba = input("Podaj dowolną liczbę: ")

for num in range(len(liczba)):
    print(słownik[int(liczba[num])])
