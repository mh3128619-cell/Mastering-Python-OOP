class BankAccount:
    def __init__(self, owner, balance):      
        self.owner = owner  # public
        self.__balance = balance  # private
    
    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
            print(f"Added {amount} to the balance")
        else:
            print("Deposit amount must be positive")
    
    def withdraw(self,amount):
        if amount>0 and amount<=self.__balance:
            self.__balance-=amount
            print(f"Withdrew {amount} from the balance")
        else:
            print("Insufficient funds or invalid withdrawal amount")
    
    def get_balance(self):
        return self.__balance   


acc=BankAccount("Mohamed", 1000)
acc.deposit(500)
acc.withdraw(300)
print(f"Final balance: {acc.get_balance()}")
