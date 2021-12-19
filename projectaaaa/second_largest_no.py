list1=[100,30,600,50,200]
max_=max(list1[0],list1[1])
secondmax=min(list1[0],list1[1])

for x in range(2,len(list1)):
    if(list1[x]>max_):
        secondmax=max_
        max_=list1[x]
    else:
        if list1[x] > secondmax:
            secondmax = list1[x]

print("sencod largest number",secondmax)