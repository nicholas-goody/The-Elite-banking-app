class Account:
    def __init__(self,balance):
        self.balance=balance

    def withdraw(self,amount):
        if amount<self.balance:
            self.balance-=amount
            print(f"New balance is {self.balance}")
        else :
            print("Insufficient balance")

    
    def deposit(self,amount):
        self.balance+=amount
        print(f"New balance is {self.balance}")

customer=Account(10000)
print(customer.withdraw(233))
print(customer.deposit(344))
