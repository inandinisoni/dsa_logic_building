n=int(input("enter a number to check armstrong or not "))
num = n
sum = 0
while n > 0:
    digit = n % 10
    sum += digit ** 3
    n = n // 10
if num == sum:
    print("The number is an Armstrong number")
else:
    print("The number is not an Armstrong number")