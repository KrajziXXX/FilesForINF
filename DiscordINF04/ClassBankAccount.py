# Definicja klasy BankAccount
class BankAccount:

    # Konstruktor klasy BankAccount
    def __init__(self, acc_number):
        # Prywatny atrybut przechowujący saldo konta
        self._balance = 0

        # Prywatny atrybut przechowujący numer konta
        self._acc_number = acc_number

    # Metoda klasowa tworząca konto z początkowym saldem
    @classmethod
    def create_with_balance(cls, acc_number, initial_balance):
        # Utworzenie nowego obiektu klasy
        acc = cls(acc_number)

        # Ustawienie początkowego salda
        acc.balance = initial_balance

        # Zwrócenie utworzonego obiektu
        return acc

    # Getter numeru konta
    @property
    def acc_number(self):
        # Zwrócenie numeru konta
        return self._acc_number

    # Setter numeru konta (blokada zmiany)
    @acc_number.setter
    def acc_number(self, value):
        print("Nie możesz zmienić numeru konta")

    # Blokada usuwania numeru konta
    @acc_number.deleter
    def acc_number(self):
        print("Nie możesz usunąć atrybutu acc_number")

    # Getter salda konta
    @property
    def balance(self):
        # Zwrócenie aktualnego salda
        return self._balance

    # Setter salda konta
    @balance.setter
    def balance(self, value):
        # Sprawdzenie czy saldo nie jest ujemne
        if value < 0:
            print("Nie możesz wypłacić więcej niż posiadasz")
            return

        # Ustawienie nowej wartości salda
        self._balance = value

    # Blokada usuwania salda
    @balance.deleter
    def balance(self):
        print("Nie możesz usunąć atrybutu balance")

    # Metoda statyczna przeliczająca walutę
    @staticmethod
    def convert(amount):
        # Przeliczenie kwoty po kursie 4.20
        return round(amount / 4.20, 2)

    # Metoda statyczna wykonująca przelew między kontami
    @staticmethod
    def transfer(sender, recipient, amount):
        # Sprawdzenie czy nadawca ma wystarczające środki
        if sender.balance >= amount:
            sender.balance -= amount
            recipient.balance += amount
            print("Przelew udany")
        else:
            print("Przelew nie udany")


# Test działania programu
my_account = BankAccount(28456812874812)

# Wyświetlenie salda konta
print(my_account.balance)

# Wyświetlenie numeru konta
print(my_account.acc_number)

# Utworzenie konta z początkowym saldem
my_account_with_balance = BankAccount.create_with_balance(823597823, 14)

# Wyświetlenie salda nowego konta
print(my_account_with_balance.balance)

# Wywołanie metody statycznej
print(BankAccount.convert(5))
