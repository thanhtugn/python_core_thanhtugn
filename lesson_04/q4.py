list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
list2.reverse
n = 0
k = 0
while (n < len(list1)):
    n += 1
    k -= 1
    val = (list1[n-1] , list2[k])
    print (val)

    