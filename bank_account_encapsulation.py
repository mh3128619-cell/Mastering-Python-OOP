class BankAccount:
    def __init__(self, owner , balance=0):
        self.owner = owner #Public attribute
        self.__balance = balance  #Private attribute
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Added {amount} to the balance")
        else:
            print("Deposit amount must be positive")
     
    def transfer(self, amount, recipient_account):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            recipient_account.deposit(amount)
            print(f"Transferred {amount} to {recipient_account.owner}")
        else:
            print("Transfer amount must be positive and less than or equal to the balance")
    
    def get_balance(self):
        return self.__balance
    

BankAccount1 = BankAccount("Mohamed", 1000)
acc1 = BankAccount("Ahmed", 1000)
acc2 = BankAccount("Ahmed", 500)

BankAccount1.deposit(500)
BankAccount1.transfer(300, acc1)
BankAccount1.transfer(200, acc2)
