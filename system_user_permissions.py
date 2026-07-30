from dataclasses import dataclass, field

@dataclass(order=True)
class SystemUser:
  username:str
  email:str
  role:str="user"
  Permissions:list=field(default_factory=list)

  def __post_init__(self):
    if self.role=="User":
      self.Permissions.append("read")

    elif self.role=="Admin":
      self.Permissions.append("read")
      self.Permissions.append("write")
      self.Permissions.append("delete")
  
SystemUser1=SystemUser("Mohamed","mohamed@123.com","User")
SystemUser2=SystemUser("Ahmed","ahmed@123.com","Admin")

print(SystemUser1.Permissions)
print(SystemUser2.Permissions)
