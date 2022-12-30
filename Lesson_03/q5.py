s1 = str(input(("Nhập Chuỗi: ")))
s1l = s1.lower()
s2 = "usa"

if s2 in s1l:
    print("Số lân USA xuất hiện trong chuỗi là", s1l.count(s2))
else:
    print("Chuỗi USA không xuất hiện trong chuỗi ", s2, s1l)