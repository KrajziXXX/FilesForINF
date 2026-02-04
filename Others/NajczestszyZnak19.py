def najczestszy_znak(tekst):
    max_znak = ""
    max_licznik = 0

    for znak in tekst:
        licznik = tekst.count(znak)
        if licznik > max_licznik:
            max_licznik = licznik
            max_znak = znak

    return max_znak

print(najczestszy_znak("aaaabbc"))