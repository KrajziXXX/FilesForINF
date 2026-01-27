
class BankAccount:
    def __init__(self, acc_number):
        self._balance = 0
        self._acc_number = acc_number

    @classmethod
    def create_with_balance(cls, acc_number, initial_balance):
        acc = cls(acc_number)
        acc.balance = initial_balance
        return acc

    @property
    def acc_number(self):
        return self._acc_number

    @acc_number.setter
    def acc_number(self, value):
        print("Nie możesz zmienić numeru konta")

    @acc_number.deleter
    def acc_number(self):
        print("Nie możesz usunąć atrybutu acc_number")

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            print("Nie możesz wypłacić więcej niż posiadasz")
            return
        self._balance = value  # ✅ Fixed: update private attribute

    @balance.deleter
    def balance(self):
        print("Nie możesz usunąć atrybutu balance")

    @staticmethod
    def convert(amount):
        return round(amount / 4.20,2)
    
    @staticmethod
    def transfer(sender,recipient,amount):
        if sender.balance >= amount:
            sender.balance -= amount
            recipient.balance += amount
            print("Przelew udany")
        else:
            print("Przelew nie udany")

# Test
my_account = BankAccount(28456812874812)
print(my_account.balance)          # 0
print(my_account.acc_number)       # 28456812874812

my_account_with_balance = BankAccount.create_with_balance(823597823, 14)
print(my_account_with_balance.balance)  # 14
print(BankAccount.convert(5))