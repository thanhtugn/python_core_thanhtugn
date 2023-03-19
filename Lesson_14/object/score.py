from utils.txt_file_ops import *
from utils.Database_conn import *
from object.base_class import *
from loguru import logger
from tabulate import tabulate
from datetime import datetime

class Score:
    def __init__(self, stu_id='', subject_id='', prog_score=0, end_score=0, final_score=''):
        self.__stu_id = stu_id
        self.__subject_id = subject_id
        self.__prog_score = prog_score
        self.__end_score = end_score
        self.__final_score = final_score
        db_obj = SQLConnector()
        self.__db_conn = db_obj.create_connection()
        self.__db_cursor = self.__db_conn.cursor()

    def display_menu(self):
        while True:
            print("--------------------------------")
            print("PLEASE SELECT A FUNCTION")
            print("1. ADD NEW SCORE")
            print("2. UPDATE SCORE")
            print("3. DELETE SCORE")
            print("4. SEARCH SCORE")
            print("5. SHOW SCORE")
            print("6. STATISTIC SCORE")
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
            elif key == '6':
                self.__statistics_score
            elif key == '0':
                print("EXITING ...")
                return
            else:
                print("INVALID CHOICE")
                print("PLEASE TRY AGAIN")

    def __get_data(self):
        sql_cmd = "SELECT * FROM score"
        self.__db_cursor.execute(sql_cmd)
        result = self.__db_cursor.fetchall()
        sco_list = []
        for row in enumerate(result):
            sco_info = [row[0], row[1], row[2], row[3], row[4]]
            sco_list.append(sco_info)

        print(tabulate(sco_list, headers=["STUDENT ID", "SUBJECT ID", "PROG SCORE", "END SCORE", "FINAL SCORE"], numalign="left"))


    def __input_score(self):
        self.__prog_score = float(input("ENTER YOUR PROGRAM SCORE: "))
        self.__end_score =  float(input("END YOUR END SCORE: "))
        # self.__stu_id = input("ENTER STUDENT ID: ")
        # self.__sub_id = input("ENTER SUBJECT ID: ")

    def __call_final_score(self):
        self.__final_score = (int(self.__prog_score) + int(self.__end_score)*2)/3

    def __validate_data(self):
        is_error = False
        if (self.__prog_score ) < 0 or (self.__prog_score )> 100:
            logger.error('SCORE MUST BE AT 0-100. PLEASE ')
            is_error = True

        if (self.__end_score ) < 0  or (self.__end_score )> 100:
            logger.error('SCORE MUST BE AT 0-100. PLEASE ')
            is_error = True
        return is_error

    def __add_data(self):        
        print("--ADD SCORE--")
        self.__stu_id = input("ENTER STUDENT ID: ")
        self.__subject_id = input("ENTER SUBJECT ID: ")
        self.__input_score()
        if self.__validate_data():
            return
        self.__call_final_score()

        sql_cmd = """INSERT INTO score (stu_id, subject_id, prog_score, end_score, final_score) 
                     VALUES (%s, %s, %s, %s, %s)
                  """
        vals = (self.__stu_id, self.__subject_id, self.__prog_score, self.__end_score, self.__final_score)
        self.__db_cursor.execute(sql_cmd, vals)
        self.__db_conn.commit()
        logger.info(("ADD SCORE SUCCESSFULLY!"))


    def __update_data(self):
        while True:
            print("--UPDATE SCORE--")
            stu_id_input = input("ENTER STUDENT ID: ")
            sub_id_input = input("ENTER SUBJECT ID: ")
            self.__input_score()
            self.__call_final_score
            sql_cmd = """UPDATE score SET prog_score = %s, end_score = %s, final_score = %s WHERE stu_id = %s AND subject_id = %s"""
            self.__db_cursor.execute(sql_cmd, (self.__prog_score, self.__end_score, self.__final_score, stu_id_input, sub_id_input))
            if (self.__db_conn.commit()):
                logger.error(("UPDATE SCORE FAILED!"))
            else:
                logger.info("UPDATE SCORE SUCCESSFUL!")
            print('SCORE NOT FOUND. PLS TRY AGAIN')



    def __delete_data(self):  
        while True:      
            print("--DELETE SCORE--")
            stu_id_input = input("ENTER STUDENT ID: ")
            sub_id_input = input("ENTER SUBJECT ID: ")
            
            sql_cmd = "DELETE FROM score WHERE stu_id = %s AND subject_id = %s"
            self.__db_cursor.execute(sql_cmd, [stu_id_input], [sub_id_input])
            if(self.__db_conn.commit()):
                logger.error("DELETE SCORE FAILED!")
            else:
                logger.info("DELETE SCORE SUCCESSFULLY!")
            print('SCORE NOT FOUND. PLS TRY AGAIN')

    def __search_data(self):
        while True:
            print("--SEARCH SCORE--")
            stu_id_input = input("ENTER STUDENT ID: ")
            sub_id_input = input("ENTER SUBJECT ID: ")

            sql_cmd = "SELECT * FROM score WHERE stu_id = %s AND subject_id = %s"
            self.__db_cursor.execute(sql_cmd, [stu_id_input], [sub_id_input])
            result = self.__db_cursor.fetchall()
            for row in result:
                print("SCORE INFORMATION:")
                print(f"STUDENT ID: {stu_id_input}")
                print(f"SUBJECT ID: {sub_id_input}")
                print(f"PROGRAM SCORE: {row[2]}")
                print(f"END SCORE: {row[3]}")
                print(f"FINAL SCORE: {row[4]}")
            print('ID NOT FOUND')


    def __statistics_score(self):
        score_a, score_b , score_c, score_d = [], [], [], []
        score_infos = read_txt('data/scores.txt')
        for sco in score_infos:
            finally_score = float(sco.split('|')[4])
            if finally_score >= 90 and finally_score <= 100:
                score_a.append(finally_score)
            elif finally_score >= 80 and finally_score < 90:
                score_b.append(finally_score)
            elif finally_score >= 50 and finally_score <70:
                score_c.append(finally_score)
            else:
                score_d.append(finally_score)

        score_a_str = "NUM OF A: " + str(len(score_a))
        score_b_str = "NUM OF B: " + str(len(score_b))
        score_c_str = "NUM OF C: " + str(len(score_c))
        score_d_str = "NUM OF D: " + str(len(score_d))
        score_statistics = ("\n").join([score_a_str, score_b_str, score_c_str, score_d_str])
        if write_txt('data/scores_statistic.txt', [score_statistics], 'w+'):
            print("WROTE SCORE STATISTICS INTO TXT FILE SUCCESSFULLY")
        else:
            print("WROTE SCORE STATISTICS INTO TXT FILE FAILED")