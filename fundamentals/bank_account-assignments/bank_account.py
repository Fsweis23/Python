class BankAccount:
    def __init__(self, int_rate, balance):
        self.interest = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self

    def withdraw(self, amount):
        # if the balance after being decreased by the amount after to be greater tahn 0
        if self.balance - amount < 0:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
            return self
        self.balance -= amount
        return self

    def display_account_info(self):
        print(self.balance, self.interest)
        return self

    def yield_interest(self):
        self.balance = self.balance + (self.balance * self.interest)
        return self

# user= BankAccount(.01, 300)
# user.display_account_info()
# user.deposit(50)
# user.display_account_info()

user1 = BankAccount(.01, 300)
user1.display_account_info
user2 = BankAccount(.02, 500)
user2.display_account_info

user1.display_account_info().deposit(50).deposit(100).deposit(50).withdraw(200).yield_interest().display_account_info()

user2.display_account_info().deposit(100).deposit(200).withdraw(200).withdraw(100).withdraw(300).withdraw(50).yield_interest().display_account_info()