class ToDoList:

    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def __str__(self):
        return f"Tasks: {self.tasks}"

    def __len__(self):
        return len(self.tasks)

    def __add__(self, other):
        if isinstance(other, ToDoList):
            new_list = ToDoList()
            new_list.tasks = self.tasks + other.tasks
            return new_list
        return NotImplemented


list1 = ToDoList()
list1.add_task("Study Python")
list1.add_task("Exercise")

list2 = ToDoList()
list2.add_task("Read a book")
list2.add_task("Go to the gym")

combined_list = list1 + list2

print(list1)
print(list2)
print(combined_list)
print(f"Total tasks: {len(combined_list)}")
