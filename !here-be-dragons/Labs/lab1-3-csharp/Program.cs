using System;

namespace BookLibrary
{
    class Program
    {
        static void Main(string[] args)
        {
            Utils.PrintHeader("Welcome to the Book Library System");

            // Create a library
            var library = new Library("City Public Library");
            Console.WriteLine($"Library: {library.Name}");

            // Add some sample books
            library.AddBook(new Book("The Great Gatsby", "F. Scott Fitzgerald", "978-0743273565", 1925));
            library.AddBook(new Book("To Kill a Mockingbird", "Harper Lee", "978-0060935467", 1960));
            library.AddBook(new Book("1984", "George Orwell", "978-0451524935", 1949));
            library.AddBook(new Book("Pride and Prejudice", "Jane Austen", "978-0141439518", 1813));
            library.AddBook(new Book("The Catcher in the Rye", "J.D. Salinger", "978-0316769174", 1951));

            // Display library statistics
            Console.WriteLine();
            Console.WriteLine($"Total books: {library.GetTotalBookCount()}");
            Console.WriteLine($"Available books: {library.GetAvailableBookCount()}");

            // List all books
            Utils.PrintHeader("All Books in Library");
            var allBooks = library.GetAllBooks();
            Utils.PrintBooks(allBooks);

            // Search for books
            Utils.PrintHeader("Search Results for 'the'");
            var searchResults = library.SearchBooks("the");
            Utils.PrintBooks(searchResults);

            // Check out a book
            Utils.PrintHeader("Checking Out a Book");
            library.CheckOutBook("978-0451524935");

            // Try to check out the same book again
            Console.WriteLine();
            library.CheckOutBook("978-0451524935");

            // Display updated statistics
            Console.WriteLine();
            Console.WriteLine($"Available books: {library.GetAvailableBookCount()}");

            // Return the book
            Utils.PrintHeader("Returning a Book");
            library.ReturnBook("978-0451524935");

            // Display final statistics
            Console.WriteLine();
            Console.WriteLine($"Available books: {library.GetAvailableBookCount()}");

            Console.WriteLine();
            Console.WriteLine("Press any key to exit...");
            Console.ReadKey();
        }
    }
}
