print("Hello, World!")
list1=[10,20,30,40]
list2=[]
num=list1[0]
for i in range(len(list1)):
	if(list1[i]>num):
		num=list1[i]
print(num)

