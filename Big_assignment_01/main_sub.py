from subject_management import subject_management
class main_sub():
    def main_sub():
        sub_mng = subject_management()
        while (1 == 1):
            print("1. Add new subject")
            print("2. update subject")
            print("3. delete subject")
            print("4. view all subjects")
            print("0. Back to Main Menu")

            key = int(input("Enter your choice: "))
            if (key == 1):
                print("Add new subject")
                sub_mng.add_subject()
                print("Add new subject successfully")

            elif (key == 2):
                if(sub_mng.num_subjects() > 0):
                    print("Update subject")
                    code = input("Enter subject code: ")
                    sub_mng.update_subject(code)
                else:
                    print("Subject list is empty")

            elif (key == 3):
                if(sub_mng.num_subjects() > 0):
                    print("Delete subject")
                    code = input("Enter subject code: ")
                    if(sub_mng.delete_subject(code)):
                        print("Delete subject successfully")
                    else: 
                        print("Object not found")
                else: 
                    print("Subject list is empty")

            elif (key == 4):
                if(sub_mng.num_subjects() > 0):
                    print("View all subjects")
                    sub_mng.show_subjects(sub_mng.get_subjects_list())
                else:
                    print("Subject list is empty")
            elif (key == 0):
                print("You have exited the program")
                break
            else:
                print("Invalid choice")
                print("Please try again")
                

                



                
            
