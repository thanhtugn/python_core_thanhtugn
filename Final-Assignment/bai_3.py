class Book:
    def __init__(self, id, title, author, publisher, publication_date, price):
        self.id = id
        self.title = title
        self.author = author
        self.publisher = publisher
        self.publication_date = publication_date
        self.price = price

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def update_book(self, old_book, new_book):
        index = self.books.index(old_book)
        self.books[index] = new_book

    def search_book(self, keyword):
        results = []
        for book in self.books:
            if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower():
                results.append(book)
        return results

    def sort_books(self, key):
        self.books.sort(key=lambda x: getattr(x, key))

    def display_books(self):
        for book in self.books:
            print(f"ID: {book.id}, Title: {book.title}, Author: {book.author}, Publisher: {book.publisher}, Publication Date: {book.publication_date}, Price: {book.price}")

# Tạo thư viện
library = Library()

while True:
    print("\n==============================")
    print("Library Management System Menu")
    print("==============================")
    print("1. Display all books")
    print("2. Add new book")
    print("3. Update book information")
    print("4. Remove book")
    print("5. Search book by keyword")
    print("6. Sort books")
    print("0. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "0":
        break

    elif choice == "1":
        if not library.books:
            print("There are no books in the library.")
        else:
            print("\nList of books:")
            library.display_books()

    elif choice == "2":
        id = input("Enter book ID: ")
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        publisher = input("Enter book publisher: ")
        publication_date = input("Enter publication date (YYYY): ")
        price = float(input("Enter book price: "))
        book = Book(id, title, author, publisher, publication_date, price)
        library.add_book(book)
        print("Book has been added to the library.")

    elif choice == "3":
        id = input("Enter the ID of the book you want to update: ")
        book = next((book for book in library.books if book.id == id), None)
        if not book:
            print("Book not found in the library.")
        else:
            title = input(f"Enter new title for {book.title}: ")
            author = input(f"Enter new author for {book.author}: ")
            publisher = input(f"Enter new publisher for {book.publisher}: ")
            publication_date = input(f"Enter new publication date (YYYY) for {book.publication_date}: ")
            price = float(input(f"Enter new price for {book.price}: "))
            new_book = Book(id, title, author, publisher, publication_date, price)
            library.update_book(book, new_book)
            print("Book information has been updated.")

    elif choice == "4":
        id = input("Enter the ID of the book you want to remove: ")
        book = next((book for book in library.books if book.id == id), None)
        if not book:
            print("Book not found in the library.")
        else:
            library.remove_book(book)
            print("Book has been removed from the library.")

    elif choice == "5":
        keyword = input("Enter keyword to search: ")
        results = library.search_book(keyword)
        if not results:
            print("No books found matching the keyword.")
        else:
            print(f"\nSearch results for '{keyword}':")
            for book in results:
                print(f"ID: {book.id}, Title: {book.title}, Author: {book.author}, Publisher: {book.publisher}, Publication Date: {book.publication_date}, Price: {book.price}")

    elif choice == "6":
        key = input("Enter key to sort by (id/title/author/publisher/publication_date/price): ")
        library.sort_books(key)
        print("Books have been sorted.")

    else:
        print("Invalid choice. Please try again.")
