wiek = int(input("Podaj Wiek: "))
imie = input("Podaj imie: ")
student = input("Student? (tak/nie): ")

if student.lower() == "tak":
    student = True
    print(True)
else:
    student = False
    print(student)

stalyklient = input("Stały klient? (tak/nie): ")
if stalyklient.lower() == "tak":
    stalyklient = True
    print(True)
else:
    stalyklient = False
    print(student)
bilet = 35
if wiek <= 15:
    bilet = 10
if student == True and wiek<=26:
    bilet = (35*0.5)
if wiek >=65:
    bilet = (35*0.8)
if stalyklient == True and bilet> 10:
    bilet = bilet-10
print(bilet)