def statystyki(lista):
    min_wartosc = lista[0]
    max_wartosc = lista[0]
    suma = 0

    for liczba in lista:
        if liczba < min_wartosc:
            min_wartosc = liczba
        if liczba > max_wartosc:
            max_wartosc = liczba
        suma += liczba

    srednia = suma / len(lista)
    return (min_wartosc, max_wartosc, srednia)


# def statystyki(lista):
#     return (min(lista), max(lista), sum(lista) / len(lista))


print(statystyki([1,2,3,4,5,5,6,7,8,11]))