import math
from student import Student
class student_management:
    student_list = []

    def add_student(self):
        num_stu_add = int(input("Enter number of students to add: "))
        with open("student.txt", "w") as student_file:
            for i in range(1, num_stu_add + 1):
                print("Enter information of student {}:".format(i))
                id = input("Enter student id: ")
                fullname = input("Enter full name: ")
                birthdate = input("Enter birthdate: ")
                sex = input("Enter sex: ")
                address = input("Enter address: ")
                phone = input("Enter number of phone: ")
                email = input("Enter email: ")
                student_file.write(id + "|" + fullname + "|" + birthdate + "|" + sex + "|" + address + "|" + phone + "|" + email + "\n")
                stu = Student(id, fullname, birthdate, sex, address, phone, email)
                self.student_list.append(stu)

    def num_student(self):
        return self.student_list.__len__()
        
    def update_student(self, id):
        stu:Student = self.find_student_by_id(id)
        if stu != None:
            fullname = input("Enter full name: ")
            birthdate = input("Enter birthdate: ")
            sex = input("Enter sex: ")
            address = input("Enter address: ")
            phone = input("Enter number of phone: ")
            email = input("Enter email: ")
            stu._fullname = fullname
            stu._birthdate = birthdate
            stu._sex = sex
            stu._address = address
            stu._phone = phone
            stu._email = email


        else:
            print("Student not found")
    
    def find_student_by_id(self, id):
        SearchResult = None
        if (self.num_student() > 0):
            for stu in self.student_list:
                if (stu._id == id):
                    SearchResult = stu
        return SearchResult

    def find_student_by_name(self, fullname):
        return_list = []
        if (self.num_student() > 0):
            for stu in self.student_list:
                if (fullname.upper() == stu._fullname.upper()):
                    return_list.append(stu)
        return return_list
    
    def delete_student(self, id):
        isDeleted = False
        stu = self.find_student_by_id(id)
        if stu != None:
            self.student_list.remove(stu)
            isDeleted = True
        return isDeleted
    
    def show_student(self ,return_list):
        print ("{:<8} {:<18} {:<8} {:<8}{:<8} {:<8} {:<8}"
              .format("ID", "Full name","Birthdate", "Sex", "Address", "Phone", "Email"))

        if (return_list.__len__() > 0):
            for stu in return_list:
               print ("{:<8} {:<18} {:<8} {:<8}{:<8} {:<8} {:<8}".format(stu._id, stu._fullname, stu._birthdate, stu._sex, stu._address, stu._phone, stu._email))

    def get_student_list(self):
        return self.student_list

             


        
                

    




        
        


                

        
