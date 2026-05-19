import { Book } from "./book";

/**
 * Manages a collection of books in the library
 */
export class Library {
  private books: Book[];
  public name: string;

  constructor(name: string) {
    this.name = name;
    this.books = [];
  }

  addBook(book: Book): void {
    this.books.push(book);
    console.log(`Added: ${book.title}`);
  }

  removeBook(isbn: string): void {
    const index = this.books.findIndex((b) => b.isbn === isbn);
    if (index !== -1) {
      const book = this.books[index];
      this.books.splice(index, 1);
      console.log(`Removed: ${book.title}`);
    } else {
      console.log(`Book with ISBN ${isbn} not found.`);
    }
  }

  searchBooks(searchTerm: string): Book[] {
    return this.books.filter(
      (book) =>
        book.title.includes(searchTerm) || book.author.includes(searchTerm)
    );
  }

  getAllBooks(): Book[] {
    return [...this.books];
  }

  checkOutBook(isbn: string): void {
    const book = this.books.find((b) => b.isbn === isbn);
    if (book) {
      if (book.isAvailable) {
        book.isAvailable = false;
        console.log(`Checked out: ${book.title}`);
      } else {
        console.log(`${book.title} is already checked out.`);
      }
    } else {
      console.log(`Book with ISBN ${isbn} not found.`);
    }
  }

  returnBook(isbn: string): void {
    const book = this.books.find((b) => b.isbn === isbn);
    if (book) {
      book.isAvailable = true;
      console.log(`Returned: ${book.title}`);
    } else {
      console.log(`Book with ISBN ${isbn} not found.`);
    }
  }

  getTotalBookCount(): number {
    return this.books.length;
  }

  getAvailableBookCount(): number {
    return this.books.filter((book) => book.isAvailable).length;
  }
}
