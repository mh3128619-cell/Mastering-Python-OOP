class Bank_Account:
  def __init__(self, balance):
    self.balance = balance

  @property
  def balance(self):
    return self._balance

  @balance.setter
  def balance(self, value):
    if value < 0:
      raise ValueError("Balance cannot be negative")
    self._balance = value

try:
  print("Attempting to create account with -50...")
  mohamed = Bank_Account(-50)
except ValueError as e:
  print(f"Error: {e}")

try:
  print("\nCreating account with 100...")
  mohamed = Bank_Account(100)
  print(f"Current balance: {mohamed.balance}")
  
  print("Attempting to set balance to -200...")
  mohamed.balance = -200
except ValueError as e:
  print(f"Error: {e}")
  print(f"Balance remains: {mohamed.balance}")
