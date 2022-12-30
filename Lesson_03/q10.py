str = input('Nhập chuỗi: ')

res = "".join([item for item in str if item.isdigit()])

print(res)