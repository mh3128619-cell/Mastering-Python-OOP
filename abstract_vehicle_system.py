from abc import ABCMeta, abstractmethod

class Vechile(metaclass=ABCMeta):

  def __init__(self,brand,max_speed):
    self.brand=brand
    self.max_speed=max_speed
  
  @abstractmethod
  def start_engine(self):
    pass 
  
  @abstractmethod
  def get_vechile_type(self):
    pass

class Car(Vechile):

  def start_engine(self):
    return "Car engine started"
  
  def get_vechile_type(self):
    return "Car"

class Bike(Vechile):

  def start_engine(self):
     return "Bike engine started"
  
  def get_vechile_type(self):
    return "Bike"

car1=Car("Toyota",200)
bike1=Bike("Honda",150)
print(car1.start_engine())
print(car1.get_vechile_type())
print(bike1.start_engine())
print(bike1.get_vechile_type())
