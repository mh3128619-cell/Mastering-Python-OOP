class Employee:
  def __init__(self,name,salary,title):
    self.name=name
    self.salary=salary
    self.title=title

Employee_one=Employee("Mohamed","15000","MlOps ENG")
Employee_two=Employee("Ayman","2000","ML ENG")
Employee_three=Employee("Khaled","2200","Doctor")

print(f"My name is {Employee_one.name} and I am {Employee_one.title} and my salary is {Employee_one.salary}")
print(f"My name is {Employee_two.name} and I am {Employee_two.title} and my salary is {Employee_two.salary}")
print(f"My name is {Employee_three.name} and I am {Employee_three.title} and my salary is {Employee_three.salary}")
