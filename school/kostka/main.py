import random
class Kosc:
    instancje = 0
    images = ["kosc0.png","kosc1.png","kosc2.png","kosc3.png","kosc4.png","kosc5.png","kosc6.png"]
    oczka = 0
    identyfikator = oczka
    dostepnosc = True
    def __init__(self,oczka= random.randint(1,6)):
        if oczka not in (1,2,3,4,5,6):
            oczka = 0
        self.oczka = oczka
        self.identyfikator = oczka
        self.dostepnosc = True
        Kosc.instancje +=1
    def rzut(self):
        if self.dostepnosc == True:
            self.oczka = random.randint(1,6)
            self.identyfikator = self.oczka
    def blokuj(self):
        self.dostepnosc = False
    def pokaz(self):
        if self.oczka == 1:
            print(f'Wyrzucono {self.oczka}: jeden')
        elif self.oczka == 2:
            print(f"Wyrzucono {self.oczka}: dwa")
        elif self.oczka == 3:
            print(f"Wyrzucono {self.oczka}: trzy")
        elif self.oczka == 4:
            print(f"Wyrzucono {self.oczka}: cztery")
        elif self.oczka == 5:
            print(f"Wyrzucono {self.oczka}:  pięć")
        elif self.oczka == 6:
            print(f"Wyrzucono {self.oczka}: sześć")
        else:
            print(f"Wyrzucono {self.oczka}: zero")

kosc1 = Kosc()
wartosc = int(input("Podaj liczbe oczek: "))
kosc2 = Kosc(wartosc)
print("--------Instancje--------")
print(Kosc.instancje)
print("--------Kość jeden--------")
kosc1.pokaz()
print("--------Kość dwa--------")
kosc2.pokaz()
print("--------Kosc jeden--------")
print(kosc1.images[kosc1.identyfikator])
print("--------Kosc dwa--------")
print(kosc2.images[kosc2.identyfikator])







    