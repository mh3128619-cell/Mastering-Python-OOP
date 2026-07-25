class Animal:
  def make_sound(self):
    raise NotImplementedError("Subclasses must implement this method")

class Dog(Animal):
  def make_sound(self):
    print("Woof!")

class Cat(Animal):
  def make_sound(self):
    print("Meow!")
  
class cow(Animal):
  def make_sound(self):
    print("Moo!")

list1 = [Dog(), Cat(), cow()]

for animal in list1:
  animal.make_sound()
