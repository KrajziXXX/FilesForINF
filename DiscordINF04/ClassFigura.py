from abc import ABC, abstractmethod
import math

class Figura(ABC):
    @abstractmethod
    def pole(self):
        pass

    @abstractmethod
    def obwod(self):
        pass


class Prostokat(Figura):
    def __init__(self, szerokosc, wysokosc):
        self.szerokosc = szerokosc
        self.wysokosc = wysokosc

    def pole(self):
        return self.szerokosc * self.wysokosc

    def obwod(self):
        return 2 * (self.szerokosc + self.wysokosc)


class Kolo(Figura):
    def __init__(self, promien):
        self.promien = promien

    def pole(self):
        return math.pi * self.promien ** 2

    def obwod(self):
        return 2 * math.pi * self.promien


# Test programu
prostokat = Prostokat(4, 6)
kolo = Kolo(3)

print("Prostokąt:")
print("Pole:", prostokat.pole())
print("Obwód:", prostokat.obwod())

print("\nKoło:")
print("Pole:", round(kolo.pole(), 2))
print("Obwód:", round(kolo.obwod(), 2))
