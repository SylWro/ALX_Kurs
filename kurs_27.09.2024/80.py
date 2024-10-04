class Produkt:

    def __init__(self, nazwa, cena):
        self.nazwa = nazwa
        self.cena = cena

class Oprogramowanie(Produkt):

    def __init__(self, nazwa, cena, jezyk, system):
        super().__init__(nazwa, cena)
        self.jezyk = jezyk
        self.system = system

class Szkolenia(Oprogramowanie):

    def __init__(self, nazwa, cena, jezyk, system, termin):
        super().__init__(nazwa, cena, jezyk, system)
        self.termin = termin


obiekt1 = Szkolenia("Szkolenie Python", 100, "Python", "Windows", "maj")