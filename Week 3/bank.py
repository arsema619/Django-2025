class BankAccount:
    def __init__(self):
        self.__balance = 0   # private attribute

    def deposit(self, amount):
        self.__balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Withdrawal denied! Insufficient balance.")
        else:
            self.__balance -= amount
            print("Withdrawn:", amount)

    def get_balance(self):
        return self.__balance

# test
account = BankAccount()
account.deposit(500)
account.withdraw(700)   # invalid withdrawal
account.withdraw(200)

print("Final Balance:", account.get_balance())
