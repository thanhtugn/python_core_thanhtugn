from object.student import Student
from object.subject import Subject
from object.score import Score
import time

def main_flow():
    

    while True:
        print ("--MAIN MENU--")
        print ("1. STUDENT")
        print ("2. SUBJECT")
        print ("3. SCORE")
        print ("0. EXIT")
        print("--------------------------------")

        key = int(input("Enter your choice: "))
        if key == 1:
            stu_obj = Student()
            stu_obj.display_menu()
        elif key == 2:
            sub_obj = Subject()
            sub_obj.display_menu()
        elif key == 3:
            sco_obj = Score()
            sco_obj.display_menu()
        elif key == 0:
            print ("You have exited the program")
            time.sleep(1)
            return
        else:
            print ("Invalid choice")
            print ("Please try again")
        
if __name__ == '__main__':
    main_flow()