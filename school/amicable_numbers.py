n = 5
i = 1
found = []
while True:
    i+=1
    dzielniki = []
    for j in range(1,i):
        if i % j ==0:
            dzielniki.append(j)
    suma=0
    for dzielnik in dzielniki:
        suma += dzielnik
    if suma <= i:
        continue
    dzielniki2 = []
    for j in range(1,suma):
        if suma % j == 0:
            dzielniki2.append(j)
    suma2=0
    for dzielnik in dzielniki2:
        suma2 += dzielnik
    if i == suma2:
        print(f"znaleziono pare{(i,suma)}")
        found.append((i,suma))
    if len(found) >= n:
        break
print(found)
