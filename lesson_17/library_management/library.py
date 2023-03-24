from loguru import logger

class library:
    def __init__(self, books):
        self.books = books

    def show_avail_books(self):
        avail_books = ('\n --List of available books as following--')
        for book, borrower in self.books.items():
            if borrower == 'Free':
                # logger.info(book)
                avail_books += book + '\n' 
        logger.info(avail_books)     

    def lend_books(self, requested_books, borrower):
        if self.books[requested_books] == 'Free':
            logger.info(f'The books {requested_books} is borrowed by {borrower}')
            self.books[requested_books] = borrower
            return True
        else:
            logger.info(f'The books {requested_books} is not available')
            return False

    def return_books(self, returned_books):
        logger.info(f'The book {returned_books} is returned')
        self.books = [returned_books] = 'Free'            