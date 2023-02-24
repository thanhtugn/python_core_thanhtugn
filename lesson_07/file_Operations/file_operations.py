'''
1. Open file
2. Read file
3. Write file
4. Close file
'''

#1 Open file to read
file_open = open('test_rw.txt','r', encoding='utf-8') 
# Read
content = file_open.read()
print(content)
#Close
file_open.close()

#method 2
with open('test_rw.txt','r', encoding='utf-8') as file_open:
    content = file_open.read()
    print(content)