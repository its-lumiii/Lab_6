class BookPages:
    def __init__(self, pages):
        self.pages = pages

    def __str__(self):
        return f"{self.pages} pages"

    def __add__(self, other):
        total_pages = self.pages + other.pages
        return BookPages(total_pages)

book1 = BookPages(120)
book2 = BookPages(85)

print(book1)

combined = book1 + book2
print(combined)