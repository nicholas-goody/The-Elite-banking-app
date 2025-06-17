from account import Account


class SavingsAccount(Account):
    def __init__(self, balance):
        Account.__init__(self, balance)

    def withdraw(self, amount):
        if amount <= 10000:
            return super().withdraw(amount)
        else:
            print("Withdrawal limit exceeded. You can only withdraw up to 10,000.")


    def deposit(self, amount):
        if amount <= 50000:
            return super().deposit(amount)
        else:
            print("Deposit limit exceeded. You can only deposit up to 50,000.")           
