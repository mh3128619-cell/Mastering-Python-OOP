class shopping_cart:
  def __init__(self):
    self.items = []
  
  def add_item(self, item):
    self.items.append(item)
  
  def __str__(self):
    items_str = ", ".join(str(item) for item in self.items)
    return f"Shopping Cart: {len(self.items)} items, Items: [{items_str}]"

  def __len__(self):
    return len(self.items)
  
  def __add__(self, other):
    if isinstance(other, shopping_cart):
      new_cart = shopping_cart()
      new_cart.items = self.items + other.items
      return new_cart
    return NotImplemented

cart1 = shopping_cart()
cart1.add_item(100)
cart1.add_item(250)

cart2 = shopping_cart()
cart2.add_item(50)

print(cart1)
print(f"Number of items in cart1: {len(cart1)}")

combined_cart = cart1 + cart2
print(combined_cart)
print(f"Number of items in combined cart: {len(combined_cart)}")
