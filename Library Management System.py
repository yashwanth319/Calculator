class BookNotAvailableException(Exception):
    """Custom exception for book unavailability."""
    pass

class Book:
    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' by {book.author} added to the library.")

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.available:
                    book.available = False
                    print(f"Book '{title}' has been borrowed.")
                    return
                else:
                    raise BookNotAvailableException(f"Book '{title}' is not available in the library.")
        print(f"Book '{title}' not found in the library.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                book.available = True
                print(f"Book '{title}' has been returned.")
                return
        print(f"Book '{title}' not found in the library.")

    def display_books(self):
        available_books = [book.title for book in self.books if book.available]
        if available_books:
            print("Available books:")
            for title in available_books:
                print(f"- {title}")
        else:
            print("No books available in the library.")

# Example usage
library = Library()
library.add_book(Book("Python Programming", "John Doe"))
library.add_book(Book("Data Science Handbook", "Jane Smith"))

try:
    library.borrow_book("Python Programming")  # Borrow an available book
    library.borrow_book("Python Programming")  # Attempt to borrow the same book again
except BookNotAvailableException as e:
    print(f"Error: {e}")

library.display_books()  # Display available books after borrowing
