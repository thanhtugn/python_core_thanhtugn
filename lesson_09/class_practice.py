class Student:
    def __init__(self,name_,age_,address_,number_):
        self.name = name_
        self.age = age_
        self.address = address_
        self.number = number_
        
    def get_student(self):
        print(f'Student inf: ')
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Address: {self.address}')
        print(f'Number: {self.number}')

    def set_student(self, name_, age_, address_, number_):
        self.name = name_
        self.age = age_
        self.address = address_
        self.number = number_
        

    def study(self, subject_name):
        print(f'I am studying',subject_name)

    def watch_movie(self):
        print(f'I am watching my favorite movies')



std_2 = Student('John', 20, 'London', '1234567')
std_2.get_student()





