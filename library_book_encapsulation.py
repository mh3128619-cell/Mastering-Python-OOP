class Book:
  def __init__(self, title, author, available):
    self.title = title  #Public
    self.author = author  #Public
    self.__available = available  #Private

  def borrow(self):
    if self.__available:
      self.__available = False
      print(f"{self.title} has been borrowed.")
    else:
      print(f"{self.title} is not available for borrowing.")

  def return_book(self):
    self.__available = True
    print(f"{self.title} has been returned.")

  def is_available(self):
    return self.__available

book=Book("Python","Elzero", True)
book.borrow()
book.return_book()
print(book.is_available())
