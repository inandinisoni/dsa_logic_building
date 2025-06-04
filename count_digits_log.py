n=int(input("enter a number to count digit "))
from math import *
def countDigits(n):
    if n == 0:
        return 1
    return int(log10(n)) + 1
print(countDigits(n))