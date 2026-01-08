class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book_name):
        self.books.append(book_name)
        print(f"Book '{book_name}' added successfully.")

    def show_books(self):
        if not self.books:
            print("No books available.")
        else:
            print("Available Books:")
            for book in self.books:
                print("-", book)


# Sample usage
lib = Library()
lib.add_book("Python Programming")
lib.add_book("Data Structures")
lib.show_books()
