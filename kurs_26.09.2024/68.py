class Zawodnik:

    def __init__(self, imie, wzrost, waga):
        self.imie = imie
        self.wzrost = wzrost
        self.waga = waga
        # self.bmi = None

    def oblicz_bmi(self):
        bmi = self.waga/self.wzrost**2
        return bmi



z1 = Zawodnik("A", 1.6, 67)
print(z1.oblicz_bmi())
