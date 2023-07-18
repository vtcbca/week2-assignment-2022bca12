Write a python script to enter any number, if it is integer number, then check its palindrom or not. Print appropriate message if it is not palindrom.
n=int(input("Enter number:"))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")
