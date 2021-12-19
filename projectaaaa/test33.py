def f1(n1,*s):
    print(n1)
    for s1 in s:
        print(s1)

f1(10)
print("*"*20)
f1(10,20,30,40)
print("*"*20)
f1(10,"A",20,"B")
