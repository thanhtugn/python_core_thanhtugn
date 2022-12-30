str = input()

char_dict = dict()

for char in str:
    count = str.count(char)
    char_dict[char] = count
print('Result:', char_dict)