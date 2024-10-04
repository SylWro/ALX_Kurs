class Auto:

    def __init__(self, marka, model, cena, kolor, silnik):
        self.marka = marka
        self.model = model
        self.cena = cena
        self.kolor = kolor
        self.silnik = silnik


auto1 = Auto("Opel", "Astra", 150000, "Czarny", "R4")

auto2 = Auto("Mercedes", "GLE", 550000, "Czarny", "V8")

auto3 = Auto("Audi", "Q8", 750000, "Czarny", "V8")

print(auto1.marka, auto1.model, auto1.cena, auto1.kolor, auto1.silnik)
print(auto2.marka, auto2.model, auto2.cena, auto2.kolor, auto2.silnik)
print(auto3.marka, auto3.model, auto3.cena, auto3.kolor, auto3.silnik)
