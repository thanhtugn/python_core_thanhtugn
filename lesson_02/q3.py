str = input('Nhập chuỗi: ')
print(str)

lenstr = len(str)

for i in range(0, lenstr - 1, 2):
    print("[", i, "]", str[i])