print("Nhập số: ")
num = int(input())
count = 0
while num != 0:
    num = num // 10
    count = count + 1
print("Số các chữ số là: ", count)