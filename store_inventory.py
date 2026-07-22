class store:
  total_products_count = 0
  inventory = {
      "laptop": 5,
      "phone": 10 
  }

  def __init__(self, name):
    self.name = name
    store.total_products_count += 1

  def sell_product(self, product_name, quantity):
    if product_name in store.inventory:
      if store.inventory[product_name] >= quantity:
        store.inventory[product_name] -= quantity
        print(f"Sold {quantity} {product_name}(s). Remaining: {store.inventory[product_name]}")
      else:
        print("We don't have enough products in stock")
    else:
      print("Product not found in inventory")

      
my_store = store("Tech Store")
my_store.sell_product("laptop", 2)
