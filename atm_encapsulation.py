class ATM:
    def __init__(self, owner, pin, balance):
        self.owner = owner          # Public
        self.__pin = pin            # Private
        self.__balance = balance    # Private

    def withdraw(self, pin, amount):
        if pin != self.__pin:
            print("Incorrect PIN")

        elif amount <= 0:
            print("Invalid Amount")

        elif amount > self.__balance:
            print("Insufficient Balance")

        else:
            self.__balance -= amount
            print("Withdrawal Successful")

    def get_balance(self):
        return self.__balance


# Testing
atm = ATM("Ahmed", 1234, 1000)

print(f"Initial Balance: {atm.get_balance()}")

atm.withdraw(1111, 100)
atm.withdraw(1234, 2000)
atm.withdraw(1234, -100)
atm.withdraw(1234, 300)

print(f"Final Balance: {atm.get_balance()}")
