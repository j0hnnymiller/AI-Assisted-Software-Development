using System;
using System.Collections.Generic;
using System.Linq;

namespace BookLibrary
{
    /// <summary>
    /// Manages a collection of books in the library
    /// </summary>
    public class Library
    {
        private List<Book> books;
        public string Name { get; set; }

        public Library(string name)
        {
            Name = name;
            books = new List<Book>();
        }

        public void AddBook(Book book)
        {
            books.Add(book);
            Console.WriteLine($"Added: {book.Title}");
        }

        public void RemoveBook(string isbn)
        {
            var book = books.FirstOrDefault(b => b.ISBN == isbn);
            if (book != null)
            {
                books.Remove(book);
                Console.WriteLine($"Removed: {book.Title}");
            }
            else
            {
                Console.WriteLine($"Book with ISBN {isbn} not found.");
            }
        }

        public List<Book> SearchBooks(string searchTerm)
        {
            return books.Where(b =>
                b.Title.Contains(searchTerm) ||
                b.Author.Contains(searchTerm))
                .ToList();
        }

        public List<Book> GetAllBooks()
        {
            return new List<Book>(books);
        }

        public void CheckOutBook(string isbn)
        {
            var book = books.FirstOrDefault(b => b.ISBN == isbn);
            if (book != null)
            {
                if (book.IsAvailable)
                {
                    book.IsAvailable = false;
                    Console.WriteLine($"Checked out: {book.Title}");
                }
                else
                {
                    Console.WriteLine($"{book.Title} is already checked out.");
                }
            }
            else
            {
                Console.WriteLine($"Book with ISBN {isbn} not found.");
            }
        }

        public void ReturnBook(string isbn)
        {
            var book = books.FirstOrDefault(b => b.ISBN == isbn);
            if (book != null)
            {
                book.IsAvailable = true;
                Console.WriteLine($"Returned: {book.Title}");
            }
            else
            {
                Console.WriteLine($"Book with ISBN {isbn} not found.");
            }
        }

        public int GetTotalBookCount()
        {
            return books.Count;
        }

        public int GetAvailableBookCount()
        {
            return books.Count(b => b.IsAvailable);
        }
    }
}
