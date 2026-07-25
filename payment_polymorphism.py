class Payment:
  def pay(self,amount):
    self.amount=amount
    raise NotImplemented

class Creditcard(Payment):
  def pay(self, amount):
    print(f"Paying {amount} using credit card")

class Paypal(Payment):
  def pay(self, amount):
    print(f"Paying {amount} using Paypal")
    
class Cash(Payment):
  def pay(self, amount):
    print(f"Paying {amount} using cash")

list1 = [Creditcard(), Paypal(), Cash()]

for payment in list1:
  payment.pay(100)
