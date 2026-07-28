from abc import ABCMeta, abstractmethod

class OrderProcessor(metaclass=ABCMeta):
  def __init__(self, amount):
    self.amount = amount

  @abstractmethod
  def validate_order(self):
    pass 
  
  @abstractmethod
  def process_transaction(self):
    pass
  
  def check_out(self):
    if self.validate_order():
      return self.process_transaction()
    else:
      return "Order validation failed"

class WalletOrderProcessor(OrderProcessor):
  def validate_order(self):
    print("Validating Wallet...")
    return True
  
  def process_transaction(self):
    return f"Processed {self.amount} via Wallet"

class CashOnDeliveryProcessor(OrderProcessor):
  def validate_order(self):
    print("Validating Address for COD...")
    return True
  
  def process_transaction(self):
    return f"Order of {self.amount} set for Cash on Delivery"

WalletOrderProcessor1 = WalletOrderProcessor(100)
CashOnDeliveryProcessor1 = CashOnDeliveryProcessor(200)
print(WalletOrderProcessor1.check_out())
print(CashOnDeliveryProcessor1.check_out())
