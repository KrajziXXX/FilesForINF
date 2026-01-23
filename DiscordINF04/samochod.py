class Samochod:
    def __init__(self, marka, model, rok_produkcji):
        self.marka = marka
        self.model = model
        self.rok_produkcji = rok_produkcji

samochody = [
    Samochod("Toyota", "Corolla", 2020),
    Samochod("Honda", "Civic", 2019),
    Samochod("Ford", "Focus", 2018),
    Samochod("BMW", "3 Series", 2021),
    Samochod("Audi", "A4", 2022)
]

# Sortowanie listy samochodów metodą sort()
samochody.sort(key=lambda samochod: samochod.rok_produkcji)

# Wyświetlenie posortowanej listy samochodów
for samochod in samochody:
    print(f"Marka: {samochod.marka}, Model: {samochod.model}, Rok produkcji: {samochod.rok_produkcji}")

