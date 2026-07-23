class to_do_list:

  def __init__(self):
    self.tasks = []

  def add_task(self, task):
    self.tasks.append(task)

  def __str__(self):
    return f"Tasks: {self.tasks}"

  def __len__(self):
    return len(self.tasks)

my_list = to_do_list()

my_list.add_task("Study Python")
my_list.add_task("Exercise")

print(f"Object representation: {str(my_list)}")
print(f"Number of tasks: {len(my_list)}")
print(f"Method reference: {my_list.add_task}")
