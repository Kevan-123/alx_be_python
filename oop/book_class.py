class Book:
    """A simple Book class using Python magic methods."""

    def __init__(self, title, author, year):
        """Initialize a Book instance with title, author, and year."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor that prints when a Book instance is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """Human-readable string representation."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official representation that recreates the Book instance."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
