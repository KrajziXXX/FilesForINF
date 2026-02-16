class Ksiazka:
    def __init__(self, tytul, autor, rok_wydania):
        self.__tytul = tytul
        self.__autor = autor
        self.__rok_wydania = rok_wydania
        self.__dostepna = True

    def wypozycz(self):
        self.__dostepna = False

    def oddaj(self):
        self.__dostepna = True

    @property
    def tytul(self):
        return self.__tytul
    
    @property
    def czy_dostepna(self):
        return self.__dostepna

    def __str__(self):
        status = "Dostepna" if self.__dostepna else "Niedostepna"
        return f"Tytul: {self.__tytul}, Autor: {self.__autor}, Rok: {self.__rok_wydania}, Status: {status}"


class Biblioteka:
    def __init__(self):
        self.__lista_ksiazek = []

    def dodaj_ksiazke(self, ksiazka):
        self.__lista_ksiazek.append(ksiazka)

    def wypozycz_ksiazke(self, tytul):
        for ksiazka in self.__lista_ksiazek:
            if ksiazka.tytul == tytul:
                ksiazka.wypozycz()

    def oddaj_ksiazke(self, tytul):
        for ksiazka in self.__lista_ksiazek:
            if ksiazka.tytul == tytul:
                ksiazka.oddaj()

    def wyswietl_dostepne(self):
        for ksiazka in self.__lista_ksiazek:
            if ksiazka.czy_dostepna:
                print(ksiazka)

    def wyswietl_wszystkie(self):
        for ksiazka in self.__lista_ksiazek:
            print(ksiazka)


# ===== Program glowny =====

def main():
    biblioteka = Biblioteka()

    k1 = Ksiazka("Wiedzmin", "Andrzej Sapkowski", 1993)
    k2 = Ksiazka("Lalka", "Boleslaw Prus", 1890)
    k3 = Ksiazka("Pan Tadeusz", "Adam Mickiewicz", 1834)

    biblioteka.dodaj_ksiazke(k1)
    biblioteka.dodaj_ksiazke(k2)
    biblioteka.dodaj_ksiazke(k3)

    print("Wszystkie ksiazki:")
    biblioteka.wyswietl_wszystkie()

    print("\nWypozyczenie ksiazki 'Lalka'")
    biblioteka.wypozycz_ksiazke("Lalka")

    print("\nDostepne ksiazki:")
    biblioteka.wyswietl_dostepne()

main()