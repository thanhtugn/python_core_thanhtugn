str = input()

char = 0
digit = 0
symbol = 0

for char in str:
    if char.isalpha():
        char += 1
    elif char.isdigit():
        digit += 1
    else:
        symbol += 1

print("Chars =", char, "Digits =", digit, "Symbol =", symbol)

''' import re

str = input('Nhập chuỗi: ')

char = re.findall("[a-zA-Z]",str)
print("Chars  = ",len(char))

digit = re.findall("[0-9]",str)
print("Digits = ",len(digit))

symbol = re.sub(r"[a-zA-Z0-9]","",str)
print("symbol = ",len(symbol)) '''
