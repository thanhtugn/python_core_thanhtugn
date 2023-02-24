# 1. Write a program to read an entire the sample.txt file
from os import remove
from tkinter import W


def read_file(filename):
    with open(filename, 'r') as f:
        print(f.read())

# file_read('sample.txt')

# 2. Write a program to read an first/last n line of the sample.txt file with n and first/last are arguments come from keyboard.
# def file_read_first_last(filename, n, first=True):
#     with open(filename, 'r') as f:
#         line = [next(f) for x in range(n)]
#         print(line)

def read_file_first_last(filename, n, first=True):
    with open(filename, 'r') as f:
        lines = f.readlines()
        if first:
            print(f'{n} first lines:')
            print(lines[:n])
        else:
            print(f'{n} last lines:')
            print(lines[-n:])

# n = int(input('Enter n: '))
# first = input("True/False: ")
# while (first != 'True' and first != 'False'):
#     print('Enter first again!')
#     first = input("True/False: ")

# if first == 'True':
#     first = True
# else: 
#     first = False

# read_file_first_last('sample.txt', n, first)

# 3. Write a program to read line by line os the sample.txt file and store them in a list. Sort the list by length of each line.
def read_file_line(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        lines.sort(key=len)
        for line in lines:
            print(line)

# read_file_line('sample.txt')

# 3. Write a program to append a line to the sample.txt file with line is argument come from keyboard. Print the length of file and
# the line with longest length.

def append_file(filename, text):
    with open(filename, 'a') as f:
        f.write(text)
        lines = f.readlines()
        print(f'File length: {len(lines)}')
        lines.sort(key=len)
        print('The longest sentence is:')
        print(lines[-1])

# text = input('Enter a text: ')
# append_file('sample.txt', text) 

# 4. Write a program to count frequency of each word in the sample.txt file.
def word_count(filename):
    word_count = dict()
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            for word in line.split(' '):
                if word not in word_count:
                    word_count[word] = 1
                else:
                    word_count[word] += 1
    word_count = sorted(word_count.items(), key=lambda item: item[1], reverse=True)
    print(word_count)

# word_count('sample.txt')

# 5. Write a program to remove a line which line number is a argument from the keyboard.
def delete_line(filename, n):
    with open(filename, 'r') as f:
        lines = f.readlines()
    with open(filename, 'w') as f:
        for idx, line in enumerate(lines):
            if idx != n:
                f.write(line)
# n = int(input('Enter the line number: '))
# delete_line('sample.txt', n)
# -------------------

# 6. Write a program to store the below content in a file name sample_w.txt. Remove blank line in the file.
'''
While CMR portrays extreme competency in capturing all data types, here are specific means through which it benefits your enterprise -

1. Automation Scope Expansion
CMR lets you leverage 85% of the untapped and unstructured data prevalent in your organization, implying that you receive enhanced results by automating deeper processes as well as more complex data.

2. Greater accuracy with data certainty
CMR offers a better capture rate with over 80% accuracy of consistently capturing information. CMR lets you promote the level of data certainty to attain a higher percentage of straight-through processing.
'''

def write_file(filename, text):
    with open(filename, 'w') as fw: 
        fw.write(text)

text = '''
While CMR portrays extreme competency in capturing all data types, here are specific means through which it benefits your enterprise -

1. Automation Scope Expansion
CMR lets you leverage 85% of the untapped and unstructured data prevalent in your organization, implying that you receive enhanced results by automating deeper processes as well as more complex data.

2. Greater accuracy with data certainty
CMR offers a better capture rate with over 80% accuracy of consistently capturing information. CMR lets you promote the level of data certainty to attain a higher percentage of straight-through processing.
'''
text = "\n".join([s for s in text.split("\n") if s])
write_file('sample_w.txt', text)