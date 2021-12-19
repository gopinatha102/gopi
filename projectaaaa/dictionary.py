"""#dictionary empty cration
d={}
d[100]="durga"
d[200]="ravi"
d[300]="shiva"
print(d)
d[100]="gopi"
print(d)
d[400]="durga"
d[500]="gopi"
d[600]="ravi"
print(d)"""

"""#how to acesss data in dictionary
d={100:"durga",200:"ravi",300:"shiva"}
key=int(input("Enter the aceess key :"))
if key in d:
    print("The key is avialble is ",d[key])
else:
    print("the value of dictionary is not avillable")
"""
"""#write record of number of students
rec={}
n=int(input("Enter the Number of Students"))
for i in range(n):
    name=input("Enter student name:")
    marks=int(input("Enter Markes of Students:"))
    rec[name]=marks

print("name","\t\t","marks")
print("*"*20)
for k in rec:
    print(k,"\t\t",rec[k])"""

"""#how to deleted key in dictionary
d={100:"ravi",200:"gopi",300:"shiva"}
print(d)
del d[100]
print(d)
del d
print(d)"""

"""#how to create empty dictionary
d=dict()
d=dict({100:"dugra",300:"ravi"})
d=dict([(100,"durga"),(200,"ravi"),(300,"gopi")])
print(d)

#how to use pop methode and popitems
d={10:"gopi",20:"ravi",30:"mmm"}
print(d)
print(d.popitem())
d.popitem()
d.popitem()
d.popitem()
print(d)"""

"""#how to use keyes()
d={100:"durga",200:"ravi",300:"shiva"}
print(d.keys())
for key in d.keys():
    print(key)
#how to use values()
print(d.values())
for value in d.values():
    print(value)
#how to use items ()
print(d.items())
for k,v in d.items():
    print(k,"-----------",v)
d1=d.copy()
print(d1)
print(id(d1))
print(id(d))
print(d.setdefault(100,"guest"))
print(d)
d2={500:"fff"}
d.update(d2)
print(d)"""
"""#WAP to take input in keyboard sum of keyes
d=dict()
n=int(input("Enter the number of dict:"))
for i in range(n):
    key=int(input("enter the key value:"))
    value=input("Enter the value:")
    d[key]=value
print(d)
sum=0
for x in d.keys():
    sum=sum+x
print(sum)
d=eval(input("Enter the dictionary"))
sum=sum(d.keys())
print("Sum of keyes is:",sum)"""

#WAP to count letter occurrenc in given string

"""name=input("Enter The String :")
d={}
for x in name:
    d[x]=d.get(x,0)+1
for k,v in sorted( d.items()):
    #print(k,"occured",v,"times")
    print("{} occured {} times".format(k,v))"""

#WAP to Find Number vowels present in given string
word=input("Enter The String:")
vowels={"a","e","i","o","u"}
d={}
for x in word:
    if x in vowels:
        d[x]=d.get(x, 0)+1
for k,v in sorted( d.items()):
    print("{} occured {} times".format(k, v))