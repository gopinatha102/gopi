
def replace(string, find_str, replace_str):
    string1 = string.split()
    l = list()
    l.append(find_str)
    output = []
    if find_str.istitle():
        convert = find_str.lower()
        l.append(convert)
        for i in range(len(string1)):
            if string1[i] in l:
                output.append(replace_str)
            else:
                output.append(string1[i])

    elif find_str.islower():
        convert = find_str.title()
        l.append(convert)
        for i in range(len(string1)):
            if string1[i] in l:
                output.append(replace_str)
            else:
                output.append(string1[i])

    print("output-->", " ".join(output))


string = str(input("Enter String:"))
find_str = str(input("Enter Match String:"))
replace_str = str(input("Enter Replace string:"))
replace(string, find_str, replace_str)