class Book:
  total_books = 0

  def __init__(self, title, author):
    self.title = title
    self.author = author
    Book.total_books += 1

  def get_book_information(self):
    print(f"Title: {self.title}, Author: {self.author}")

  @classmethod
  def get_total_books(cls):
    print(f"Total books: {cls.total_books}")

  @staticmethod
  def is_valid_isbn(isbn):
    return len(str(isbn)) == 13 and str(isbn).isdigit()

  @classmethod
  def from_string(cls, book_str):
    title, author = book_str.split(",")
    return cls(title.strip(), author.strip())

book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("To Kill a Mockingbird", "Harper Lee")

book1.get_book_information()
book2.get_book_information()
Book.get_total_books()

print(f"Is ISBN valid? {Book.is_valid_isbn('1234567890123')}")

book3 = Book.from_string("Python Programming, Guido van Rossum")
book3.get_book_information()
Book.get_total_books()
