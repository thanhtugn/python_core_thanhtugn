from loguru import logger

class Student:
    def __init__(self, stu_name, library):
        self.stu_name = stu_name
        self.books = []
        self.library = library

    def view_borrowed_books(self):
        if not self.books:
            logger.info('You have not borrowed any books')
        else:
            for ind, book in enumerate (self.books):
                logger.info(f'{ind+1}.{book}')

    def request_books(self):
        book_name = input('Enter a book name which you want to borrow: ')
        if self.library.len_book(book_name, self.stu_name):
            logger.info(f'You have borrowed the book {book_name}')
            self.books.append(book_name)
        else:
            logger.info(f'You can not borrow the book {book_name}. Try again')

    def return_books(self):
        self.view_borrowed_books()
        return_book_id = int(input('Choose a book in above list to return (1,2,...):'))
        return_book_name = self.books[return_book_id-1]
        self.library.return_book(return_book_name)
        self.books.pop(return_book_id-1)
        logger.info(f'You returned the book {return_book_name}')