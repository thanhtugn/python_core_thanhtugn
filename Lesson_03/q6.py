str = input('Nhập chuỗi: ')
sumdigits = 0
count = 0
for char in str:
    if char.isdigit():
        sumdigits += int(char)
        count += 1

avg = sumdigits / count
print("Sum is:", sumdigits, "Average is ", avg)


'''import re

str = input('Nhập chuỗi: ')

digits = re.findall("[0-9]",str)
digits = "".join(digits)
print("Digits = ",int(digits))

n = int(digits)
k = 0
for i in list(digits):
    k += int(i)
print ("Sum digits: " , k)

avg = k / len(digits)
print ("Avg digits: ", avg)'''