class Book:
    def __init__(self, title, author, ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.available = True

    def borrow(self):
        if self.available:
            self.available = False
            print(f"You have borrowed {self.title}")
        else:
            print(f"{self.title} is not available")

    def return_book(self):
        if not self.available:
            self.available = True
            print(f"{self.title} has been returned")
        else:
            print(f"{self.title} was not borrowed.")


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, library, book_title):
        for book in library.books:
            if book.title == book_title:
                if book.available:
                    book.borrow()
                    self.borrowed_books.append(book)
                    return
                else:
                    print(f"{book_title} is currently not available.")
                    return
        print(f"{book_title} not found in the library.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
        else:
            print("You don't have this book.")

    def view_borrowed_books(self):
        if not self.borrowed_books:
            print(f"{self.name} has not borrowed any books.")
        else:
            print(f"{self.name} has borrowed:")
            for book in self.borrowed_books:
                print(f"{book.title} by {book.author}")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)



library = Library()

book1 = Book("Python Basics", "Gui", "12345")
book2 = Book("Data Structures", "Nik", "67890")

library.add_book(book1)
library.add_book(book2)

member = Member("Ish", 101)

member.borrow_book(library, "Python Basics")
member.view_borrowed_books()

member.borrow_book(library, "Python Basics") 
member.borrow_book(library, "Unknown Book") 

member.return_book(book1)
member.view_borrowed_books()