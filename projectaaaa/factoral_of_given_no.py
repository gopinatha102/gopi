"""num=int(input("Enter the Number of factorial :"))
i=0
while i<=num:
    if i==0:
        result=1
    else:
        result=num*i
    i=i+1

print(result)"""
#methode 2
"""""
factorial=1
num=0
if num<0:
    print("Factorial does not exist nagative number ")
elif num==0:
    print("Factorial of 0 is 1")
else:
    for i in range(1,num+1):
        factorial=factorial*i
    print("The Factorial of",num,"is",factorial)
print(factorial)"""

#method 3 using function
def factorial(num):
    if (num==0 or num==1):
        return 1
    else:
        return num*factorial(num-1)

num=5
fact=factorial(num)
print("Factorial of given number ",num,"is ",fact)
