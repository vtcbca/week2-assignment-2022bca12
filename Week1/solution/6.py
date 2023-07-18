Write a python script to enter any string and print only part of string. Take input of start character and end character from user.
inputString = input("enter a string:")
count = 0
for i in inputString:
      count = count + 1
newString = inputString[ 0:2 ] + inputString [count - 2: count ]
print("Input string = " + inputString)
print("New String = "+ newString)
