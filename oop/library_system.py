class Book:
    """Base Book class with title and author."""

    def __init__(self, title, author):
        self.title = title
        self.author = author


class EBook(Book):
    """EBook class inheriting from Book."""

    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size  # in KB


class PrintBook(Book):
    """PrintBook class inheriting from Book."""

    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count  # number of pages


class Library:
    """Library class demonstrating composition (has a collection of books)."""

    def __init__(self):
        self.books = []

    def add_book(self, book):
        """Add any type of Book (Book, EBook, PrintBook) to the library."""
        self.books.append(book)

    def list_books(self):
        """Prints details of each book."""
        for book in self.books:
            if isinstance(book, EBook):
                print(f"EBook: {book.title} by {book.author}, File Size: {book.file_size}KB")
            elif isinstance(book, PrintBook):
                print(f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}")
            else:
                print(f"Book: {book.title} by {book.author}")
