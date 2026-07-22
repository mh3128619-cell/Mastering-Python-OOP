class Product:
    store_discount = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def get_final_price(self):
        final_price = self.price - (self.price * Product.store_discount)
        return final_price

product1 = Product("phone", 1000)
product2 = Product("laptop", 2000)

print("--- Before General Discount ---")
print(product1.get_final_price())
print(product2.get_final_price())

Product.store_discount = 0.15 

print("--- After applying 15% Store Discount ---")
print(f"Product: {product1.name}, Final Price: {product1.get_final_price()}")
print(f"Product: {product2.name}, Final Price: {product2.get_final_price()}")
