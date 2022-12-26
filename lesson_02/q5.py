print("Nhập  n: ",end='')
n = int(input())
if n > 0:
    tong=0
    for i in range(1, n + 1):
        tong=tong+i
    print("Tổng dãy số từ 1 đến ",n," là: ",tong)
else:
    print("Vui lòng nhập n > 0!")
