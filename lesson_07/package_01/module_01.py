import math

def is_square():
    number = int(input("Enter the Num: "))
    sq_root = int(math.sqrt(number))
    return (sq_root*sq_root) == number