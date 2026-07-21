class Employee:
    def __init__(self, name, salary, title):
        self.name = name
        self.salary = salary
        self.title = title

    def get_full_info(self):
        print(f"My name is {self.name} and I am {self.title} and my salary is {self.salary}")

    def give_raise(self, amount):
        self.salary += amount
        print(f"New salary for {self.name} is {self.salary}")

emp1 = Employee("Mohamed", 15000, "MLOps ENG")

emp1.get_full_info()
emp1.give_raise(2000)
