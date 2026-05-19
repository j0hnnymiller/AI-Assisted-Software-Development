import { Book } from "./book";
import { Library } from "./library";
import { printHeader, printBooks } from "./utils";

function main(): void {
  printHeader("Welcome to the Book Library System");

  // Create a library
  const library = new Library("City Public Library");
  console.log(`Library: ${library.name}`);

  // Add some sample books
  library.addBook(
    new Book("The Great Gatsby", "F. Scott Fitzgerald", "978-0743273565", 1925)
  );
  library.addBook(
    new Book("To Kill a Mockingbird", "Harper Lee", "978-0060935467", 1960)
  );
  library.addBook(new Book("1984", "George Orwell", "978-0451524935", 1949));
  library.addBook(
    new Book("Pride and Prejudice", "Jane Austen", "978-0141439518", 1813)
  );
  library.addBook(
    new Book("The Catcher in the Rye", "J.D. Salinger", "978-0316769174", 1951)
  );

  // Display library statistics
  console.log();
  console.log(`Total books: ${library.getTotalBookCount()}`);
  console.log(`Available books: ${library.getAvailableBookCount()}`);

  // List all books
  printHeader("All Books in Library");
  const allBooks = library.getAllBooks();
  printBooks(allBooks);

  // Search for books
  printHeader("Search Results for 'the'");
  const searchResults = library.searchBooks("the");
  printBooks(searchResults);

  // Check out a book
  printHeader("Checking Out a Book");
  library.checkOutBook("978-0451524935");

  // Try to check out the same book again
  console.log();
  library.checkOutBook("978-0451524935");

  // Display updated statistics
  console.log();
  console.log(`Available books: ${library.getAvailableBookCount()}`);

  // Return the book
  printHeader("Returning a Book");
  library.returnBook("978-0451524935");

  // Display final statistics
  console.log();
  console.log(`Available books: ${library.getAvailableBookCount()}`);

  console.log();
  console.log("Application completed.");
}

main();
