print("APP STARTED")
from flask import Flask, render_template, request, redirect
from manager.book_manager import BookManager
from models.book import Book

app = Flask(__name__)

manager = BookManager()
manager.load_from_file()


@app.route("/test")
def test():
    return "WORKING"


@app.route("/test")
def test():
    return "OK WORKS"
# 🏠 HOME (FIXED)
@app.route("/")
def home():
    return redirect("/books")


# 📚 SHOW BOOKS
@app.route("/books")
def books():
    return render_template("books.html", books=manager.books)


# ➕ ADD BOOK
@app.route("/add", methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        title = request.form.get("title")
        author = request.form.get("author")
        year = request.form.get("year")

        try:
            year = int(year)
        except:
            return "Invalid year!"

        new_book = Book(title, author, year)
        manager.add_book(new_book)
        manager.save_to_file()

        return redirect("/books")

    return render_template("add.html")


# ❌ DELETE BOOK
@app.route("/delete")
def delete_book():
    title = request.args.get("title")

    for book in manager.books:
        if book.title == title:
            manager.books.remove(book)
            break

    manager.save_to_file()
    return redirect("/books")


# ✏️ UPDATE BOOK
@app.route("/update", methods=["GET", "POST"])
def update_book():
    title = request.args.get("title")

    if request.method == "POST":
        new_title = request.form.get("title")
        new_author = request.form.get("author")
        new_year = request.form.get("year")

        try:
            new_year = int(new_year)
        except:
            return "Invalid year!"

        for book in manager.books:
            if book.title == title:
                if new_title:
                    book.title = new_title
                if new_author:
                    book.author = new_author
                book.year = new_year
                break

        manager.save_to_file()
        return redirect("/books")

    return render_template("update.html", title=title)


# 🔍 SEARCH
@app.route("/search", methods=["GET", "POST"])
def search():
    results = []

    if request.method == "POST":
        query = request.form.get("query").lower()

        for book in manager.books:
            if query in book.title.lower() or query in book.author.lower():
                results.append(book)

    return render_template("search.html", results=results)


# 🚀 RUN (LOCAL ONLY)
if __name__ == "__main__":
    app.run(debug=True)