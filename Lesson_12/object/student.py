from utils import *
class Student:
    def __init__(self, stu_id='', stu_name='', stu_birthdate='', stu_sex='', stu_address='', stu_phone='', stu_email=''):
        self.stu_id = stu_id
        self.stu_name = stu_name
        self.stu_birthdate = stu_birthdate
        self.stu_sex = stu_sex
        self.stu_address = stu_address
        self.stu_phone = stu_phone
        self.stu_email = stu_email

    def display_menu(self):
        while True:
            print("--------------------------------")
            print("PLEASE SELECT A FUNCTION")
            print("1. ADD NEW STUDENT")
            print("2. UPDATE STUDENT")
            print("3. DELETE STUDENT")
            print("4. FIND STUDENT")
            print("0. EXIT")
            key = input("ENTER YOUR CHOICE: ")
            if key == '1':
                self.add_student()
            elif key == '2':
                self.update_student()
            elif key == '3':
                self.delete_student()
            elif key == '4':
                self.find_student()
            elif key == '0':
                print("EXITING...")
                return
            else:
                print("INVALID CHOICE")
                print("PLEASE TRY AGAIN")

    def input_stu_info(self):
        self.stu_name = input("STUDENT NAME: ")
        self.stu_birthdate = input("BIRTHDATE: ")
        self.stu_sex = input("SEX: ")
        self.stu_address = input("ADDRESS: ")
        self.stu_phone = input("PHONE: ")
        self.stu_email = input("EMAIL: ")

    def add_student(self):
        #Input information from keyboard
        print("INPUT STUDENT INFORMATION:")
        self.stu_id = input("STUDENT ID: ")
        self.input_stu_info()

        #data format 
        stu_info = '|'.join([self.stu_id, self.stu_name, self.stu_birthdate, self.stu_sex, self.stu_address, self.stu_phone, self.stu_email, '\n'])
        add_student_status = write_txt('data/hocvien.txt', [stu_info], 'a+')
        if add_student_status:
            print("ADD STUDENT SUCCESSFULLY!")
        else:
            print("ADD STUDENT FAILED!")

    def update_student(self):
        print("--UPDATE STUDENT INFORMATION--")
        print("ENTER STUDENT ID:")
        while True:
            stu_ID_input = input("STUDENT ID: ")
            stu_infos = read_txt('data/hocvien.txt')

            #get id of student list
            for idx, stu in enumerate(stu_infos):
                stu_ID  = stu.split('|')[0]
                if stu_ID_input == stu_ID:
                    print("ENTER NEW STUDENT INFORMATION:")
                    self.input_stu_info()
                    #data format 
                    stu_info = '|'.join([stu_ID_input, self.stu_name, self.stu_birthdate, self.stu_sex, self.stu_address, self.stu_phone, self.stu_email, '\n'])
                    stu_infos[idx] = stu_info
                    add_student_status = write_txt('data/hocvien.txt', stu_infos, 'w+')
                    if add_student_status:
                        print("UPDATE STUDENT SUCCESSFULLY!")
                        return True
                    else:
                        print("UPDATE STUDENT FAILED!")
                        return False
                    
            print("STUDENT NOT FOUND!")
            print("PLEASE TRY AGAIN!")

    def delete_student(self):
        while True:
            print("--FIND STUDENT INFORMATION--")
            stu_ID_input = input("ENTER STUDENT ID: ")
            stu_infos = read_txt('data/hocvien.txt')

            #get id of student list
            for idx, stu in enumerate(stu_infos):
                stu_ID  = stu.split('|')[0]
                if stu_ID_input == stu_ID:
                    stu_infos.pop(idx)
                    add_student_status = write_txt('data/hocvien.txt', stu_infos, 'w+')
                    if add_student_status:
                        print("DELETE STUDENT SUCCESSFULLY!")
                        return True
                    else:
                        print("DELETE STUDENT FAILED!")
                        return False
            print("STUDENT NOT FOUND!")
            print("PLEASE TRY AGAIN!")
            
    def find_student(self):
        print("--FIND STUDENT INFORMATION--")
        stu_ID_input = input("ENTER STUDENT ID: ")
        stu_infos = read_txt('data/hocvien.txt')
        #get id of student list
        for idx, stu in enumerate(stu_infos):
            stu_ID  = stu.split('|')[0]
            if stu_ID_input == stu_ID:
                print("STUDENT INFORMATION:")
                print(f"STUDENT ID:, {stu_ID_input}")
                print(f"STUDENT NAME:, {stu.split('|')[1]}")
                print(f"STUDENT BIRTHDATE:, {stu.split('|')[2]}")
                print(f"STUDENT SEX:, {stu.split('|')[3]}")
                print(f"STUDENT ADDRESS:, {stu.split('|')[4]}")
                print(f"STUDENT PHONE:, {stu.split('|')[5]}")
                print(f"STUDENT EMAIL:, {stu.split('|')[6]}")
                return
        print("STUDENT NOT FOUND!")
        

