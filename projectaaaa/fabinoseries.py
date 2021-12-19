num=int(input("Enter the number :"))
n1=0
n2=1
print(n1)
print(n2)
for i in range(2,num):
    result=n1+n2
    print(result)
    n1=n2
    n2=result