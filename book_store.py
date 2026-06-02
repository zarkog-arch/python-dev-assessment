class Book:
    
    CURRENT_YEAR = 2026

    def __init__(self, title, author, isbn, publication_year):
       
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_year = publication_year

    def get_age(self):
        
        return self.CURRENT_YEAR - self.publication_year

    def get_summary(self):
        
        return f"Title: [{self.title}], Author: [{self.author}], Published: [{self.publication_year}]"

# --- Example Usage ---

book1 = Book(
    title="Harry Potter and the Philosopher's Stone",
    author="J.K. Rowling",
    isbn="978-0747532699",
    publication_year=1997
)


book2 = Book(
    title="The Alchemist",
    author="Paulo Coelho",
    isbn="978-0061122415",
    publication_year=1988
)


book3 = Book(
    title="A Man Called Ove",
    author="Fredrik Backman",
    isbn="978-1476738017",
    publication_year=2012
)

books = [book1, book2, book3]

print("--- Book Details ---")
for book in books:
    print(f"Title: {book.title}")
    print(f"Author: {book.author}")
    print(f"Age: {book.get_age()} years")
    print(f"Summary: {book.get_summary()}")
    print("-" * 20)