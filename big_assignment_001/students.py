from mysql.connector import MySQLConnection, Error

class students:

    conn = None

    def __init__(self):
        self.connect()

    def __del__(self):
        if self.conn!= None:
            self.conn.close()

    def connect(self):
        db_config = {
            'host': 'localhost',
            'database': 'student_management',
            'user': 'root',
            'password': ''
        }

        conn = None

        try:
            conn = MySQLConnection(**db_config)
            if conn.is_connected() == False:
                raise Error
        except Error as e:
            print(e)

        self.conn = conn

    def show(self):
        
        show_db = 'SELECT * FROM student_management.students;'
        result = self.conn._execute_query(show_db)
        for row_number, row_data in enumerate(result):
            print (row_data)
            
        self.conn.close()
        

        

        
        
    

