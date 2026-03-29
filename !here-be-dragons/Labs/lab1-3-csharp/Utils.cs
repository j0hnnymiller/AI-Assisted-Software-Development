using System;
using System.Collections.Generic;

namespace BookLibrary
{
    /// <summary>
    /// Helper utilities for the library application
    /// </summary>
    public static class Utils
    {
        public static void PrintHeader(string title)
        {
            Console.WriteLine();
            Console.WriteLine("=".PadRight(50, '='));
            Console.WriteLine(title);
            Console.WriteLine("=".PadRight(50, '='));
            Console.WriteLine();
        }

        public static void PrintBooks(List<Book> books)
        {
            if (books.Count == 0)
            {
                Console.WriteLine("No books found.");
                return;
            }

            Console.WriteLine($"Found {books.Count} book(s):");
            Console.WriteLine();
            foreach (var book in books)
            {
                Console.WriteLine($"  • {book}");
            }
            Console.WriteLine();
        }

        public static string GetUserInput(string prompt)
        {
            Console.Write($"{prompt}: ");
            return Console.ReadLine();
        }

        public static int GetYearInput(string prompt)
        {
            while (true)
            {
                Console.Write($"{prompt}: ");
                if (int.TryParse(Console.ReadLine(), out int year))
                {
                    return year;
                }
                Console.WriteLine("Invalid year. Please enter a valid number.");
            }
        }
    }
}
