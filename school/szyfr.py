tekst = "ZZ zz ZZ"
przesuniecie = 3
wynik = ""

for znak in tekst:
    if znak == " ":
        wynik += " "
    elif znak.isupper():
        w = (ord(znak) - ord('A') + przesuniecie) % 26 + ord('A')
        wynik += chr(w)
    elif znak.islower():
        w = (ord(znak) - ord('a') + przesuniecie) % 26 + ord('a')
        wynik += chr(w)
    else:
        wynik += znak

print(wynik)