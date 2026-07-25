class Customer:
  def Final_Price(self,price):
    raise NotImplementedError("This method should be overridden by subclasses.")

class RegularCustomer(Customer):
  def Final_Price(self, price):
    return price

class VIPCustomer(Customer):
  def Final_Price(self, price):
    return price * 0.9

class PremiumCustomer(Customer):
  def Final_Price(self, price):
    return price * 0.8

class Employee(Customer):
  def Final_Price(self, price):
    return price * 0.7

class StudentCustomer(Customer):
  def Final_Price(self, price):
    return price * 0.85

list1 = [RegularCustomer(), VIPCustomer(), PremiumCustomer(),Employee(),StudentCustomer()]

for customer in list1:
  print(customer.Final_Price(1000))
