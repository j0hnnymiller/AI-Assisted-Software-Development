# Book Library Practice Codebase (C#)

This is a practice codebase for GitHub Copilot Training Labs 1-3.

## Purpose

This codebase provides a realistic environment to practice:

- Adding context with @ symbols (@workspace, @file, @terminal)
- Using Ask, Edit, and Agent modes
- Writing effective prompts
- Understanding context management

## Project Structure

```
lab1-3-csharp/
├── README.md           # This file
├── Book.cs            # Book model class
├── Library.cs         # Library management class
├── Program.cs         # Main entry point
└── Utils.cs           # Helper utilities
```

## What This Application Does

A simple book library management system that allows you to:

- Add books to the library
- Search for books by title or author
- List all books
- Remove books from the library

## How to Use This Codebase for Labs

### Lab 1: Getting Started

- Open this folder in VS Code
- Familiarize yourself with the file structure
- Use Copilot chat to ask questions about the code

### Lab 2: Understanding Context Management

**Practice @workspace:**

- "Explain what this codebase does" (using @workspace)
- "Find all methods that modify the book collection"
- "Show me where books are stored"

**Practice @file:**

- "Explain the Book class in @Book.cs"
- "What does the SearchBooks method do in @Library.cs?"
- "Review the Main method in @Program.cs"

**Practice specific prompts:**

- Vague: "Make it better"
- Specific: "Add error handling to the AddBook method in @Library.cs for null book parameters"

### Lab 3: Exploring Copilot Modes

**Ask Mode (no code changes):**

- "What design patterns are used in @Library.cs?"
- "How could I improve the Book class?"
- "Explain the difference between List and Array in C#"

**Edit Mode (inline changes):**

- Select the SearchBooks method
- Ask: "Add case-insensitive search"
- Review and accept/reject the changes

**Agent Mode (file operations):**

- "Create a new file BookReport.cs that generates statistics about the library"
- "Add XML documentation comments to all public methods"
- "Create unit tests for the Library class"

## Building and Running

```bash
# Compile
dotnet build

# Run
dotnet run

# Or use Copilot to help:
# "How do I run this C# console application?"
```

## Suggested Exercises

1. Ask Copilot to explain the purpose of each file
2. Use @file to reference specific files in your questions
3. Practice switching between Ask, Edit, and Agent modes
4. Try different models and compare the results
5. Monitor your token usage when using premium models

## Common Prompts to Try

- "Explain how the Library class manages books using @Library.cs"
- "Add a feature to search books by publication year"
- "Create a method to get the top 5 most recently added books"
- "What potential bugs or issues do you see in this code?"
- "How would you refactor this code to use LINQ more effectively?"

## Tips for Success

- Always review AI-generated code before accepting
- Provide specific context using @ references
- Start new chats when switching to different topics
- Test any changes Copilot makes
- Use Ask mode to explore ideas without consuming premium tokens
