'''Way 3 of findind factors this is the optimal way in which we iterate till only sqrt of the
number taken and uses math to do so,although this gives result not in shorted manner but we can always sort 
it using sort function '''
from math import sqrt
num = int(input("enter a number "))
result = []
for i in range(1,int(sqrt(num))+1):  # tc = o(sqrt(n))
    if num % 1 == 0:
        result .append(i)
        if num // i != i:
            result.append(num//i)
result.sort() # tc = o(nlogn)
print(result)

# tc = o(sqrt(n))  +  o(nlogn)