class Employee:
  def __init__(self, name, salary):
    self.name = name
    self.salary = salary

class Manager(Employee):
  def __init__(self,name,salary,department):
    super().__init__(name,salary)
    self.department = department

Employee_one=Employee("Ahmed",1000)
Manager_one=Manager("Mohamed",1000,"IT")
print(f"Employee Name: {Employee_one.name}, Salary: {Employee_one.salary}")
print(f"Manager Name: {Manager_one.name}, Salary: {Manager_one.salary}, Department: {Manager_one.department}")
