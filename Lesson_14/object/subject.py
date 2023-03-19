# from utils.txt_file_ops import *
from utils.Database_conn import *
from object.base_class import *
from loguru import logger
from tabulate import tabulate
from datetime import datetime


class Subject:
    def __init__(self, sub_id='', sub_name=''):
        self.__sub_id = sub_id
        self.__sub_name = sub_name
        db_obj = SQLConnector()
        self.__db_conn = db_obj.create_connection()
        self.__db_cursor = self.__db_conn.cursor()

    def display_menu(self):
        while True:
            print("--------------------------------")
            print("PLEASE SELECT A FUNCTION")
            print("1. ADD NEW SUBJECT")
            print("2. UPDATE SUBJECT")
            print("3. DELETE SUBJECT")
            print("4. FIND SUBJECT")
            print("5. SHOW ALL SUBJECTS")
            print("0. EXIT")
            key = input("ENTER YOUR CHOICE: ")
            if key == '1':
                self.__add_data()
            elif key == '2':
                self.__update_data()
            elif key == '3':
                self.__delete_data()
            elif key == '4':
                self.__search_data()
            elif key == '5':
                self.__get_data()
            elif key == '0':
                print("EXITING...")
                return
            else:
                print("INVALID CHOICE")
                print("PLEASE TRY AGAIN")

    def __get_data(self):
        sql_cmd = "SELECT * FROM subject"
        self.__db_cursor.execute(sql_cmd)
        result = self.__db_cursor.fetchall()
        sub_list = []
        for row in enumerate(result):

            sub_info = [row[0], row[1]]
            sub_list.append(sub_info)

        print(tabulate(sub_list, headers = ['ID', 'NAME']))

    def __input_sub_info(self):
        self.__sub_name = input("SUBJECT NAME: ")

    def __add_data(self):
        #Input information from keyboard
        print("--INPUT SUBJECT INFORMATION--")
        self.__input_sub_info()

        sql_cmd = """INSERT INTO subject (subject_name) 
                     VALUES (%s)
                  """
        vals = (self.__sub_name,)
        self.__db_cursor.execute(sql_cmd, vals)
        self.__db_conn.commit()
        logger.info("SUBJECT ADDED SUCCESSFULLY")
        

    def __update_data(self):
        print("--UPDATE SUBJECT INFORMATION--")
        print("ENTER SUBJECT ID:")
        sub_ID_input = input("STUDENT ID: ")
        self.__input_sub_info()
        sql_cmd =   "UPDATE subject SET subject_name = %s WHERE subject_id = %s"
        self.__db_cursor.execute(sql_cmd, (self.__sub_name, sub_ID_input))
        if (self.__db_conn.commit()):
            logger.error("UPDATE SUBJECT FAILED!")               
        else:
            logger.info("UPDATE SUBJECT SUCCESSFULLY!") 

    def __delete_data(self):
        print("--FIND SUBJECT INFORMATION--")
        sub_ID_input = input("ENTER SUBJECT ID: ")
        sql_cmd =   "DELETE FROM subject WHERE subject_id = %s"
        self.__db_cursor.execute(sql_cmd, [sub_ID_input])
        if(self.__db_conn.commit()):
            logger.error("DELETE SUBJECT FAILED!")
        else:
            logger.info("DELETE SUBJECT SUCCESSFULLY!")
                

    def __search_data(self):
        print("--FIND SUBJECT INFORMATION--")
        while True:
            print("1. FIND SUBJECT BY ID")
            print("2. FIND SUBJECT BY NAME")
        
            key = input("Enter your choice: ")
            if key == '1':
                self.__search_sub_byID()
            elif key == '2':
                self.__search_sub_byName()
            elif key == '0':
                print ("You have exited the program")
                return
            else:
                print ("Invalid choice")
                print ("Please try again")

    def __search_sub_byID(self):
        while True:
            print("--FIND SUBJECT INFORMATION--")
            sub_ID_input = int(input("ENTER SUBJECT ID: "))
            sql_cmd = "SELECT * FROM students WHERE subject_id = %s"
            self.__db_cursor.execute(sql_cmd, [sub_ID_input])
            results = self.__db_cursor.fetchall()
            for row in results:
                #logger.info(row)
                print("--SUBJECT INFORMATION--")
                print(f"SUBJECT ID: {sub_ID_input}")
                print(f"SUBJECT NAME: {row[1]}")
            print('ID NOT FOUND')

    def __search_sub_byName(self):
        while True:
            print("--FIND SUBJECT INFORMATION--")
            sub_name_input = input("ENTER SUBJECT NAME: ")
            sql_cmd = "SELECT * FROM students WHERE subject_name = %s"
            self.__db_cursor.execute(sql_cmd, [sub_name_input])
            results = self.__db_cursor.fetchall()
            for row in results:
                #logger.info(row)
                print("--SUBJECT INFORMATION--")
                print(f"SUBJECT ID: {row[0]}")
                print(f"SUBJECT NAME: {row[sub_name_input]}")
            print('SUB NOT FOUND')

