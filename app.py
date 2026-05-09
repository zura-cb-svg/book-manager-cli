from flask import Flask, render_template, request, redirect
from manager.book_manager import BookManager
from models.book import Book

app = Flask(__name__)

manager = BookManager()
manager.load_from_file()


@app.route("/")
def home():
    return redirect("/books")


@app.route("/books")
def books():
    return render_template("books.html", books=manager.books)


@app.route("/add", methods=["GET", "POST"])
def add_book():
    error = None

    if request.method == "POST":
        title = request.form.get("title")
        author = request.form.get("author")
        year = request.form.get("year")

        if title.strip() == "" or author.strip() == "":
            error = "Title and Author are required"

        else:
            try:
                year = int(year)
                if year < 0:
                    error = "Year must be positive"
            except:
                error = "Invalid year"

            if not error:
                for book in manager.books:
                    if book.title == title:
                        error = "Book with this title already exists"
                        break

            if not error:
                new_book = Book(title, author, year)
                manager.add_book(new_book)
                manager.save_to_file()
                return redirect("/books")

    return render_template("add.html", error=error)


@app.route("/delete")
def delete_book():
    title = request.args.get("title")

    for book in manager.books:
        if book.title == title:
            manager.books.remove(book)
            break

    manager.save_to_file()
    return redirect("/books")


@app.route("/update", methods=["GET", "POST"])
def update_book():
    title = request.args.get("title")
    error = None

    book_to_edit = None
    for book in manager.books:
        if book.title == title:
            book_to_edit = book
            break

    if request.method == "POST":
        new_title = request.form.get("title")
        new_author = request.form.get("author")
        new_year = request.form.get("year")

        if new_title.strip() == "":
            error = "Title cannot be empty"

        else:
            try:
                new_year = int(new_year)
            except:
                error = "Invalid year"

            if not error:
                for book in manager.books:
                    if book.title == title:
                        book.title = new_title
                        book.author = new_author
                        book.year = new_year
                        break

                manager.save_to_file()
                return redirect("/books")

    return render_template("update.html", book=book_to_edit, error=error)


@app.route("/search", methods=["GET", "POST"])
def search():
    results = []

    if request.method == "POST":
        query = request.form.get("query").lower()

        for book in manager.books:
            if query in book.title.lower() or query in book.author.lower():
                results.append(book)

    return render_template("search.html", results=results)


if __name__ == "__main__":
    app.run(debug=True)