books = []

def add_book():
    id = input("Enter book ID: ")
    title = input('Enter title: ')
    author = input('Enter author: ')
    publisher = input('Enter publisher: ')
    year = input('Enter year: ')
    book = {'id':id,'Title': title,'Author' :author,'Publisher' :publisher, 'Year':year}
    books.append(book)
    print("book added successfully.")

def search_book():
    id = input('Enter book ID: ')
    for book in books:
        if book['id'] == id:
            print('Book found: ')
            print('ID', book['id'])
            print('Title', book['Title'])
            print('Author', book['Author'] )
            print('Publisher', book['Publisher'])
            print('Year', book['Year'])
            return
    print("Book not found.")

def update_book():
    id = input("Enter book ID: ")
    for book in books:
        if book['id'] == id:
            print('Book found: ')
            print('id', book['id'])
            print('Title', book['Title'])
            print('Author', book['Author'] )
            print('Publisher', book['Publisher'])
            print('Year', book['Year'])
            print("Book updated successfully.")
            return
    print("Book not found.")

def delete_book():
    id = input("Enter book ID: ")
    for book in books:
        if book['id'] == id:
            books.remove(book)
            print("Book deleted successfully.")
            return
    print("Book not found.")

def show_menu():
    print("1. Add book")
    print("2. Search book")
    print("3. Update book")
    print("4. Delete book")
    print("6. Sort books by author")
    print("0. Exit")
    choice = input("Enter your choice: ")
    return choice

def get_author_name(book):
    return book['Author']

def sort_by_author():
    print("Sort by author")
    books.sort(key=get_author_name)
    print(books)
    
    

while True:
    choice = show_menu()
    if choice == "1":
        add_book()
    elif choice == "2":
        search_book()
    elif choice == "3":
        update_book()
    elif choice == "4":
        delete_book()
    elif choice == "5":
        sort_by_author()
    elif choice == "0":
        break
    else:
        print("Invalid choice. Please try again.")
