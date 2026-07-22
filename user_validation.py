class User:
  user_account = 0
  banned_users = ["admin", "root", "superuser"]
  
  def __init__(self, name, email):
    self.name = name
    self.email = email
    
  @classmethod
  def validation(cls, name):
    if name in cls.banned_users:
      raise ValueError("Name not allowed")
    else:
      cls.user_account += 1

User.validation("Ahmed")
print(f"Users count: {User.user_account}")

try:
    User.validation("admin")
except ValueError as e:
    print(f"Error: {e}")
