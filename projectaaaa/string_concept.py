"""message="Today is tuesuday in august"
message1=message.split()
message2=[]
for x in range(len(message1)):

    if x%2==0:
        message2.append(message1[x].upper())
    else:
        message2.append(message1[x])

output=" ".join(message2)
print(output)"""

#**************************************************************************
from typing import List, Any

"""""#given string revser
#***************************************************************************
message="today is tuesuday in august"
l=message.split()
l2=[]
i=len(l)-1
while i>=0:
    l2.append(l[i])
    i=i-1
print(l2)
output=" ".join(l2)
print(output)"""
#
#*************************************************************************
# program to reverse internal content of each word
"""message="today is tusday in august"
l=message.split()
l2=[]
i=0
while i<len(l):
    l2.append(l[i][::-1])
    i=i+1
output=" ".join(l2)
print(output)"""

#************************************************************************************
#write program given string is palladoma or not

"""str1="madaaam"
str2=str1[::-1]
if str1==str2:
    print("given string is pallidoma")
else:
    print("given string is not pallidoma")"""

#********************************************************************
"""size=len(str1)-1
leng=int(size/2)
for x in range(0,leng):
    if str1[x]==str1[size-x]:
        print("string as pallidoma")
    else:
        print("not palidoma")
"""
#**********************************************************************
"""import re
a="ip of this node is 22.225.120.45"
matcher=re.finditer("[0-9_.]",a)
for match in matcher:
    print(match.group(),end="")"""

#**************************************************************************
"""str1="a"
print(ord(str1))
print( chr(97))"""
#**************************************************************************
"""s="Learning python is very diffuclute"
s2=s.replace('diffuclute',"easy")
print(s2)
#***************************************************************************
s=input("Enter the squence of string is :")
l=s.split()
l2=[]
print(l)
for i in l:
    l2.append(i[::-1])
output=" ".join(l2)
print(output)

#*********************************************************************************
#WAP to odd and even position
#**************************************************************************
n=input("Enter the string is :")
size=len(n)
for i in range(size):
    if i%2==0:
        print("given string even  position is ",i ,"and string is ",n[i])
    else:
        print("given string odd  position is ", i, "and string is ", n[i])
#****************************************************************************************
#WAP TO Find given string how many times occurance
#**************************************************************************
s="abbabababbababb"
false=False
pos=-1
n=len(s)
count=0
while True:
    pos=s.find("bb",pos+1,n)
    if pos==-1:
        break
    print("found at position is ",pos)
    count=count+1
    flage=True
if flage==False:
    print("Not Found ")
else:
    print("the given string is",count," times found")
#***********************************************************************
#WAP TO Reverse given string
#**************************************************************************
str1=input("Enter The string:")
print(str1[::-1])
print("".join(reversed(str1)))
n=len(str1)-1
target=""
while n>=0:
    target=target+str1[n]
    n=n-1
print("reverse of string is ",target)
#***********************************************************************
#WAP To Programming reverse order of words
#**************************************************************************
str1=input("Enter the string:")
l=str1.split()
l1=[]
length=len(l)-1
while length>=0:
    l1.append(l[length])
    length=length-1
output=" ".join(l1)
print(output)

#**************************************************************************
#WAP To Programming reverse internal content  of words
#**************************************************************************
str1=input("Enter the string:")
l=str1.split()
l1=[]
i=0
while i<len(l):
    l1.append(l[i][::-1])
    i=i+1
output=" ".join(l1)
print(output)"""
"""#**************************************************************************
#WAP to merge charters of 2string into single string by taking charters alternativly
#**************************************************************************
s1=input("Enter some string1 :")
s2=input("Enter some String 2 :")
s1len=len(s1)
s2len=len(s2)
output=""
i=0
j=0
while i<s1len or j<s2len:

    if i<s1len:
        output=output+s1[i]
        i=i+1
    if j<s2len:
        output=output+s2[j]
        j=j+1
print(output))

#**************************************************************************
#WAP to sort the characters of the string and first alphabet symbols follwed by numbeics value
#**************************************************************************

s=input("Enter the string ")
s1=s2=output=""
for x in s:
    if x.isalpha():
        s1=s1+x
    else:
        s2=s2+x
for x in sorted(s1):
    output=output+x
for x in sorted(s2):
    output=output+x
print(output)"""

"""
#***************************************************************************
#WAP for the following requirements
#***************************************************************************
s=input("Enter the string")
output=""
for x in s:
    if x.isalpha():
        output=output+x
        previous=x
    else:
       output=output+previous*(int(x)-1)
print(output)

#***************************************************************************
# wap to program to perform the following activity
# input=a4k3b2
# output=aeknbd
# ***************************************************************************

s = input("Enter some string:")
output = ""
for x in s:
    if x.isalpha():
        output = output + x
        previous = x
    else:
        output = output + chr((ord(previous)) + (int(x)))

print(output)"""

"""# wap to program to remove duplicate letters
# input=abcdaabbccd
# output=abcd
# ***************************************************************************

s = input("Enter some string:")
l=[]
for x in s:
    if x not in l:
        l.append(x)
output=''.join(l)

print(output)"""


























