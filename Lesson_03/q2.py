print("Nhập vào chuỗi của bạn: ")
s1 = str(input())
s2 = str(input())

lenstr = len(s1)
lencen = lenstr//2

s3 = (s1[:lencen]+s2+s1[lencen:])
print (s3)


