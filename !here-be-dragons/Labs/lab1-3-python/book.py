class Book:
    """Represents a book in the library system"""

    def __init__(self, title, author, isbn, publication_year):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_year = publication_year
        self.is_available = True

    def __str__(self):
        availability = "Available" if self.is_available else "Checked Out"
        return f'"{self.title}" by {self.author} ({self.publication_year}) - ISBN: {self.isbn} - {availability}'

    def __repr__(self):
        return f'Book("{self.title}", "{self.author}", "{self.isbn}", {self.publication_year})'
