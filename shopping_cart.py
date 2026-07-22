class shopping_cart:
  def __init__(self, customer_name):
    self.items = {} 
    self.customer_name = customer_name

  def add_item(self, product, price, quantity):
    if product in self.items:
      self.items[product]['quantity'] += int(quantity)
    else:
      self.items[product] = {'price': float(price), 'quantity': int(quantity)}

  def remove_item(self, product, quantity):
    if product in self.items:
      if self.items[product]['quantity'] >= quantity:
        self.items[product]['quantity'] -= quantity
        if self.items[product]['quantity'] == 0:
          del self.items[product]
      else:
        print(f"We don't have enough {product} in the cart")
    else:
      print(f"{product} is not in the cart")

  def check_out(self):
    total_price = 0
    for item_info in self.items.values():
      total_price += item_info['price'] * item_info['quantity']
    return total_price

Mohamed_shopping_cart = shopping_cart("Mohamed")
Mohamed_shopping_cart.add_item("shoes", 500, 1)
Mohamed_shopping_cart.add_item("shirt", 200, 3)
Mohamed_shopping_cart.remove_item("shirt", 2)
total = Mohamed_shopping_cart.check_out()
print(f"Total for {Mohamed_shopping_cart.customer_name}: {total}")
