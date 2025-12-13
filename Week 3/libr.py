class Library:
    def __init__(self):
        self.books = []   # list to store book titles

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        print("Books in library:")
        for book in self.books:
            print("-", book)

# test
lib = Library()
lib.add_book("Python Basics")
lib.add_book("Data Structures")
lib.add_book("AI Introduction")

lib.show_books()
