class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def introduce(self):
        print(f"Title: {self.title} | Author: {self.author} | Year: {self.year}")

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "year": self.year
        }