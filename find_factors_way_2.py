'''way 2 better solution where we apply simple logic of maths
 and take only half of the entered number 
 iterate through the half and find factors as the 
 second half does not contain any factors other than the number itself '''
num = int(input("enter a number "))
result = []
for i in range (1,num//2 +1):
    if num % i == 0 :
        result.append(i)
result.append(num)
print(result) 