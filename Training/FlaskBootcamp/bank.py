class bank:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __repr__(self):
        return F"Hello {self.owner} your balance is:{self.balance}"

    def deposit(self, amount):
        self.balance += amount
        return F"Your new balance is {self.balance}"

    def withdraw(self, withdrawal):
        if withdrawal <= self.balance:
            self.balance -= withdrawal
            return F"After withdrawing {withdrawal},Your new balance is {self.balance}"
        else:
            return F"Not enough funds, your balance is:{self.balance}"


account = bank('Bob', 500)
print(account.deposit(100))
print(account.withdraw(400))
