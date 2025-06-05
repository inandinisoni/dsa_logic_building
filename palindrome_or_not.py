n=int(input("enter a number to find pandrome or not "))
num = n
rev = 0
while n > 0:
    digit = n % 10
    rev = (rev * 10) + digit
    n = n // 10
if num == rev:
    print("The number is a palindrome") 
else:
    print("The number is not a palindrome")