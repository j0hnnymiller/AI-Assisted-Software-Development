/**
 * Represents a book in the library system
 */
export class Book {
  public title: string;
  public author: string;
  public isbn: string;
  public publicationYear: number;
  public isAvailable: boolean;

  constructor(
    title: string,
    author: string,
    isbn: string,
    publicationYear: number
  ) {
    this.title = title;
    this.author = author;
    this.isbn = isbn;
    this.publicationYear = publicationYear;
    this.isAvailable = true;
  }

  toString(): string {
    const availability = this.isAvailable ? "Available" : "Checked Out";
    return `"${this.title}" by ${this.author} (${this.publicationYear}) - ISBN: ${this.isbn} - ${availability}`;
  }
}
