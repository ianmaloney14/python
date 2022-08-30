class BankAccount:
    all_accounts = []
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

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
        print("Your balance: $" + str(self.balance))
        return self
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance *= (self.int_rate +1)
        return self

    @classmethod
    def account_info(cls):
        for i in cls.all_accounts:
            i.display_account_info()
    

user_1 = BankAccount(0.01, 1000)
user_1.deposit(1100).deposit(2150).deposit(2500).withdraw(1800).yield_interest().display_account_info()

user_2 = BankAccount(0.02, 10000)
user_2.deposit(5000).deposit(7500).withdraw(3500).withdraw(1567).withdraw(809).withdraw(259).yield_interest().display_account_info()

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.account = BankAccount(int_rate=0.01, balance=0)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        print("You deposited: $" + str(amount))

    def make_withdrawl(self, amount):
        self.account.withdraw(amount)
        print("You withdrew: $" + str(amount))

    def display_user_balance(self):
        print("Your balance: $" + str(self.account.balance))

    def transfer_money(self, amount, other_user):
        self.other_user = other_user
        self.account.balance -= amount
        self.other_user.account.balance += amount
        print(f"You sent {other_user.username}: " + str(amount))

user_1 = User("johndoe123", "johndoe123@gmail.com")
user_2 = User("janedoe321", "janedoe321@gmail.com")

user_1.make_deposit(5000)
user_1.make_withdrawl(2500)
user_1.display_user_balance()
user_1.transfer_money(1000, user_2)
user_1.display_user_balance()

# BankAccount.account_info()