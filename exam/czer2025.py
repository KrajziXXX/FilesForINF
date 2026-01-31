import random

def losowanie(arg):
    tablica = []
    wylosowane = 0
    arg -= 1
    while wylosowane <= arg:
        inside = []
        i = 0
        while i < 6:
            l = random.randrange(1,50)
            inside.append(l)
            i+=1
        tablica.append(inside)
        wylosowane +=1
    return tablica

def wyswietlanie(tablica):
    print("Zestawy wylosowanych liczb:")
    l = 0
    for row in tablica:
        l+=1
        print(f"Losowanie {l}:",end=" ")
        for i in row:
            print(i,end=" ")
        print()

def liczenie(tablica):
    l = 0
    i=0
    while True:
        count = 0
        i+=1
        l+=1
        if i == 50:
            break
        for row in tablica:
            x = row.count(l)
            count += x
        print(f"Wystąpienie liczby {i}: {count}")

print("Ile wygenerować losowań: ")
n = int(input(""))
tab = losowanie(n)
wyswietlanie(tab)
liczenie(tab)
