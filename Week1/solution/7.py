Write a python script to enter any string, replace vowel with its position number.
n=input("Enter string :")
new=""
for i in range(len(n)):
    if i%2!=0:
        new+=n[i]
    else:
        new+=str(i)
print(new)
