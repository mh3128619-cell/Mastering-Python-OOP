class Bank_Account:
  def __init__(self, owner_name, balance):
    self.owner_name = owner_name
    self.balance = balance

  def deposit(self, amount):
    if amount > 0:
      self.balance += amount
      print(f"Your new balance is {self.balance}")
    else:
      print(f"Invalid amount. Current balance is {self.balance}")

  def withdraw(self, amount):
    if self.balance >= amount:
      self.balance -= amount
      print(f"Your new balance is {self.balance}")
    else:
      print(f"Insufficient funds. Current balance is {self.balance}")

  def get_balance(self):
    print(f"Your name is {self.owner_name} and your balance is {self.balance}")

Bank_Account_one = Bank_Account("Mohamed", 1000)
Bank_Account_one.deposit(500)
Bank_Account_one.withdraw(200)
Bank_Account_one.get_balance()
