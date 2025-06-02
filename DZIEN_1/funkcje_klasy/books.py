class Book:
    def __init__(self, title, author, year,  price):
        self.booktitle = title
        self.author = author
        self.year = year
        self.cena = price
        self.createbook()

    def __repr__(self):
        return f"ksiażka -> {self.booktitle} , {self.author} ({self.year})"

    def createbook(self):
        print(f"{self.booktitle} by {self.author} ({self.year})")

    def cena_po_rabacie(self,rabat):
        return self.cena - (self.cena * rabat/100)

