from utils.txt_file_ops import *
from utils.Database_conn import *
from object.base_class import *
from loguru import logger
from tabulate import tabulate
from datetime import datetime

class Student:
    def __init__(self, stu_id='', stu_name='', stu_birthdate='', stu_sex='', stu_address='', stu_phone='', stu_email=''):
        self.__stu_id = stu_id
        self.__stu_name = stu_name
        self.__stu_birthdate = stu_birthdate
        self.__stu_sex = stu_sex
        self.__stu_address = stu_address
        self.__stu_phone = stu_phone
        self.__stu_email = stu_email
        db_obj = SQLConnector()
        self.__db_conn = db_obj.create_connection()
        self.__db_cursor = self.__db_conn.cursor()

    def display_menu(self):
        while True:
            print("--------------------------------")
            print("PLEASE SELECT A FUNCTION")
            print("1. ADD NEW STUDENT")
            print("2. UPDATE STUDENT")
            print("3. DELETE STUDENT")
            print("4. FIND STUDENT")
            print("5. SHOW ALL STUDENTS")
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
        sql_command = "SELECT * FROM students"
        self.__db_cursor.execute(sql_command)
        result = self.__db_cursor.fetchall()
        stu_list = []
        for row in result:

            stu_info = [row[0], row[1], row[2], row[3], row[4], row[5], row[6]]
            stu_list.append(stu_info)

        print(tabulate(stu_list, headers=["ID", "NAME", "BIRTHDATE", "SEX", "ADDRESS", "PHONE", "EMAIL"], numalign="left"))

    def __input_stu_info(self):
        self.__stu_name = input("STUDENT NAME: ")
        self.__stu_birthdate = input("BIRTHDATE: ")
        self.__stu_sex = input("SEX: ")
        self.__stu_address = input("ADDRESS: ")
        self.__stu_phone = input("PHONE: ")
        self.__stu_email = input("EMAIL: ")

    def __validate_data(self):
        is_error = False
        # validate name
        if len(self.__stu_name) <= 0 or len(self.__stu_name) > 30:
            logger.error("Name must be at least 30 characters")
            is_error = True

        # validate date of birth
        format = "%Y-%m-%d"
        # using try-except to check for truth value
        try:
            bool(datetime.strptime(self.__stu_birthdate, format))
        except ValueError:
            logger.error("PLEASE ENTER A VALID DATE OF BIRTH: %Y-%m-%d")
            is_error = True

        # validate phone number
        if len(self.__stu_phone) > 11 or len(self.__stu_phone) < 10:
            logger.error("PHONE NUMBER MUST BE AT LEAST 10-11 CHARACTERS AND MORE THAN")
            is_error = True
        if (not self.__stu_phone.isdigit()):
            logger.error("PHONE NUMBER MUST BE DIGIT")
            is_error = True

        # validate email
        if not self.__stu_email.__contains__('@'):
            logger.error("EMAIL MUST CONTAIN AT LEAST ONE @")
            is_error = True

        return is_error

    def __add_data(self):
        #Input information from keyboard
        print("INPUT STUDENT INFORMATION:")
        # self.stu_id = input("STUDENT ID: ")
        self.__input_stu_info()

        if self.__validate_data():
            return
        
        sql_cmd =   """
            INSERT INTO `students`    (`stu_name`, `stu_birthdate`, `stu_sex`, `stu_address`, `stu_phone`, `stu_email`) 
            VALUES     (%s, %s, %s, %s, %s, %s)
                    """
        vals =  (self.__stu_name, self.__stu_birthdate, self.__stu_sex, self.__stu_address, self.__stu_phone, self.__stu_email)
        self.__db_cursor.execute(sql_cmd, vals)
        self.__db_conn.commit()
        logger.info(("ADD STUDENT SUCCESSFULLY!"))


    def __update_data(self):
        print("--UPDATE STUDENT INFORMATION--")
        print("ENTER STUDENT ID:")
        while True:
            stu_ID_input = input("STUDENT ID: ")
            self.__input_stu_info()
            sql_cmd =   "UPDATE students SET stu_name = %s, stu_birthdate = %s, stu_sex = %s, stu_address = %s, stu_phone = %s, stu_email = %s WHERE stu_id = %s"
            self.__db_cursor.execute(sql_cmd, (self.__stu_name, self.__stu_birthdate, self.__stu_sex, self.__stu_address, self.__stu_phone, self.__stu_email, stu_ID_input))
            if (self.__db_conn.commit()):
                logger.error("UPDATE STUDENT FAILED!")               
            else:
                logger.info("UPDATE STUDENT SUCCESSFULLY!") 
            print('ID NOT FOUND')

            

    def __delete_data(self):
        while True:
            print("--FIND STUDENT INFORMATION--")
            stu_ID_input = input("ENTER STUDENT ID: ")
            sql_cmd =   "DELETE FROM students WHERE stu_id = %s"
            self.__db_cursor.execute(sql_cmd, [stu_ID_input])
            if(self.__db_conn.commit()):
                logger.error("DELETE STUDENT FAILED!")
            else:
                logger.info("DELETE STUDENT SUCCESSFULLY!")
            print('ID NOT FOUND')

           
    def __search_data(self):
        print("--FIND STUDENT INFORMATION--")
        while True:
            print("1. FIND STUDENT BY ID")
            print("2. FIND STUDENT BY NAME")
        
            key = int(input("Enter your choice: "))
            if key == 1:
                self.__search_student_byID()
            elif key == 2:
                self.__search_student_byName()
            elif key == 0:
                print ("You have exited the program")
                return
            else:
                print ("Invalid choice")
                print ("Please try again")

    def __search_student_byID(self):
        while True:
            stu_ID_input = int(input("ENTER STUDENT ID: "))
            sql_cmd = "SELECT * FROM students WHERE stu_id = %s"
            self.__db_cursor.execute(sql_cmd, [stu_ID_input])
            results = self.__db_cursor.fetchall()
            for row in results:
                #logger.info(row)
                print("--STUDENT INFORMATION--")
                print(f"STUDENT ID: {stu_ID_input}")
                print(f"STUDENT NAME: {row[1]}")
                print(f"STUDENT BIRTHDATE: {row[2]}")
                print(f"STUDENT SEX: {row[3]}")
                print(f"STUDENT ADDRESS: {row[4]}")
                print(f"STUDENT PHONE: {row[5]}")
                print(f"STUDENT EMAIL: {row[6]}")
            print('ID NOT FOUND')
            
    def __search_student_byName(self):
        while True:
            stu_name_input = input("ENTER STUDENT Name: ")
            sql_cmd = "SELECT * FROM students WHERE stu_name = %s"
            self.__db_cursor.execute(sql_cmd, [stu_name_input])
            results = self.__db_cursor.fetchall()
            for row in results:
                #logger.info(row)
                print("--STUDENT INFORMATION--")
                print(f"STUDENT ID: {row[0]}")
                print(f"STUDENT NAME: {stu_name_input}")
                print(f"STUDENT BIRTHDATE: {row[2]}")
                print(f"STUDENT SEX: {row[3]}")
                print(f"STUDENT ADDRESS: {row[4]}")
                print(f"STUDENT PHONE: {row[5]}")
                print(f"STUDENT EMAIL: {row[6]}")

            print('NAME NOT FOUND')
        

