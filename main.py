from manager.book_manager import BookManager
from models.book import Book
from utils.input_utils import get_valid_year, get_non_empty_input
import os


def main():
    manager = BookManager()
    manager.load_from_file()

    while True:
        print("\n📚 BOOK MANAGER")
        print("------------------")
        print("1 - Add book")
        print("2 - Show books")
        print("3 - Search book")
        print("4 - Delete book")
        print("5 - Update book")
        print("6 - Count by author")
        print("7 - Exit")
        print("8 - Sort books by year")
        print("0 - Clear screen")

        choice = input("Choose: ")

        if choice == "1":
            title = get_non_empty_input("Title: ")
            author = get_non_empty_input("Author: ")
            year = get_valid_year()

            book = Book(title, author, year)
            manager.add_book(book)
            manager.save_to_file()

        elif choice == "2":
            manager.show_books()

        elif choice == "3":
            title = get_non_empty_input("Title: ")
            manager.search_book(title)

        elif choice == "4":
            title = get_non_empty_input("Title: ")
            manager.delete_book(title)
            manager.save_to_file()

        elif choice == "5":
            title = get_non_empty_input("Title: ")
            manager.update_book(title)
            manager.save_to_file()

        elif choice == "6":
            author = get_non_empty_input("Author: ")
            manager.count_by_author(author)

        elif choice == "7":
            print("Goodbye 👋")
            break

        elif choice == "8":
            manager.sort_books_by_year()
            manager.show_books()

        elif choice == "0":
            os.system("cls")  # Windows

        else:
            print("Invalid choice, try again!")


if __name__ == "__main__":
    main()