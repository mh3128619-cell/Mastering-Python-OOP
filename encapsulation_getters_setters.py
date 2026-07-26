class Employee:
    def __init__(self, name, salary):
        self.name = name #Public attribute
        self.__salary = salary #Private attribute
    
    def get_salary(self):
        return self.__salary #Getter method to access private attribute
    
    def set_salary(self, salary):
        if salary < 0:
            raise ValueError("Salary cannot be negative")
        self.__salary = salary #Setter method to modify private attribute
        print(f"Salary updated to: {self.__salary} successfully.")
    
    def add_bonus(self, bonus):
        if bonus < 0:
            raise ValueError("Bonus cannot be negative")
        self.__salary += bonus #Method to add bonus to salary
        print(f"Bonus of {bonus} added. New salary is: {self.__salary}.")
    
    def display_info(self):
        print(f"Employee Name: {self.name}, Salary: {self.__salary}") #Method to display employee information


# Example usage
emp = Employee("John Doe", 50000)
emp.display_info()  # Display initial information
emp.set_salary(55000)  # Update salary
emp.add_bonus(5000)  # Add bonus to salary
emp.display_info()  # Display updated information
