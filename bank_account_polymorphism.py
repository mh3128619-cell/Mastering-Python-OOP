class Account:
    def annual_interest(self):
        raise NotImplementedError("Subclasses must implement annual_interest()")


class SavingsAccount(Account):
    def __init__(self, balance):
        self.balance = balance

    def annual_interest(self):
        return self.balance * 0.05


class CurrentAccount(Account):
    def __init__(self, balance):
        self.balance = balance

    def annual_interest(self):
        return 0


class FixedDepositAccount(Account):
    def __init__(self, balance):
        self.balance = balance

    def annual_interest(self):
        return self.balance * 0.12


accounts = [
    SavingsAccount(10000),
    CurrentAccount(7000),
    FixedDepositAccount(10000)
]

for account in accounts:
    print(f"{account.__class__.__name__} -> Annual Interest: {account.annual_interest()}")
