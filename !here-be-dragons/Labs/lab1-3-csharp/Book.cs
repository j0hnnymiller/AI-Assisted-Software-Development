namespace BookLibrary
{
    /// <summary>
    /// Represents a book in the library system
    /// </summary>
    public class Book
    {
        public string Title { get; set; }
        public string Author { get; set; }
        public string ISBN { get; set; }
        public int PublicationYear { get; set; }
        public bool IsAvailable { get; set; }

        public Book(string title, string author, string isbn, int publicationYear)
        {
            Title = title;
            Author = author;
            ISBN = isbn;
            PublicationYear = publicationYear;
            IsAvailable = true;
        }

        public override string ToString()
        {
            string availability = IsAvailable ? "Available" : "Checked Out";
            return $"\"{Title}\" by {Author} ({PublicationYear}) - ISBN: {ISBN} - {availability}";
        }
    }
}
