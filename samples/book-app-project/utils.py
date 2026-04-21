from dataclasses import dataclass
from typing import Optional
from books import Book


def print_menu():
    print("\n📚 Book Collection App")
    print("1. Add a book")
    print("2. List books")
    print("3. Mark book as read")
    print("4. Remove a book")
    print("5. Exit")


def get_user_choice() -> str:
    """Prompt the user to pick a menu option (1-5). Returns a valid choice string."""
    choice = input("Choose an option (1-5): ").strip()
    if not choice:
        print("Please enter a number between 1 and 5.")
        return ""
    if not choice.isdigit() or choice not in ("1", "2", "3", "4", "5"):
        print(f'"{choice}" is not a valid option. Please enter a number between 1 and 5.')
        return ""
    return choice


def get_book_details():
    """Interactively prompt the user for book details via the terminal.

    Prompts for title, author, and publication year in sequence.
    Validates each field before proceeding to the next:
    - Title and author must be non-empty strings.
    - Year must be a non-empty, numeric value.

    Returns:
        tuple[str, str, int]: A (title, author, year) tuple if all inputs are valid.
        None: If any field fails validation. An error message is printed to stdout
              describing which field was invalid and why.

    Example:
        details = get_book_details()
        if details is None:
            return  # user gave invalid input
        title, author, year = details
    """
    title = input("Enter book title: ").strip()
    if not title:
        print("Error: Title cannot be empty.")
        return None

    author = input("Enter author: ").strip()
    if not author:
        print("Error: Author cannot be empty.")
        return None

    year_input = input("Enter publication year: ").strip()
    if not year_input:
        print("Error: Year cannot be empty.")
        return None

    try:
        year = int(year_input)
    except ValueError:
        print(f'Error: "{year_input}" is not a valid year. Please enter a number.')
        return None

    return title, author, year


def print_books(books):
    if not books:
        print("No books in your collection.")
        return

    print("\nYour Books:")
    for index, book in enumerate(books, start=1):
        status = "✅ Read" if book.read else "📖 Unread"
        print(f"{index}. {book.title} by {book.author} ({book.year}) - {status}")


@dataclass
class CollectionStats:
    total: int
    read: int
    unread: int
    oldest: Optional[Book]
    newest: Optional[Book]


def get_collection_stats(books: list[Book]) -> CollectionStats:
    """Return statistics for a list of books."""
    if not books:
        return CollectionStats(total=0, read=0, unread=0, oldest=None, newest=None)

    read_books = [b for b in books if b.read]
    books_with_year = [b for b in books if b.year > 0]

    return CollectionStats(
        total=len(books),
        read=len(read_books),
        unread=len(books) - len(read_books),
        oldest=min(books_with_year, key=lambda b: b.year) if books_with_year else None,
        newest=max(books_with_year, key=lambda b: b.year) if books_with_year else None,
    )
