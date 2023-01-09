list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
finalist = []
n = 0
while (n < len(list1)):
    n += 1
    val = list1[n-1]+list2[n-1]
    finalist.append(val)
print(finalist)
