from utils import *
class Subject:
    def __init__(self, sub_id='', sub_name=''):
        self.sub_id = sub_id
        self.sub_name = sub_name

    def display_menu(self):
        while True:
            print("--------------------------------")
            print("PLEASE SELECT A FUNCTION")
            print("1. ADD NEW SUBJECT")
            print("2. UPDATE SUBJECT")
            print("3. DELETE SUBJECT")
            print("4. FIND SUBJECT")
            print("0. EXIT")
            key = input("ENTER YOUR CHOICE: ")
            if key == '1':
                self.add_subject()
            elif key == '2':
                self.update_subject()
            elif key == '3':
                self.delete_subject()
            elif key == '4':
                self.find_subject()
            elif key == '0':
                print("EXITING ...")
                return
            else:
                print("INVALID CHOICE")
                print("PLEASE TRY AGAIN")

    def input_sub_info(self):
        self.sub_name = input("SUBJECT NAME: ")

    def add_subject(self):
        #Input information from keyboard
        print("--INPUT SUBJECT INFORMATION--")
        self.sub_id = input("SUBJECT ID: ")
        self.input_sub_info()

        #data format 
        sub_info = '|'.join([self.sub_id, self.sub_name, '\n'])
        add_subject_status = write_txt('data/subject.txt', [sub_info], 'a+')
        if add_subject_status:
            print("ADD SUBJECT SUCCESSFULLY!")
        else:
            print("ADD SUBJECT FAILED!")

    def update_subject(self):
        print("--UPDATE SUBJECT INFORMATION--")
        print("ENTER SUBJECT ID:")
        while True:
            sub_ID_input = input("SUBJECT ID: ")
            sub_infos = read_txt('data/subject.txt')

            #get id of subject list
            for idx, sub in enumerate(sub_infos):
                sub_ID  = sub.split('|')[0]
                if sub_ID_input == sub_ID:
                    print("ENTER NEW SUBJECT INFORMATION:")
                    self.input_sub_info()
                    #data format 
                    sub_info = '|'.join([sub_ID_input, self.sub_name, '\n'])
                    sub_infos[idx] = sub_info
                    add_subject_status = write_txt('data/subject.txt', sub_infos, 'w+')
                    if add_subject_status:
                        print("UPDATE SUBJECT SUCCESSFULLY!")
                        return True
                    else:
                        print("UPDATE SUBJECT FAILED!")
                        return False
            print("SUBJECT NOT FOUND!")
            print("PLEASE TRY AGAIN!")

    def delete_subject(self):
        while True:    
            print("--FIND SUBJECT INFORMATION--")
            sub_ID_input = input("ENTER SUBJECT ID: ")
            sub_infos = read_txt('data/subject.txt')

            #get id of subject list
            for idx, sub in enumerate(sub_infos):
                sub_ID  = sub.split('|')[0]
                if sub_ID_input == sub_ID:
                    sub_infos.pop(idx)
                    add_subject_status = write_txt('data/subject.txt', sub_infos, 'w+')
                    if add_subject_status:
                        print("DELETE SUBJECT SUCCESSFULLY!")
                        return True
                    else:
                        print("DELETE SUBJECT FAILED!")
                        return False
            print("SUBJECT NOT FOUND!")
            print("PLEASE TRY AGAIN!")

    def find_subject(self):
        print("--FIND SUBJECT INFORMATION--")
        sub_ID_input = input("ENTER SUBJECT ID: ")
        sub_infos = read_txt('data/subject.txt')

        #get id of subject list
        for  sub in (sub_infos):
            sub_ID  = sub.split('|')[0]
            if sub_ID_input == sub_ID:
                print("SUBJECT INFORMATION:")
                print(f"SUBJECT ID:, {sub_ID}")
                print(f"SUBJECT NAME:, {sub.split('|')[1]}")
                return
        print("SUBJECT NOT FOUND!")
        

