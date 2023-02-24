def main():
    num_emps = int(input('How many employees record to create? '))
    with open('employee.txt','w') as emp_file:
        emp_file.write('Name\t')
        emp_file.write('ID number\t')
        emp_file.write('Department\t')
        emp_file.write('\n')
        for emp in range(1, num_emps + 1):
            print(f'Enter information for employee {emp}:')
            name = input('Name: ')
            id_num = input('ID number: ')
            dept = input('Department: ')

            emp_file.write(name + '\t')
            emp_file.write(id_num + '\t')
            emp_file.write(dept + '\t')
            emp_file.write('\n')
            print('................................................................')
        print(f'All employee information are saved')

def read_emp_info():
    with open('employee.txt', 'r') as emp_file:
        for ind, line in enumberate(emp_file.readline()):
            if ind == 0:
                continue
            print('Information of employee {ind + 1}:')
            name = line.split("\t")[0]
            id_num = line.split("\t")[1]
            dept = line.split("\t")[2]
            print(f'Name: {name}')
            print(f'ID number: {id_num}')
            print(f'Department: {dept}')
            print('....................................')

if __name__ == '__main__':
    read_emp_info()

