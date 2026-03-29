def print_header(title):
    """Print a formatted header"""
    print()
    print("=" * 50)
    print(title)
    print("=" * 50)
    print()

def print_books(books):
    """Print a list of books"""
    if not books:
        print("No books found.")
        return

    print(f"Found {len(books)} book(s):")
    print()
    for book in books:
        print(f"  • {book}")
    print()

def get_user_input(prompt):
    """Get string input from user"""
    return input(f"{prompt}: ")

def get_year_input(prompt):
    """Get year input from user with validation"""
    while True:
        try:
            year = int(input(f"{prompt}: "))
            return year
        except ValueError:
            print("Invalid year. Please enter a valid number.")
