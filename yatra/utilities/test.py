def read_file():
    with open("text.txt", "r") as f:
        lines = f.readlines()
    return lines


def line_arrangement():
    event_code = read_file()
    listl = []
    i = 0
    for line in event_code:
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
    return listl


def read_file_yield(file_name):
    text_file = open(file_name, 'r')
    while True:
        line_data = text_file.readline()
        if not line_data:
            text_file.close()
            break
        yield line_data


file_data = read_file_yield("text.txt")
print(type(file_data))
listl = []
i=0
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
print("heloo",listl)

def binary_hex_opcode(opcode):
    binary = bin(int(opcode, 16)).replace("0b", "")
    ocf = "".join(reversed([str(i) for i in binary[-1:-10:-1]]))
    ogf = "".join(reversed([str(i) for i in binary[-11:-17:-1]]))
    ocf_code = binary_decimal_ocf(ocf)
    ogf_code = binary_hex_ogf_ocf(ogf)
    return ocf_code, ogf_code


def binary_hex_ogf_ocf(num):
    decimal_representation = int(num, 2)
    hexadecimal_string = hex(decimal_representation)
    return hexadecimal_string


def binary_decimal_ocf(num):
    decimal_representation = int(num, 2)
    return decimal_representation


def dec_to_hex_convert(data1):
    dec_array = [int(x, 16) for x in data1]
    hex_array = [hex(x) for x in dec_array]
    return hex_array


def packet_type():
    command_packet = 0x01
    Asynchronous_data_packet = 0x02
    Synchronous_data_packet = 0x03
    Event_packet = 0x04
    Extended_Command_packet = 0x09


def opcode(data):
    #OFFSET, SIZE_OCTETS = 2, 2
    #op_code = get_data(data, OFFSET, SIZE_OCTETS)
    op_code=["10","09"]
    op_data=dec_to_hex_convert(op_code)
    print(op_data)
    op_code = "{0}{1}".format(l[0][2], l[0][3])
    ogf, ocf = binary_hex_opcode(op_code)
    print("OCF", ocf, "|", "OGF", ogf)
    return ogf, ocf


def parameters_length(data):
    offset, size_octets = 4, 1
    data1 = get_data(data, offset, size_octets)
    hex_array=dec_to_hex_convert(data1)
    print(hex_array)
    print("parameter=", hex_array)


def get_data(data, offset, size_octets=None):
    if size_octets is not None:
        return data[offset:offset + size_octets]
    else:
        return data[offset:]


l = line_arrangement()
parameters_length(l[0])
print(l[0])
opcode(l[0])
