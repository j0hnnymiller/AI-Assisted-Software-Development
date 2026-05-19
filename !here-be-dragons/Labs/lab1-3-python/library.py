
class Library:
    """Manages a collection of books in the library"""

    def __init__(self, name):
        self.name = name
        self._books = []

    def add_book(self, book):
        """Add a book to the library"""
        self._books.append(book)
        print(f"Added: {book.title}")

    def remove_book(self, isbn):
        """Remove a book from the library by ISBN"""
        book = self._find_book_by_isbn(isbn)
        if book:
            self._books.remove(book)
            print(f"Removed: {book.title}")
        else:
            print(f"Book with ISBN {isbn} not found.")

    def search_books(self, search_term):
        """Search for books by title or author"""
        results = []
        for book in self._books:
            if search_term in book.title or search_term in book.author:
                results.append(book)
        return results

    def get_all_books(self):
        """Get a copy of all books in the library"""
        return self._books.copy()

    def check_out_book(self, isbn):
        """Check out a book by ISBN"""
        book = self._find_book_by_isbn(isbn)
        if book:
            if book.is_available:
                book.is_available = False
                print(f"Checked out: {book.title}")
            else:
                print(f"{book.title} is already checked out.")
        else:
            print(f"Book with ISBN {isbn} not found.")

    def return_book(self, isbn):
        """Return a book by ISBN"""
        book = self._find_book_by_isbn(isbn)
        if book:
            book.is_available = True
            print(f"Returned: {book.title}")
        else:
            print(f"Book with ISBN {isbn} not found.")

    def get_total_book_count(self):
        """Get the total number of books in the library"""
        return len(self._books)

    def get_available_book_count(self):
        """Get the number of available books"""
        return sum(1 for book in self._books if book.is_available)

    def _find_book_by_isbn(self, isbn):
        """Private helper method to find a book by ISBN"""
        for book in self._books:
            if book.isbn == isbn:
                return book
        return None
