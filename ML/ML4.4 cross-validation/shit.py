class Bank:
    accounts = 0

    def __init__(self, owner_name, initial_balance=0):
        self.owner_name = owner_name
        self.balance = initial_balance
        Bank.accounts += 1

    def change_balance(self, amount):
        self.balance += amount

    def account_info(self):
        return f"Owner: {self.owner_name}, Balance: ${self.balance}"

    @classmethod
    def accounts_info(cls):
        return f"Total number of accounts: {cls.accounts}"

    def __str__(self):
        return f"Owner: {self.owner_name}, Balance: ${self.balance}"

user1 = Bank("Mary", 1000)
print(user1)
user1.change_balance(1800)
print(user1)

user2 = Bank("Max", 1500)
print(user2)
print(Bank.accounts_info())
