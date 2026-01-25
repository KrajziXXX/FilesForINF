class Device:
    __isNew = True
    battery = 100
    #konstruktor
    def __init__(self,name = "phome",pin=1111):
        self.name = name
        self.__pin = pin
    
    #getter
    @property
    def pin(self):
        return self.__pin
    
    @property
    def isNew(self):
        return self.__isNew
    #Metody
    def display(self):
        print(f"Nazwa urządzenia {self.name}, poziom baterii {self.battery}")
    
    def ifnew(self):
        print(f"urządzenia jest nowe" if self.isNew else "Urządzenie nie jest nowe")
    
    def checkpin(self, pintocheck):
        if self.pin == pintocheck:
            return True
        else:
            return False

#Tworzenie obiektów
samsung = Device()
iphone = Device("Iphone",1312)

#Testowanie
print("----Samsung----")
samsung.display()
samsung.ifnew()
print("Pin: ",samsung.checkpin(1234))

print("\n ----Iphone-----")
iphone.display()
iphone.ifnew()
print("iphone: ",iphone.checkpin(1222))


    