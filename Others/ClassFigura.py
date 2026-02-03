# Import klasy ABC i dekoratora abstractmethod
from abc import ABC, abstractmethod

# Import biblioteki math
import math


# Definicja klasy abstrakcyjnej Figura
class Figura(ABC):

    # Abstrakcyjna metoda obliczająca pole figury
    @abstractmethod
    def pole(self):
        pass

    # Abstrakcyjna metoda obliczająca obwód figury
    @abstractmethod
    def obwod(self):
        pass


# Definicja klasy Prostokat dziedziczącej po klasie Figura
class Prostokat(Figura):

    # Konstruktor klasy Prostokat
    def __init__(self, szerokosc, wysokosc):
        # Przypisanie szerokości prostokąta
        self.szerokosc = szerokosc

        # Przypisanie wysokości prostokąta
        self.wysokosc = wysokosc

    # Implementacja metody pole
    def pole(self):
        # Obliczenie pola prostokąta
        return self.szerokosc * self.wysokosc

    # Implementacja metody obwod
    def obwod(self):
        # Obliczenie obwodu prostokąta
        return 2 * (self.szerokosc + self.wysokosc)


# Definicja klasy Kolo dziedziczącej po klasie Figura
class Kolo(Figura):

    # Konstruktor klasy Kolo
    def __init__(self, promien):
        # Przypisanie promienia koła
        self.promien = promien

    # Implementacja metody pole
    def pole(self):
        # Obliczenie pola koła
        return math.pi * self.promien ** 2

    # Implementacja metody obwod
    def obwod(self):
        # Obliczenie obwodu koła
        return 2 * math.pi * self.promien


# Test działania programu
prostokat = Prostokat(4, 6)
kolo = Kolo(3)

# Wyświetlenie danych prostokąta
print("Prostokąt:")
print("Pole:", prostokat.pole())
print("Obwód:", prostokat.obwod())

# Wyświetlenie danych koła
print("\nKoło:")
print("Pole:", round(kolo.pole(), 2))
print("Obwód:", round(kolo.obwod(), 2))
