class Product:
  def __init__(self,price,discount):
    self.price=price
    self.discount=discount
  
  @property
  def final_price(self):
    return self.price*(1-self.discount)

Product1=Product(100,0.2)
print(Product1.final_price)
