def wczytaj_dane(nazwa_pliku):
    dane = []
    try:
        with open(nazwa_pliku, "r", encoding="utf-8") as plik:
            for linia in plik:
                elementy = linia.strip().split()
                imie = elementy[0]
                nazwisko = elementy[1]
                oceny = list(map(int, elementy[2:]))
                dane.append({
                    "imie": imie,
                    "nazwisko": nazwisko,
                    "oceny": oceny
                })
        return dane
    except FileNotFoundError:
        print("Blad: Plik nie istnieje.")
        return None

def oblicz_srednia(lista_ocen):
    if len(lista_ocen) == 0:
        return 0
    return sum(lista_ocen) / len(lista_ocen)

def zapisz_raport(dane):
    with open("raport.txt", "w", encoding="utf-8") as plik:
        plik.write("RAPORT OCEN\n")
        plik.write("-------------------------\n")
        
        for uczen in dane:
            linia = f"{uczen['imie']} {uczen['nazwisko']} - srednia: {uczen['srednia']:.2f}\n"
            plik.write(linia)

def main():
    dane = wczytaj_dane("oceny.txt")
    if dane is None:
        return    
    
    for uczen in dane:
        srednia = oblicz_srednia(uczen["oceny"])
        uczen["srednia"] = srednia
        print(f"{uczen['imie']} {uczen['nazwisko']} - srednia: {srednia:.2f}")
    zapisz_raport(dane)
    print("\nRaport zapisano do pliku raport.txt")


#Program
main()