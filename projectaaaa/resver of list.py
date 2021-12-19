"""mylist=[10,11,12,13,14,15]
print("Before the reverse",mylist)
size=len(mylist)
length=int(size/2)
for i in range(length):
    temp=mylist[i]
    mylist[i]=mylist[size-i-1]
    mylist[size-i-1]=temp
print("After the Reverse ",mylist)"""

"""mylist=[10,20,30,40,10,10]
x=10
count=0
for i in range(0,len(mylist)):
    if mylist[i]==x:
        count=count+1
print("the give number occure of",x,"is",count)"""
mylist=[3,4,2]
mylist2=1
for i in range(0,len(mylist)):
    mylist2=mylist2*mylist[i]
print(mylist2)