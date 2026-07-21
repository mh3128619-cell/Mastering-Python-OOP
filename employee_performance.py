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

    def evaluate_performance(self, performance_score):
        if performance_score >= 8:
            self.salary += 5000
            print(f"Congratulations {self.name}! Your performance score is {performance_score}. You got a raise, and your new salary is {self.salary}")
        else:
            print(f"Sorry {self.name}, your performance score is {performance_score}. You did not get a raise this month.")

emp1 = Employee("Mohamed", 15000, "MLOps ENG")

emp1.evaluate_performance(6)
emp1.evaluate_performance(9)
