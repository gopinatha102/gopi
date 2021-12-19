
"""num=l[0]
min_=min(l[0],l[1])
for i in range(0,len(l)):
    if l[i]>num:
        num=l[i]
        print("Largest number in list is :",num)
    elif l[i]<min_:
        min_=l[i]
        print("Smallest Number i  list is :",min_)
print(num)
print(min_)
print(l)
"""
""""#find element in assending order 
l=[10,10,4,4,8,16]
l2=[]
for i in range(0,len(l)):
    for j in range(0,len(l)):
        if l[i]<l[j]:
            temp=l[i]
            l[i]=l[j]
            l[j]=temp

print(l)
"""


"""#find desending order
l=[10,10,4,4,8,16]
l2=[]
for i in range(0,len(l)):
    for j in range(0,len(l)):
        if l[i]>l[j]:
            temp=l[i]
            l[i]=l[j]
            l[j]=temp
print(l)
"""
#convert reverse order
"""l=[10,30,20,59,40]
size=len(l)
length=int(size/2)

for i in range(length):
    temp=l[i]
    l[i]=l[size-i-1]
    l[size-i-1]=temp
print(l)"""
