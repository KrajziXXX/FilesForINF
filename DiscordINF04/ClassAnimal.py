# Definicja klasy Animal (klasa bazowa)
class Animal:

    # Zmienna klasowa przechowująca liczbę utworzonych obiektów
    counter = 0

    # Lista przechowująca wszystkie obiekty klasy Animal
    animals_list = []

    # Konstruktor klasy Animal
    def __init__(self, weight, age):
        # Przypisanie wagi zwierzęcia
        self.weight = weight

        # Przypisanie wieku zwierzęcia
        self.age = age

        # Zwiększenie licznika zwierząt
        Animal.counter += 1

        # Dodanie obiektu do listy zwierząt
        Animal.animals_list.append(self)


# Definicja klasy Mammal dziedziczącej po klasie Animal
class Mammal(Animal):

    # Konstruktor klasy Mammal
    def __init__(self, weight, age, can_swim):
        # Wywołanie konstruktora klasy nadrzędnej
        super().__init__(weight, age)

        # Informacja czy ssak potrafi pływać
        self.can_swim = can_swim 

    # Metoda sprawdzająca umiejętność pływania
    def swim(self):
        if self.can_swim:
            print("to zwierze umie pływać")
        else:
            print("Nie umie pływać")


# Definicja klasy dog dziedziczącej po klasie Mammal
class dog(Mammal):

    # Konstruktor klasy dog
    def __init__(self, weight, age, can_swim, breed):
        # Wywołanie konstruktora klasy nadrzędnej
        super().__init__(weight, age, can_swim)

        # Przypisanie rasy psa
        self.breed = breed

    # Metoda charakterystyczna dla psa
    def fetch(self):
        print("ten pies apartuje")


# Wyświetlenie liczby utworzonych zwierząt
print(f"ilość zwierząt: {Animal.counter}")

# Iteracja po liście wszystkich zwierząt
for index, animal in enumerate(Animal.animals_list):
    # Numer porządkowy zwierzęcia
    nr = index + 1

    # Wyświetlenie danych o zwierzęciu
    print(f"Dane o zwierzęciu: {nr}")
    print(f"Gatunek: {animal.species}")
    print(f"Waga: {animal.weight}")
    print(f"Wiek: {animal.age}")
