# first way
num = int(input("enter a number "))
result = []
for i in range(1,num+1):
    if num % i == 0:
        result.append(i)
print(result)
