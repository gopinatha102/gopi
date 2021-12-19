# create simple function
def wish(name):
    print("hello my name  is:", name)


wish("durga")


# to create return function
def cal(a, b):
    add = a + b
    sub = a - b
    mul = a * b
    div = a / b
    return add, sub, mul, div


result = cal(10, 20)
print("Result of cal is", result)

for i in result:
    print("result is ", i)


# write a program to find the given number is add or even

def even_odd(num):
    if num % 2 == 0:
        print("given number is even:", num)
    else:
        print("given number is odd", num)


even_odd(20)
even_odd(15)


# write programm to find factoral number
def fact(num):
    result = 1
    while num >= 1:
        result = result * num
        num = num - 1
    return result


result1 = fact(1)
result2 = fact(4)
print("Factorial of given number is ", result1)
print("Factorial of given number is ", result2)
