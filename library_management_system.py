class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}')"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        if not self.books:
            print("No books available in the library.")
            return
        for book in self.books:
            print(f"Title: {book.title}, Author: {book.author}")


class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book, library):
        if book in library.books:
            self.borrowed_books.append(book)
            library.books.remove(book)
            print(f"{self.name} borrowed '{book.title}'")
        else:
            print(f"'{book.title}' is not available in the library.")

    def return_book(self, book, library):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            library.books.append(book)
            print(f"{self.name} returned '{book.title}'")
        else:
            print(f"{self.name} did not borrow '{book.title}'.")


class Menu:
    def __init__(self, library):
        self.library = library
        self.members = {}

    def get_member(self, name):
        if name not in self.members:
            self.members[name] = Member(name)
        return self.members[name]

    def display_menu(self):
        print("Library Menu:")
        print("1. List all books")
        print("2. Add a book")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            if choice == '1':
                self.library.list_books()
            elif choice == '2':
                title = input("Enter book title: ")
                author = input("Enter book author: ")
                book = Book(title, author)
                self.library.add_book(book)
                print(f"Added '{title}' by {author} to the library.")
            elif choice == '3':
                title = input("Enter the title of the book to borrow: ")
                book = next((b for b in self.library.books if b.title == title), None)
                if book:
                    member_name = input("Enter your name: ")
                    member = self.get_member(member_name)
                    member.borrow_book(book, self.library)
                else:
                    print(f"'{title}' is not available in the library.")
            elif choice == '4':
                title = input("Enter the title of the book to return: ")
                member_name = input("Enter your name: ")
                member = self.get_member(member_name)
                book = next((b for b in member.borrowed_books if b.title == title), None)
                if book:
                    member.return_book(book, self.library)
                else:
                    print(f"{member_name} did not borrow '{title}'.")
            elif choice == '5':
                print("Exiting the library menu.")
                break
            else:
                print("Invalid choice. Please try again.")


book = Book("1984", "George Orwell")
library = Library()
library.add_book(book)
menu = Menu(library)
menu.run()
