class product:
  def __init__(self, name, price, stock):
    self.name = name
    self.price = price
    self.quantity = stock

  def apply_discount(self, discount):
    self.price = self.price - (self.price * discount)

  def buy(self, quantity):
    if self.quantity >= quantity:
      self.quantity -= quantity
      print(f"You bought {quantity} {self.name}")
    else:
      print(f"We don't have enough {self.name} in stock")

product1 = product("Laptop", 1000, 5)
product1.apply_discount(0.1)
product1.buy(2)
product1.buy(10)
