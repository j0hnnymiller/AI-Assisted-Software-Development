import { Book } from "./book";

/**
 * Print a formatted header
 */
export function printHeader(title: string): void {
  console.log();
  console.log("=".repeat(50));
  console.log(title);
  console.log("=".repeat(50));
  console.log();
}

/**
 * Print a list of books
 */
export function printBooks(books: Book[]): void {
  if (books.length === 0) {
    console.log("No books found.");
    return;
  }

  console.log(`Found ${books.length} book(s):`);
  console.log();
  books.forEach((book) => {
    console.log(`  • ${book.toString()}`);
  });
  console.log();
}

/**
 * Get user input (simplified for demonstration)
 */
export function getUserInput(prompt: string): string {
  // In a real application, you would use readline or a similar library
  // This is simplified for the demonstration
  return "";
}

/**
 * Get year input with validation (simplified for demonstration)
 */
export function getYearInput(prompt: string): number {
  // In a real application, you would use readline or a similar library
  // This is simplified for the demonstration
  return new Date().getFullYear();
}
