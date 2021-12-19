list1=[0,51,8,50,1,9,10,3]
min_=min(list1[0],list1[1])#51
secondmin_=max(list1[0],list1[1])#200

for x in range(2,len(list1)):
    if list1[x]<min_:       #7>200 50>51
        secondmin_=min_
        min_=list1[x]

    else:
        if list1[x]<secondmin_:
            secondmin_=list1[x]
            list1[x]=secondmin_
print(min_)
print(secondmin_)