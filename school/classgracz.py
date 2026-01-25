class Gracz:
    def __init__(self, login="user", haslo="password", poziom=1):
        self._login = login
        self._haslo = haslo
        self._poziom = poziom

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, value):
        self._login = value

    @property
    def haslo(self):
        return self._haslo

    @haslo.setter
    def haslo(self, value):
        self._haslo = value

    @property
    def poziom(self):
        return self._poziom

    @poziom.setter
    def poziom(self, value):
        self._poziom = value

    def print(self):
        print(f"Login: {self._login}, Hasło: {self._haslo}, Poziom: {self._poziom}")


class Admin(Gracz):
    def __init__(self, login="user", haslo="password", poziom=1):
        super().__init__(login, haslo, poziom)


if __name__ == "__main__":
    g1 = Gracz()
    g1.print()

    print()

    g2 = Gracz("Radosław", "1312", 3)
    g2.print()
