n=int(input("enter a number "))
num = n
while num> 0:
    digit = num % 10
    print(digit)
    num = num // 10