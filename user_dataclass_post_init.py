from dataclasses import dataclass, field

@dataclass(order=True)
class User:
    user_name: str
    email: str
    is_active: bool

    def __post_init__(self):
        # Fix: Remove spaces from the user_name string
        self.user_name = self.user_name.replace(" ", "")

User1 = User("Mohamed", "mohamed@123.com", True)
User2 = User(" Ah med ", "ahmed@123.com", True)

print(User1)
print(User2)
