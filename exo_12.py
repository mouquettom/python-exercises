class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

class Library:
    def __init__(self):
        self.books = []
        self.borrowed_books_list = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book_title):
        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)
                print(f"\n'{book_title}' a été supprimé.")
                return
        else:
            print("\nCe livre est introuvable.")

    def borrow_book(self, book_title):
        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)
                self.borrowed_books_list.append(book)
                print(f"\nVous avez emprunté le livre suivant : '{book_title}'.")
                print(f"'{book_title}' n'est plus disponible.")
                return
        print(f"\nLe livre '{book_title}' n'est pas disponible.")

    def return_book(self, book_title):
        for book in self.borrowed_books_list:
            if book.title == book_title:
                self.borrowed_books_list.remove(book)
                self.books.append(book)
                print(f"\nVous avez retourné le livre suivant : '{book_title}'.")
                print(f"'{book_title}' est de nouveau disponible.")
                return
        print(f"\nLe livre '{book_title}' n'a pas été emprunté.")

    def available_books(self):
        print("\n*** Livres disponibles ***")
        for i, book in enumerate(self.books):
            print(f"{i + 1} : {book.title}")

    def borrowed_books(self):
        print("\n*** Livres empruntés ***")
        for i, book in enumerate(self.borrowed_books_list):
            print(f"{i + 1} : {book.title}")

if __name__ == "__main__":
    library = Library()

    # Ajout des livres
    library.add_book(Book("1984", "George Orwell", 1949))
    library.add_book(Book("To Kill a Mockingbird", "Harper Lee", 1960))
    library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald", 1925))
    library.add_book(Book("Harry Potter and the Philosopher Stone", "JK.Rowling", 1997))
    library.add_book(Book("Harry Potter and the Chamber of Secrets", "JK.Rowling", 1998))
    library.add_book(Book("Harry Potter and the Prisoner of Azkaban", "JK.Rowling", 1999))

    library.available_books()

    library.borrow_book("1984")
    library.borrow_book("Harry Potter and the Philosopher Stone")
    library.borrow_book("The Great Gatsby")

    library.available_books()
    library.return_book("Harry Potter and the Chamber of Secrets")
    library.return_book("1984")

    library.available_books()
    library.borrowed_books()

    library.remove_book("1984")

    library.available_books()