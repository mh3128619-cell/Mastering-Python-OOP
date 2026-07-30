from dataclasses import dataclass, field

@dataclass(order=True)
class Product():
    sort_index: float = field(init=False, repr=False)
    
    name: str
    price: float
    quantity: int
    total_value: float = field(init=False)
    
    def __post_init__(self):
        self.total_value = self.price * self.quantity
        self.sort_index = self.total_value

product1 = Product("Phone", 1000, 2)
product2 = Product("Laptop", 24300.39, 1)

print(product1 < product2)
print(product1.total_value)
print(product2.total_value)
print(product1)
