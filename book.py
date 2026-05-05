import json

filename="books.json"

class Book:
    def __init__(self, title, author, year):
        self.title=title
        self.author=author
        self.year=year
    def introduce(self):
        print(f"Title: {self.title} | Author: {self.author} | Year: {self.year}")
    
    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "year": self.year
        }
    
class BookManager:
    def __init__(self):
        self.books=[]
    
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
            new_title = input("title: ")
            new_author = input("author: ")
            new_year = int(input("year: "))

            book.title = new_title
            book.author = new_author
            book.year = new_year

            print("updated successfully")
            return
    print("book not found")

    def count_by_author(self, author):
        count = 0
        for book in self.books:
            if author.lower() in book.author.lower():
                count += 1

        if count > 0:
          print(f"{count} books found for {author}")
        else:
           print("no book from this author")
    
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

manager = BookManager()
manager.load_from_file()

def main():
    while True:
        print("\n---MENU---")
        print("1 - Add book")
        print("2 - Show books")
        print("3 - Search book")
        print("4 - Delete book")
        print("5 - Update book")
        print("6 - Count by author")
        print("7 - Exit")

        choice = input("Choose: ")

        if choice == "1":
            title = input("title: ")
            author = input("author: ")
            year = int(input("year: "))
            book = Book(title, author, year)
            manager.add_book(book)
            manager.save_to_file()

        elif choice == "2":
            manager.show_books()

        elif choice == "3":
            title = input("title: ")
            manager.search_book(title)

        elif choice == "4":
            title = input("title: ")
            manager.delete_book(title)
            manager.save_to_file()

        elif choice == "5":
            title = input("title: ")
            manager.update_book(title)
            manager.save_to_file()

        elif choice == "6":
            author = input("author: ")
            manager.count_by_author(author)

        elif choice == "7":
            print("Goodbye")
            break

main()