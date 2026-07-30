from dataclasses import dataclass, field

@dataclass(order=True, frozen=True)
class Order:
    sort_index: float = field(init=False, repr=False)
    order_id: str
    total_amount: float
    items: list = field(default_factory=list)
    status: str = "pending"

    def __post_init__(self):
        object.__setattr__(self, "sort_index", self.total_amount)

Order1 = Order("ORD001", 150.50)
Order2 = Order("ORD002", 300.75)

print(f"Is Order1 < Order2? {Order1 < Order2}")
print(f"Order1 Total: {Order1.total_amount}")
