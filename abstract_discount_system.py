from abc import ABCMeta, abstractmethod

class Discount(metaclass=ABCMeta):
  def __init__(self, price, name):
    self.price = price
    self.name = name

  def get_base_price(self):
    return self.price
  
  @abstractmethod
  def apply_discount(self):
    pass
  
  @abstractmethod
  def get_discount_name(self):
    pass

class VIPDiscount(Discount):
  def __init__(self, price, name):
    super().__init__(price, name)

  def apply_discount(self):
    return self.price * 0.7
  
  def get_discount_name(self):
    return self.name

class FlashSaleDiscount(Discount):
  def __init__(self, price, name):
    super().__init__(price, name)

  def apply_discount(self):
    return self.price * 0.5
  
  def get_discount_name(self):
    return self.name

VIPDiscount1 = VIPDiscount(800, "Ahmed")
FlashSaleDiscount1 = FlashSaleDiscount(1000, "Ayman")

print(f"Base Price: {VIPDiscount1.get_base_price()}")
print(f"VIP Discount: {VIPDiscount1.apply_discount()}")
print(f"Discount Name: {VIPDiscount1.get_discount_name()}")
print(f"Flash Sale Discount: {FlashSaleDiscount1.apply_discount()}")
print(f"Discount Name: {FlashSaleDiscount1.get_discount_name()}")
