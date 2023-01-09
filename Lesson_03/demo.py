input_str = input('Input:')
Sum = 0
digit_count = 0
for char in input_str:
    if char.isdigit():
        Sum += int(char)
        digit_count += 1
print("Sum: ", Sum, "Average is: ", Sum/digit_count)


