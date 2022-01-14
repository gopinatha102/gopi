import os
import sys

Filename = input("Enter The File Name:")
if os.path.isfile(Filename):
    print("File Exists:", Filename)
    f = open(Filename, "r")

else:
    print("File Does Not Exist:", Filename)
    sys.exit(0)
lcount = wcount = ccount = 0

for line in f:
    lcount = lcount + 1
    ccount = ccount + len(line)
    word = line.split()
    wcount = wcount + len(word)

print("length of Line count is lcount=", lcount)
print("character count of File =", ccount)
print("Word count of File is =", wcount)
