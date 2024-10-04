class Pojazd:

    def __init__(self, waga, mocSilnika, kolor, liczbaPasazerow, cena):
        self.waga = waga
        self.mocSilnika = mocSilnika
        self.kolor = kolor
        self.liczbaPasazerow = liczbaPasazerow
        self.cena = cena


class PojazdKolowy(Pojazd):

    def __init__(self, waga, mocSilnika, kolor, liczbaPasazerow, cena, liczbaKol):
        super().__init__(waga, mocSilnika, kolor, liczbaPasazerow, cena)
        self.liczbaKol = liczbaKol


class Lodz(Pojazd):

    def __init__(self, waga, mocSilnika, kolor, liczbaPasazerow, cena, zanurzenie):
        super().__init__(waga, mocSilnika, kolor, liczbaPasazerow, cena)
        self.zanurzenie = zanurzenie


class Samolot(Pojazd):

    def __init__(self, waga, mocSilnika, kolor, liczbaPasazerow, cena, pulap):
        super().__init__(waga, mocSilnika, kolor, liczbaPasazerow, cena)
        self.pulap = pulap


class Samochod(PojazdKolowy):

    def __init__(self, waga, mocSilnika, kolor, liczbaPasazerow, cena, liczbaKol, typFelg):
        super().__init__(waga, mocSilnika, kolor, liczbaPasazerow, cena, liczbaKol)
        self.typFelg = typFelg


class Motocykl(PojazdKolowy):
    def __init__(self, waga, mocSilnika, kolor, liczbaPasazerow, cena, liczbaKol, bagaznikNaKask):
        super().__init__(waga, mocSilnika, kolor, liczbaPasazerow, cena, liczbaKol)
        self.bagaznikNaKask = bagaznikNaKask


volvo = Samochod("3.5t", "300 KM", "Czarny", "5", "300 000 pln", "4", "aluminium")
print(volvo.mocSilnika, volvo.liczbaKol, volvo.typFelg)


