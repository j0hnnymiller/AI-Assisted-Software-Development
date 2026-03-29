# Book Library Practice Codebase (TypeScript)

This is a practice codebase for GitHub Copilot Training Labs 1-3.

## Purpose

This codebase provides a realistic environment to practice:

- Adding context with @ symbols (@workspace, @file, @terminal)
- Using Ask, Edit, and Agent modes
- Writing effective prompts
- Understanding context management

## Project Structure

```
lab1-3-typescript/
├── README.md           # This file
├── package.json        # Node.js dependencies
├── tsconfig.json       # TypeScript configuration
├── src/
│   ├── book.ts        # Book model class
│   ├── library.ts     # Library management class
│   ├── utils.ts       # Helper utilities
│   └── main.ts        # Main entry point
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

- "Explain the Book class in @src/book.ts"
- "What does the searchBooks method do in @src/library.ts?"
- "Review the main function in @src/main.ts"

**Practice specific prompts:**

- Vague: "Make it better"
- Specific: "Add error handling to the addBook method in @src/library.ts for null book parameters"

### Lab 3: Exploring Copilot Modes

**Ask Mode (no code changes):**

- "What design patterns are used in @src/library.ts?"
- "How could I improve the Book class?"
- "Explain the difference between interfaces and classes in TypeScript"

**Edit Mode (inline changes):**

- Select the searchBooks method
- Ask: "Add case-insensitive search"
- Review and accept/reject the changes

**Agent Mode (file operations):**

- "Create a new file src/bookReport.ts that generates statistics about the library"
- "Add JSDoc comments to all public methods"
- "Create unit tests for the Library class using Jest"

## Setup and Running

```bash
# Install dependencies
npm install

# Build TypeScript
npm run build

# Run the application
npm start

# Or use Copilot to help:
# "How do I run this TypeScript application?"
```

## Development

```bash
# Watch mode for development
npm run dev

# Type checking
npm run type-check
```

## Suggested Exercises

1. Ask Copilot to explain the purpose of each file
2. Use @file to reference specific files in your questions
3. Practice switching between Ask, Edit, and Agent modes
4. Try different models and compare the results
5. Monitor your token usage when using premium models

## Common Prompts to Try

- "Explain how the Library class manages books using @src/library.ts"
- "Add a feature to search books by publication year"
- "Create a method to get the top 5 most recently added books"
- "What potential bugs or issues do you see in this code?"
- "How would you refactor this code to use modern TypeScript features?"

## Tips for Success

- Always review AI-generated code before accepting
- Provide specific context using @ references
- Start new chats when switching to different topics
- Test any changes Copilot makes
- Use Ask mode to explore ideas without consuming premium tokens

## TypeScript-Specific Practice

- Ask about type safety and interfaces
- Explore TypeScript-specific features (generics, union types, etc.)
- Practice with async/await patterns
- Learn about TypeScript configuration options
