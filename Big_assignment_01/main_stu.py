from student_management import student_management
class main_stu():
    def main_stu():
        stu_mng = student_management()
        while (1==1):
            print("Student Management System")
            print("1. Add student")
            print("2. Update student")
            print("3. Delete student")
            print("4. Show all students")
            print("0. Back to Main Menu")
            
            key = int(input("Enter your choice: "))
            if (key == 1):
                print("Add student")
                stu_mng.add_student()
                print('add student successfully')

            elif (key == 2):
                if(stu_mng.num_student() > 0 ):
                    print("Update student")
                    id = input("Enter student ID: ")
                    stu_mng.update_student(id)
                else:
                    print("Student list is empty")

            elif (key == 3):
                if(stu_mng.num_student() > 0 ):
                    print("Delete student")
                    id = input("Enter student ID: ")
                    if(stu_mng.delete_student(id)):
                        print('delete student successfully')
                    else:
                        print('code not found')

                else:
                    print("Student list is empty")

            elif (key == 4):
                if(stu_mng.num_student() > 0 ):
                    print("Show all students")
                    stu_mng.show_student(stu_mng.get_student_list())
                else:
                    print("Student list is empty")

            elif (key == 0):
                print("You have exited the program")
                break

            else:
                print("Invalid choice")
                print("please try again")

        print(stu_mng.num_student())



                        
                    

