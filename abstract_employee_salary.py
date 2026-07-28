from abc import ABCMeta, abstractmethod

class Employee(metaclass=ABCMeta):
  def __init__(self,name,base_salary):
    self.name=name #public
    self.salary=base_salary #public

  @abstractmethod
  def calculate_salary(self):
    pass

class FullTimeEmployee(Employee):
  def calculate_salary(self):
    return self.salary +100

class ContractorEmployee(Employee):
  def calculate_salary(self):
     return self.salary 

FullTimeEmployee1=FullTimeEmployee("Mohamed",1000)
ContractorEmployee1=ContractorEmployee("Ahmed",500)
print(FullTimeEmployee1.calculate_salary())
print(ContractorEmployee1.calculate_salary())
