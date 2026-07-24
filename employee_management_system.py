class Employee:
  def __init__(self, name, id_number, **kwargs):
    self.name = name
    self.id_number = id_number
  
  def get_info(self):
    return f"Name: {self.name}, ID: {self.id_number}"

class TechStaff(Employee):
  def __init__(self, name, id_number, programming_language, **kwargs):
    super().__init__(name=name, id_number=id_number, **kwargs)
    self.programming_language = programming_language
  
  def write_code(self):
    print(f"{self.name} is writing code in {self.programming_language}")

class AdminStaff(Employee):
  def __init__(self, name, id_number, access_level, **kwargs):
    super().__init__(name=name, id_number=id_number, **kwargs)
    self.access_level = access_level
  
  def manage_system(self):
    print(f"{self.name} is managing the system with access level {self.access_level}")

class TechLead(TechStaff, AdminStaff):
  def __init__(self, name, id_number, programming_language, access_level):
    super().__init__(name=name, id_number=id_number, programming_language=programming_language, access_level=access_level)
  
  def lead_project(self):
    print(f"{self.name} is leading the Technical Team")

employee1 = Employee("Ahmed", 1000)
tech_staff1 = TechStaff("Mohamed", 1001, "Python")
admin_staff1 = AdminStaff("Ali", 1002, "High")
tech_lead1 = TechLead("Sara", 1003, "Python", "High")

print(f"Employee name: {employee1.name}, ID: {employee1.id_number}")
print(f"TechStaff name: {tech_staff1.name}, ID: {tech_staff1.id_number}, Programming Language: {tech_staff1.programming_language}")
print(f"AdminStaff name: {admin_staff1.name}, ID: {admin_staff1.id_number}, Access Level: {admin_staff1.access_level}")
print(f"TechLead name: {tech_lead1.name}, ID: {tech_lead1.id_number}, Programming Language: {tech_lead1.programming_language}, Access Level: {tech_lead1.access_level}")
