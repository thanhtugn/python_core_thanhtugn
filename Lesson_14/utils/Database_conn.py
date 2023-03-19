import mysql.connector
from loguru import logger

class SQLConnector:
    pass

    def create_connection(self):
        my_conn = mysql.connector.connect   (host='localhost',
                                            user = 'root',
                                            passwd = 'B4ngb0ng@',
                                            database = 'student_management')
        logger.info("Connected to MySQL DB")
        return my_conn

        cur = my_conn.cursor()
        cur.execute("show databases")
        for row in cur:
            print(row)

        my_conn.close()

# conn = SQLConnector()
# conn.create_connection()
