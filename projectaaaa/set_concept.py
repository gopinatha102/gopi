"""#creat empty set and add ()
s=set()
s.add(10)
s.add(20)
s.add(40)
s.add(10)
print(s)
#using update()
l=[50,60,70,40]
t=(10,20,30,40)
s.update(t,l,range(1,10),"durga")
print(s)

#using copy ()

s1=s.copy()
print(id(s))
print(id(s1))
print(s1)

#using pop()
print(s.pop())
print(s.pop())
#remove()
print(s.remove(4))
print(s)
#discard()
print(s.discard(40))
print(s)

#clear
s.clear()
print(s)

#mathamatical expessions
s1={10,20,30,40}
s2={20,30,40,50}
print(s1.union(s2)) #{10,20,30,40}
print(s1|s2)             #{10,20,30,40}
print(s1.intersection(s2))#{20,30,40}
print(s1&s2)               #{20,30,40}
print(s1.difference(s2))   #{10}
print(s1-s2)               #{10}
print(s2.difference(s1))  #{50}
print(s1.symmetric_difference(s2))#{10,50}
print(s1^s2)                      #{10,50}"""

#set compreshension

s={x*x for x in range(1,10)}
print(s)