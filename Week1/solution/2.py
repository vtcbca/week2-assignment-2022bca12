Write a python script to enter any number and print the sum of its digit.
n=int(input("enter a number:"))
total=0
while(n>0):

    digit=n%10
    total=total+digit
    n=n//10
print("the total sum of digit is:",total)    
