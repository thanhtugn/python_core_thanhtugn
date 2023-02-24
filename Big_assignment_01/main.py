from main_stu import main_stu
from main_sub import main_sub
while 1 == 1:
    print ("--MAIN MENU--")
    print ("1. STUDENT")
    print ("2. SUBJECT")
    print ("0. EXIT")
    
    key = int(input("Enter your choice: "))
    if key == 1:
       main_stu.main_stu()

    elif key == 2:
        main_sub.main_sub()

    elif key == 0:
        print ("You have exited the program")
        break
    else:
        print ("Invalid choice")
        print ("Please try again")
        

    

