class BankAccount:
    def __init__(self, int_rate, balance, name):
        self.interest = int_rate
        self.balance = balance
        self.name = name

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print(self.balance, self.interest)
        return self

    def yield_interest(self):
        self.balance = self.balance + (self.balance * self.interest)
        return self


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.checking_account = BankAccount(int_rate=0.02, balance=0, name="checking")
        self.saving_account = BankAccount(int_rate=0.02, balance=0, name="saving")

    def make_deposit(self, amount, account):
        account.balance = amount + account.balance
        print(f"{account.balance} {account.name}")
        return self

    def make_withdraw(self, amount, account):
        amount = account - amount
        print(account)
        return self

    def display_user_balance(self, account):
        print(account)
        return self

    def transfer_money(self, amount, other_user_account, account):
        if amount <= account.balance:
            print(account.balance - amount)
            print(other_user_account.balance + amount)
        else:
            print("Not enough funds")
        return self

user = User("Firas", "firas@gmail.com")
user2 = User("Joe", "joe@gmail.com")
user.make_deposit(100, user.checking_account)
user.transfer_money(50, user2.saving_account, user.checking_account)