"""#WAP To Find second largest Number
l=[10,20,30,40,50]
size=len(l)
max_number=max(l[0],l[1])
second_max=min(l[0],l[1])

for i in range(2,size):
    if l[i]>max_number:
        second_max=max_number
        max_number=l[i]
    elif l[i]>second_max:
        second_max=l[i]

print("First maxmium Number in list is  :",max_number)
print("Second maxmium Number in list is :",second_max)

#WAP To Find Second smallest Number

l=[10,20,5,80,50]
size=len(l)
first_min=min(l[0],l[1])
second_min=max(l[0],l[1])
for i in range(2,size):
    if l[i]<first_min:
        second_min=first_min
        first_min=l[i]
    elif l[i]<second_min:
        second_min=l[i]
print("First smallest Number in list is",first_min)
print("Second smallest Number in list is",second_min)

#WAP To given squence find prime number
l=[10,20,5,3,50,2,9]
size=len(l)
count=0
for i in l:
    if i%2==0:
        count=count+1
        print("given Squence is not prime Number is ", i )
    else:

        print("given squencen is prime Number",i )

#WAP To GIVEN SQUEN IS POWER USING lambda function

l=[10,20,30,40,50]
mylist2=map(lambda n:n*n,l)
for x in mylist2:
    print("power of given squence using map function is:",x)

l=[10,20,30,40,5]
mylist2=filter(lambda n:n%2==0,l)
for x in mylist2:
    print("filter of given squenc is :",x)

from functools import *
l=[1,2,3,5]
mylist2=reduce(lambda x,y:x+y,l)
print(mylist2)

#WAP to given sequence is factorial

def fact(a):
    if a==1 or a==0:
        return 1
    else:
        result=a*fact(a-1)
        return result
n=fact(5)
print(n)

#sort
l=[10,20,30,40,5]
l2=l.sort(reverse=True)
print(l)
print(l2)"""

num=[10,20,30,50,10,5]
num2=[10,20,80,90]
l=[x for x in num2 if x not in num]
print(l)

str="gopi nath is very good "
l=str.split()
words=[[word.upper(),len(word)] for word in l]
print(words)

vowels=["a","e","i","o","u"]
str1=input("Enter the string:")
l=[letter for letter in str1 if letter in vowels ]
print(l)
"""found=[]
for x in str:
    if x in vowels:
        if x not in found:
            found.append(x)
found.sort()
print(found)"""

string="hello "
string2="world"
string3=string +" "+ string2
print(string3)
