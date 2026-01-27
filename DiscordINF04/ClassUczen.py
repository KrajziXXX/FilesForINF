class Uczen:
    def __init__(self, imie, nazwisko, ocena1, ocena2, ocena3):
        self.imie = imie
        self.nazwisko = nazwisko
        self.ocena1 = ocena1
        self.ocena2 = ocena2
        self.ocena3 = ocena3

    def srednia(self):
        return (self.ocena1 + self.ocena2 + self.ocena3) / 3

    def czy_zdal(self):
        if self.srednia() >= 3.0:
            return "Zdał"
        else:
            return "Nie zdał"


imie = input("Podaj imię: ")
nazwisko = input("Podaj nazwisko: ")

ocena1 = float(input("Podaj pierwszą ocenę: "))
ocena2 = float(input("Podaj drugą ocenę: "))
ocena3 = float(input("Podaj trzecią ocenę: "))

uczen = Uczen(imie, nazwisko, ocena1, ocena2, ocena3)

print("\nDANE UCZNIA")
print("Imię:", uczen.imie)
print("Nazwisko:", uczen.nazwisko)
print("Średnia ocen:", round(uczen.srednia(), 2))
print("Status:", uczen.czy_zdal())
