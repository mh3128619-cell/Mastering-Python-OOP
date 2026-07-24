class employee:
  def __init__(self, name, salary):
    self.name = name
    self.salary = salary
  
  def calculate_total_pay(self):
    return self.salary

class manager(employee):
  def __init__(self, name, salary, department):
    super().__init__(name, salary)
    self.department = department
  
  def calculate_total_pay(self):
    base_pay = super().calculate_total_pay()
    return base_pay + 5000

class director(manager):
  def __init__(self, name, salary, department, stock_option):
    super().__init__(name, salary, department)
    self.stock_option = stock_option
  
  def calculate_total_pay(self):
    base_pay = super().calculate_total_pay() + self.stock_option
    return base_pay


employee1 = employee("Ahmed", 1000)
manager1 = manager("Mohamed", 1000, "IT")
director1 = director("Ali", 1000, "IT", 5000)

print(f"Employee Name: {employee1.name}, Salary: {employee1.calculate_total_pay()}")
print(f"Manager Name: {manager1.name}, Salary: {manager1.calculate_total_pay()}")
print(f"Director Name: {director1.name}, Salary: {director1.calculate_total_pay()}")
