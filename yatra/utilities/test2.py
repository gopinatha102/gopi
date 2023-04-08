def read_file_yield(file_name):
    text_file = open(file_name, 'r')
    while True:
        line_data = text_file.readline()
        if not line_data:
            text_file.close()
            break
        yield line_data


def read(file_data):
    listl = []
    i = 0
    for line in file_data:
        strip_lines = line.strip()
        listi = strip_lines.split()
        if "<" in listi[0]:
            listl.append(listi)
            i = i + 1
        elif ">" in listi[0]:
            listl.append(listi)
            i = i + 1
        else:
            listl[i - 1].extend(listi)
    print("heloo", listl)


file_data = read_file_yield("text.txt")
print(type(file_data))
read(file_data)
