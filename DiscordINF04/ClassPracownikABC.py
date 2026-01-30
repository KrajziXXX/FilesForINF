from abc import ABC, abstractmethod

class Pracownik(ABC):
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    @abstractmethod
    def oblicz_pensje(self):
        pass


class PracownikEtatowy(Pracownik):
    def __init__(self, imie, nazwisko, pensja_miesieczna):
        super().__init__(imie, nazwisko)
        self.pensja_miesieczna = pensja_miesieczna

    def oblicz_pensje(self):
        return self.pensja_miesieczna


class PracownikGodzinowy(Pracownik):
    def __init__(self, imie, nazwisko, stawka_godzinowa, liczba_godzin):
        super().__init__(imie, nazwisko)
        self.stawka_godzinowa = stawka_godzinowa
        self.liczba_godzin = liczba_godzin

    def oblicz_pensje(self):
        return self.stawka_godzinowa * self.liczba_godzin


# Test programu
p1 = PracownikEtatowy("Jan", "Kowalski", 5000)
p2 = PracownikGodzinowy("Anna", "Nowak", 40, 160)
p3 = PracownikGodzinowy("Piotr", "Zieliński", 35, 120)

pracownicy = [p1, p2, p3]

suma_pensji = 0

for p in pracownicy:
    pensja = p.oblicz_pensje()
    print(p.imie, p.nazwisko, "- pensja:", pensja, "zł")
    suma_pensji += pensja

print("\nŁączna kwota wypłat:", suma_pensji, "zł")
