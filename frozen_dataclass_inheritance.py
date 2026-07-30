from dataclasses import dataclass, field

@dataclass(order=True, frozen=True)
class Employee():
    name: str
    salary: float

@dataclass(order=True, frozen=True)
class Manager(Employee):
    department: str

Employee1 = Employee("Mohamed", 1000)
manager1 = Manager("Mohamed", 1000, "IT")

print(manager1)

try:
    Employee1.salary = 2000
except Exception as e:
    print(f"Error: {e}")

print(f"The salary of Employee1 is: {Employee1.salary}")
