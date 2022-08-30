class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print("Balance: $" + str(self.balance))
        return self
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance *= (self.int_rate +1)
        return self

    @classmethod
    def account_info(cls, user):
        print(cls.display_account_info(user))

user_1 = BankAccount(0.01, 1000)
user_1.deposit(1100).deposit(2150).deposit(2500).withdraw(1800).yield_interest().display_account_info()

user_2 = BankAccount(0.02, 10000)
user_2.deposit(5000).deposit(7500).withdraw(3500).withdraw(1567).withdraw(809).withdraw(259).yield_interest().display_account_info()

BankAccount.account_info(user_1)
BankAccount.account_info(user_2)



