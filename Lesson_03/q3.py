str = str(input('Nhập chuỗi: '))

lower = []
upper = []

for char in str:
    if char.islower():
        lower.append(char)
    else:
        upper.append(char)

newstr = ''.join(lower + upper)
print(newstr)



''' import re 

str = str(input('Nhập chuỗi: '))

strl = re.findall("[a-z]",str)
lower = "".join(strl)

stru = re.findall("[A-Z]",str)
upper = "".join(stru)

print(lower+upper) '''

