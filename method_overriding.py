class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_details(self):
        print(f"Employee name: {self.name}, Salary: {self.salary}")


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def get_details(self):
        print(f"Manager name: {self.name}, Salary: {self.salary}, Department: {self.department}")


employee1 = Employee("Ahmed", 1000)
manager1 = Manager("Mohamed", 1000, "IT")

employee1.get_details()
manager1.get_details()
