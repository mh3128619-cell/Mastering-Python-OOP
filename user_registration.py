class user:
  active_users_count = 0
  min_password_len = 8

  def __init__(self, name, password):
    if len(str(password)) < user.min_password_len:
      raise ValueError(f"Password must be at least {user.min_password_len} characters")
    
    self.name = name
    self.password = self.hash_password(password)
    user.active_users_count += 1
    print(f"User {self.name} created successfully.")

  @staticmethod
  def hash_password(password):
    return f"hashed_{password}"

  @classmethod
  def from_json(cls, json_data):
    return cls(json_data["name"], json_data["password"])

try:
    u1 = user("Ahmed", "1234567890123")
    u2 = user.from_json({"name": "Sara", "password": "secret_pass"})
    print(f"Active users: {user.active_users_count}")

    u3 = user("Ayman", 1234)
except ValueError as e:
    print(f"Error: {e}")
