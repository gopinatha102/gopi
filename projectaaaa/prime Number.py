
#nuber only dived by 1 and itself is called prime number
#19 is only divied by 1 and 19 it is prime number
#10 is divided by 2,5,10 because it is not prime number
num=int(input("Enter the given Number is :"))
"""if num<0:
    print("it is not correct number")
else:
    if num%2!=0:
        
        print("It is prime number ")
    else:
        print("it is not prime no")"""
count=0
if num>1:
    for i in range(1,num+1):
        if(num%i)==0:
            count=count+1
    if count==2:
        print("given Number is Prime Number")
    else:
        print("given number is not prime number ")