import math
from subject import subject
class subject_management:
    subjects_list = []
    
    def add_subject(self):
        num_subjects_add = int(input("Enter number of subjects to add: "))
        with open("subjects.txt", "w") as subject_file:
            for i in range(1, num_subjects_add + 1):
                print("Enter information for subject {}:".format(i))
                code = input("Subject code: ")
                name = input("Subject name: ")
                subject_file.write(code + "|" + name + "\n")
                sub = subject(code, name)
                self.subjects_list.append(sub)

    def num_subjects(self):
        return self.subjects_list.__len__()
    
    def update_subject(self, code):
        sub:subject = self.find_subject_bycode(code)
        if (sub!= None):
            name = input("Enter new subject name: ")
            sub._name = name
        else:
            print("Subject not found")
        
    def find_subject_bycode(self, code):
        SearchResult = None
        if (self.num_subjects() > 0):
            for sub in self.subjects_list:
                if (sub._code == code):
                    SearchResult = sub
        return SearchResult

    def find_subject_byname(self, name):
        return_list = []
        if (self.num_subjects() > 0):
            for sub in self.subjects_list:
                if (name.upper() == sub.name.upper()):
                    return_list.append(sub)
        return return_list
    
    

    def delete_subject(self, code):
        isDeleted = False
        sub = self.find_subject_bycode(code)
        if sub != None:
            self.subjects_list.remove(sub)
            isDeleted = True
        return isDeleted
    

    def show_subjects(self, return_list):
        print ("{:<8} {:<18}".format("Code", "Name"))
        if (return_list.__len__() > 0):
            for sub in return_list:
                print ("{:<8} {:<18}".format(sub._code, sub._name))

    def get_subjects_list(self):
        return self.subjects_list







                


