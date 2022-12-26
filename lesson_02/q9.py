print("input number starts")
start = int(input())
print("input number ends")
end = int(input())
print("Prime numbers: ")
for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num, end=' ')