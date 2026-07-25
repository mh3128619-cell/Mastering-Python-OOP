class Employee:
  def calculate_salary(self):
    raise NotImplementedError

class Full_Time_Employee(Employee):
  def __init__(self, monthly_salary):
    self.monthly_salary = monthly_salary

  def calculate_salary(self):
    return self.monthly_salary

class Part_Time_Employee(Employee):
  def __init__(self, hourly_rate, hours_worked):
    self.hourly_rate = hourly_rate
    self.hours_worked = hours_worked

  def calculate_salary(self):
    return self.hourly_rate * self.hours_worked

class Freelancer(Employee):
  def __init__(self,name,project_payment,bonus):
    self.name = name
    self.project_payment = project_payment
    self.bonus = bonus

  def calculate_salary(self):
    return self.project_payment + self.bonus


list1=[Full_Time_Employee(5000), Part_Time_Employee(20, 160), Freelancer("Alice", 1000, 200)]

for employee in list1:
  print(employee.calculate_salary())
