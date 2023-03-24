from loguru import logger
from library import library
from student import Student
def create_library():
    books = {
        'Gone with the wind' : 'Free',
        'Python programming for everyone' : 'Free',
        'Clean code' : 'Free',
        'Software design pattern' : 'Free'
    }
    libr = library(books)
    Stu = Student('NgTT', libr)

    while True:
        logger.info('''---LIBRARY FUNCTIONS MENU---
            1. Display available books
            2. Borrow a book
            3. Return a book
            4. View borrowed books
            0. Exit program
        ''')

        key = int(input('Enter your choice: '))
        if key == 1:  
            libr.show_avail_books()
        elif key == 2:
            Stu.request_books()
        elif key == 3:
            Stu.return_books()
        elif key == 4:
            Stu.view_borrowed_books()
        elif key == 0:
            logger.info('You have existing ...')
        else:
            logger.info('Invalid choice ! Please try again !')
