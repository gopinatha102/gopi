a = "gopinath python automation"
b = a.replace(" ", "")
c = list("".join(b))
n = len(c)
for num in range(n):
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           c.insert(num, "-")

output = "".join(c)
print(output)

"""
a = [10, 1, 2, 3, 5,4]
for i in range(len(a)):
    for j in range(i, len(a)):
        if a[i] < a[j]:
            temp = a[j]
            a[j] = a[i]
            a[i] = temp
print(a)


# prime number
n = int(input("Enter ranger :"))
for num in range(n):
    if num > 0:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print("n--->", num)
            
"""