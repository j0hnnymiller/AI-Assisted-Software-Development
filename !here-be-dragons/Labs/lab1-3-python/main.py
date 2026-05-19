import utils
from book import Book
from library import Library


def main():
    utils.print_header("Welcome to the Book Library System")

    # Create a library
    library = Library("City Public Library")
    print(f"Library: {library.name}")

    # Add some sample books
    library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald", "978-0743273565", 1925))
    library.add_book(Book("To Kill a Mockingbird", "Harper Lee", "978-0060935467", 1960))
    library.add_book(Book("1984", "George Orwell", "978-0451524935", 1949))
    library.add_book(Book("Pride and Prejudice", "Jane Austen", "978-0141439518", 1813))
    library.add_book(Book("The Catcher in the Rye", "J.D. Salinger", "978-0316769174", 1951))

    # Display library statistics
    print()
    print(f"Total books: {library.get_total_book_count()}")
    print(f"Available books: {library.get_available_book_count()}")

    # List all books
    utils.print_header("All Books in Library")
    all_books = library.get_all_books()
    utils.print_books(all_books)

    # Search for books
    utils.print_header("Search Results for 'the'")
    search_results = library.search_books("the")
    utils.print_books(search_results)

    # Check out a book
    utils.print_header("Checking Out a Book")
    library.check_out_book("978-0451524935")

    # Try to check out the same book again
    print()
    library.check_out_book("978-0451524935")

    # Display updated statistics
    print()
    print(f"Available books: {library.get_available_book_count()}")

    # Return the book
    utils.print_header("Returning a Book")
    library.return_book("978-0451524935")

    # Display final statistics
    print()
    print(f"Available books: {library.get_available_book_count()}")

    print()
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()
