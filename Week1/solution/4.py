Write a python script to enter any number, if it is integer number, then check its armstrong or not. Print appropriate message if it is not palindrom.
n=int(input("Enter number:"))
sum=0
temp=n
while temp>0:
    dig=temp%10
    sum+=dig**3
    temp//=10
  if n==sum:
      print("the number is armstrong!")
  else:
      print("the number is not armstrong!")
