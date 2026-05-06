import json
from models.book import Book

filename = "books.json"

class BookManager:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Added successfuly")
    
    def show_books(self):
        print("\n---ALL BOOKS---")
        if not self.books:
            print("no books yet")
            return
        for book in self.books:
            book.introduce()
    
    def search_book(self, title):
        print(f"searching: {title}")
        for book in self.books:
         if title.lower() in book.title.lower():
            book.introduce()
            return
    print("not found")

    def delete_book(self, title):
        print(f"delete: {title}")
        for book in self.books:
         if title.lower() in book.title.lower():
            self.books.remove(book)
            print("deleted successfully")
            return
    print("not found")

    def update_book(self, title):
        for book in self.books:
           if title.lower() in book.title.lower():
              print("Leave empty if you don't want to change")

              new_title = input(f"New title ({book.title}): ")
              new_author = input(f"New author ({book.author}): ")

              try:
                 new_year_input = input(f"New year ({book.year}): ")
                 new_year = int(new_year_input) if new_year_input else book.year
              except ValueError:
                print("Invalid year, keeping old value")
                new_year = book.year

              if new_title:
                book.title = new_title
              if new_author:
                book.author = new_author

              book.year = new_year

              print("Updated successfully")
              return

    print("Book not found")

    def count_by_author(self, author):
        count = 0
        for book in self.books:
            if author.lower() in book.author.lower():
               count += 1

        if count > 0:
          print(f"📚 {count} books found for '{author}'")
        else:
          print("No books found")
    
    def save_to_file(self):
       data=[]
       for book in self.books:
           data.append(book.to_dict())
       with open(filename, "w") as file:
          json.dump(data, file)
    
    def load_from_file(self):
       try:
          with open(filename, "r") as file:
             data = json.load(file)
             self.books = []
             for item in data:
                 book = Book(item["title"], item["author"], item["year"])
                 self.books.append(book)
       except FileNotFoundError:
           print("no file yet")
       except json.JSONDecodeError:
           print("failed to load books")
    
    def sort_books_by_year(self):
        self.books.sort(key=lambda book: book.year)
        print("Books sorted by year")