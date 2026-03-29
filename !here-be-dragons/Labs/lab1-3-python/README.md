# Book Library Practice Codebase (Python)

This is a practice codebase for GitHub Copilot Training Labs 1-3.

## Purpose

This codebase provides a realistic environment to practice:

- Adding context with @ symbols (@workspace, @file, @terminal)
- Using Ask, Edit, and Agent modes
- Writing effective prompts
- Understanding context management

## Project Structure

```
lab1-3-python/
├── README.md           # This file
├── book.py            # Book model class
├── library.py         # Library management class
├── utils.py           # Helper utilities
└── main.py            # Main entry point
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

- "Explain the Book class in @book.py"
- "What does the search_books method do in @library.py?"
- "Review the main function in @main.py"

**Practice specific prompts:**

- Vague: "Make it better"
- Specific: "Add error handling to the add_book method in @library.py for None book parameters"

### Lab 3: Exploring Copilot Modes

**Ask Mode (no code changes):**

- "What design patterns are used in @library.py?"
- "How could I improve the Book class?"
- "Explain the difference between lists and tuples in Python"

**Edit Mode (inline changes):**

- Select the search_books method
- Ask: "Add case-insensitive search"
- Review and accept/reject the changes

**Agent Mode (file operations):**

- "Create a new file book_report.py that generates statistics about the library"
- "Add docstrings to all public methods"
- "Create unit tests for the Library class using pytest"

## Running the Application

```bash
# Run directly
python main.py

# Or use Copilot to help:
# "How do I run this Python application?"
```

## Installing Dependencies (if needed)

```bash
python -m pip install --upgrade pip
# No external dependencies required for basic version
```

## Suggested Exercises

1. Ask Copilot to explain the purpose of each file
2. Use @file to reference specific files in your questions
3. Practice switching between Ask, Edit, and Agent modes
4. Try different models and compare the results
5. Monitor your token usage when using premium models

## Common Prompts to Try

- "Explain how the Library class manages books using @library.py"
- "Add a feature to search books by publication year"
- "Create a method to get the top 5 most recently added books"
- "What potential bugs or issues do you see in this code?"
- "How would you refactor this code to use list comprehensions?"

## Tips for Success

- Always review AI-generated code before accepting
- Provide specific context using @ references
- Start new chats when switching to different topics
- Test any changes Copilot makes
- Use Ask mode to explore ideas without consuming premium tokens

## Python-Specific Practice

- Ask about type hints and how to add them
- Explore Python-specific idioms and best practices
- Practice with list comprehensions and generators
- Learn about Python's data classes vs regular classes
