Write a python script to enter any string and count vowel.
v=input("Enter a string:")
count=0
i=['a','e','i','o','u','A','E','I','O','U']
for a in v:
        if v in i:
            count=count+1
print("vowel:",count)   
