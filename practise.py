

class Book:
    def __init__(self, title, author, year):
        self.title=title
        self.author=author
        self.year=year
    def introduce(self):
        print(f"title: {self.title} | author: {self.author} | year: {self.year}")
    
class BookManager:
    def __init__(self):
        self.books=[]

    def add_books(self, book):
        self.books.append(book)
        print("added succesfully")
    
    def show_book(self):
        print("\n---ALL BOOKS---")
        if not self.books:
            print("no book yet")
            return
        for book in self.books:
            book.introduce()
    
    def search_book(self, title):
        print(f"searching: {title}")
        found = False

        for book in self.books:
            if title.lower() in book.title.lower():
                book.introduce()
                found = True

        if not found:
            print("book not found")

        return found
    
    def delete_book(self, title):
        print(f"deleting: {title}")
        for book in self.books:
            if title.lower() in book.title.lower():
                self.books.remove(book)
                print("deleted succesfully")
                return
        print("book not found")
    
    def update_books(self, title):
        for book in self.books:
            if book.title == title:
               new_title = input("new title: ")
               new_author = input("new author: ")

               try:
                  new_year = int(input("new year: "))
               except ValueError:
                   print("Invalid year, keeping old value")
                   new_year = book.year

               book.title = new_title
               book.author = new_author
               book.year = new_year

               print("Updated successfully")
               return

        print("Book not found")
    
    def total_books(self):
        count=len(self.books)
        print(f"Total books: {count}")

    def clear_books(self):
        self.books.clear()
        print("All books deleted")
