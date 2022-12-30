print("Nhập vào chuỗi của bạn: ")
mystring = str(input())

print(mystring[0], end='')

lenstr = len(mystring)
if lenstr %2 ==0:
    lencen = lenstr//2
    print(mystring[lencen-1:lencen+1], end='')
else:
    lencen = lenstr//2
    print(mystring[lencen], end='')

print(mystring[-1],end='')