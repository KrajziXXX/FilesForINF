# Import klasy ABC oraz dekoratora abstractmethod
from abc import ABC, abstractmethod


# Definicja klasy abstrakcyjnej Pracownik
class Pracownik(ABC):

    # Konstruktor klasy Pracownik
    def __init__(self, imie, nazwisko):
        # Przypisanie imienia pracownika
        self.imie = imie

        # Przypisanie nazwiska pracownika
        self.nazwisko = nazwisko

    # Abstrakcyjna metoda obliczająca pensję
    @abstractmethod
    def oblicz_pensje(self):
        pass


# Definicja klasy PracownikEtatowy dziedziczącej po klasie Pracownik
class PracownikEtatowy(Pracownik):

    # Konstruktor klasy PracownikEtatowy
    def __init__(self, imie, nazwisko, pensja_miesieczna):
        # Wywołanie konstruktora klasy nadrzędnej
        super().__init__(imie, nazwisko)

        # Przypisanie miesięcznej pensji
        self.pensja_miesieczna = pensja_miesieczna

    # Implementacja metody oblicz_pensje
    def oblicz_pensje(self):
        # Zwrócenie stałej pensji miesięcznej
        return self.pensja_miesieczna


# Definicja klasy PracownikGodzinowy dziedziczącej po klasie Pracownik
class PracownikGodzinowy(Pracownik):

    # Konstruktor klasy PracownikGodzinowy
    def __init__(self, imie, nazwisko, stawka_godzinowa, liczba_godzin):
        # Wywołanie konstruktora klasy nadrzędnej
        super().__init__(imie, nazwisko)

        # Przypisanie stawki godzinowej
        self.stawka_godzinowa = stawka_godzinowa

        # Przypisanie liczby przepracowanych godzin
        self.liczba_godzin = liczba_godzin

    # Implementacja metody oblicz_pensje
    def oblicz_pensje(self):
        # Obliczenie pensji na podstawie stawki i liczby godzin
        return self.stawka_godzinowa * self.liczba_godzin


# Test działania programu
p1 = PracownikEtatowy("Jan", "Kowalski", 5000)
p2 = PracownikGodzinowy("Anna", "Nowak", 40, 160)
p3 = PracownikGodzinowy("Piotr", "Zieliński", 35, 120)

# Lista obiektów typu Pracownik
pracownicy = [p1, p2, p3]

# Zmienna przechowująca sumę pensji
suma_pensji = 0

# Pętla iterująca po liście pracowników
for p in pracownicy:
    # Obliczenie pensji pracownika (polimorfizm)
    pensja = p.oblicz_pensje()

    # Wyświetlenie danych pracownika
    print(p.imie, p.nazwisko, "- pensja:", pensja, "zł")

    # Dodanie pensji do sumy
    suma_pensji += pensja

# Wyświetlenie łącznej kwoty wypłat
print("\nŁączna kwota wypłat:", suma_pensji, "zł")
