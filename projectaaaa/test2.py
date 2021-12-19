"t----4"
"e----5"
"s-----3"
"r---6"
string="Tester"
d={}
str2=string.lower()
i=1
for x in str2:
    if x not in d:
        d[x]=i
        i+=1
    else:
        d[x]=i
        i=i+1

for k,v in d.items():
    print("{}-----{}".format(k,v))


