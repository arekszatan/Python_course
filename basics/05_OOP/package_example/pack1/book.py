
class Book:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return "Book: " + self.title