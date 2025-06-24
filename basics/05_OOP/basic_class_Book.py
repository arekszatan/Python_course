
class Book:
    def __init__(self, author, title = "unknown", isbn = "unknow", year = "unknown"):
        self.author = author
        self.title = title
        self.isbn = isbn
        self.year = year

    def print_data(self):
        print(self.author, self.title, self.isbn, self.year)

book1 = Book("Ola Kowalska", "Podróże", "213243", "2020")
book1.print_data()

book2 = Book("Arek Szatan")
book2.print_data()
