n=int(input("enter a number to count digit "))
num = n
count = 0
while num > 0:
    count += 1
    num = num // 10
print(count)