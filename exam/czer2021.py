class SelectionSort:
    def __init__(self):
        self.tablica = []

    def wczytaj_dane(self):
        print("Podaj 10 liczb całkowitych:")
        for i in range(10):
            liczba = int(input(f"Liczba {i + 1}: "))
            self.tablica.append(liczba)

    def sortuj_malejaco(self):
        n = len(self.tablica)
        for i in range(n):
            index_max = self.__znajdz_max_index(i)
            # zamiana miejscami
            self.tablica[i], self.tablica[index_max] = self.tablica[index_max], self.tablica[i]

    def __znajdz_max_index(self, start):
        max_index = start
        for i in range(start + 1, len(self.tablica)):
            if self.tablica[i] > self.tablica[max_index]:
                max_index = i
        return max_index

    def wyswietl(self):
        print("Posortowana tablica (malejąco):")
        for element in self.tablica:
            print(element)


# --- Program główny ---
sortowanie = SelectionSort()
sortowanie.wczytaj_dane()
sortowanie.sortuj_malejaco()
sortowanie.wyswietl()
