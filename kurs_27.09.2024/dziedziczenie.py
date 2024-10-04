# wielodziedziczenie

class TestA:

    def __init__(self, poleA):
        self.__poleA = poleA

    def getPoleA(self):
        return self.__poleA


class Pojazdy(TestA):

    def __init__(self, nazwa, silnik, x):
        super().__init__(x)
        self.nazwa = nazwa
        self.silnik = silnik


class Samolot(Pojazdy):

    def __init__(self, nazwa, silnik, pulap, x):
        super().__init__(nazwa, silnik, x)
        self.pulap = pulap


s1 = Samolot("Boeing", "2345", "345678", "AAAAA")

print(s1.nazwa, s1.silnik, s1.pulap)
print(s1.getPoleA())
 


# metoda SUPER

class A:

    def __init__(self):
        pass

    def hello(self):
        print("A")

class B(A):

    def hello(self):
        print("B")

    def helloA(self):
        super().hello()

ob = B()
ob.hello()
ob.helloA()

