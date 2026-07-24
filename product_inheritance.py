class Product:  # Base Class
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def get_info(self):
        return f"Name: {self.name}, Price: {self.price}, Weight: {self.weight}"

    def calculate_shipping(self):
        return self.weight * 10


class Electronics(Product):  # Derived Class
    def __init__(self, name, price, weight, warranty_years):
        super().__init__(name, price, weight)
        self.warranty_years = warranty_years

    def calculate_shipping(self):
        return super().calculate_shipping() + 50

    def get_info(self):
        return (
            f"Name: {self.name}, Price: {self.price}, "
            f"Weight: {self.weight}, Warranty: {self.warranty_years} years"
        )


class Clothing(Product):  # Derived Class
    def __init__(self, name, price, weight, size):
        super().__init__(name, price, weight)
        self.size = size

    def get_info(self):
        return (
            f"Name: {self.name}, Price: {self.price}, "
            f"Weight: {self.weight}, Size: {self.size}"
        )


product1 = Product("Laptop", 100, 10)
electronics1 = Electronics("Gaming Laptop", 200, 20, 2)
clothing1 = Clothing("Shirt", 300, 30, "M")

print(product1.get_info())
print(f"Shipping Cost: {product1.calculate_shipping()}")

print()

print(electronics1.get_info())
print(f"Shipping Cost: {electronics1.calculate_shipping()}")

print()

print(clothing1.get_info())
print(f"Shipping Cost: {clothing1.calculate_shipping()}")
