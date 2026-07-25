import math

class Area:
  def calculate_area(self):
    raise NotImplementedError("Subclasses must implement calculate_area")

class Circle(Area):
  def __init__(self, radius):
    self.radius = radius
  def calculate_area(self):
     return math.pi * self.radius ** 2

class Rectangle(Area):
  def __init__(self, width, height):
    self.width = width
    self.height = height
  def calculate_area(self):
    return self.width * self.height

class Triangle(Area):
  def __init__(self, base, height):
    self.base = base
    self.height = height
  def calculate_area(self):
    return 0.5 * self.base * self.height

shapes = [Circle(5), Rectangle(10, 20), Triangle(10, 5)]

for shape in shapes:
  print(f"{type(shape).__name__} area: {shape.calculate_area():.2f}")
