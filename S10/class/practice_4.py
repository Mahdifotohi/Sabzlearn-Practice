class Book:
    def __init__(self, titel, author, year):
        self.titel = titel
        self.author = author
        self.year = year

    def book_info(self):
        return f"BookTitel: {self.titel}, AuthorTitel: {self.author}, year: {self.year}."
    


book = Book("To Kill a Mockingbird", "Harper Lee", "1960")
print(book.book_info())