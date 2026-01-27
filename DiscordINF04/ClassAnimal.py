class Animal:

    counter = 0
    animals_list=[]

    def __init__(self,weight,age):
        self.weight = weight
        self.age = age
        Animal.counter += 1
        Animal.animals_list.append(self)

class Mammal(Animal):
    def __init__(self, weight, age, can_swim):
        super().__init__(weight, age)
        self.can_swim = can_swim 
    def swim(self):
        if self.can_swim:
            print("to zwierze umie pływać")
        else:
            print("Nie umie pływać")
class dog(Mammal):
    def __init__(self, weight, age, can_swim, breed):
        super().__init__(weight, age, can_swim)
        self.breed = breed
    def fetch(self):
        print("ten pies apartuje")

print(f"ilość zwierząt: {Animal.counter}")
for index, animal in enumerate(Animal.animals_list):
    nr = index + 1
    print(f"Dane o zwierzęciu: {nr}")
    print(f"Gatunek: {animal.species}")
    print(f"Waga: {animal.weight}")
    print(f"Wiek: {animal.age}")