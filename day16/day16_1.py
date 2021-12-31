"""
Day 16. Packet Decoder
"""
def readfile():
    with open('input.txt') as file:
        lines = [ line.strip() for line in file.readlines()]
    return lines[0]

def process_literal(binnumber):
    original = binnumber
    #print(f'Literal packet {binnumber}, ', end='')
    literal = ''
    binnumber, firstbit = read(binnumber, 1)
    while firstbit != '0':
        binnumber, portion = read(binnumber, 4)
        literal += portion
        binnumber, firstbit = read(binnumber, 1)
    binnumber, portion = read(binnumber, 4)
    literal += portion
    #print(f'value: {literal} = {int(literal, 2)}')
    return binnumber, literal

def read_packet(binnumber):
    version_sum = 0
    binnumber, version, type = read_header(binnumber)
    version_sum += version
    #print(f'version_sum={version_sum}')
    if type == 4:
        binnumber, literal = process_literal(binnumber)
    else:
        binnumber, length_type_id = read(binnumber, 1)
        #print(f'Operator packet {binnumber}, type={length_type_id}, ', end='')
        if length_type_id == '0':
            binnumber, value  =read(binnumber, 15)
            subpackets_length = int(value, 2)
            #print(f'subpacket length={subpackets_length}')
            binnumber, subpacket = read(binnumber, subpackets_length)
            while len(subpacket) != 0:
                #print(f'subpacket {subpacket}')
                subpacket, version = read_packet(subpacket)
                version_sum += version
        else:
            number_of_subpackets = int(binnumber[:11], 2)
            #print(f'number of subpackets={number_of_subpackets}')
            binnumber = binnumber[11:]
            for _ in range(number_of_subpackets):
                #print(f'subpacket {binnumber}')
                binnumber, version = read_packet(binnumber)
                version_sum += version
    return binnumber, version_sum


def read_header(binnumber):
    version, type = int(binnumber[:3], 2), int(binnumber[3:6], 2)
    binnumber = binnumber[6:]
    return binnumber, version, type

def read(string, length):
    value = string[:length]
    string = string[length:]
    return string, value

def process_packet(hexnumber):
    binnumber = ('{0:04b}'.format(int(hexnumber, 16))).zfill(len(hexnumber) * 4)
    #print(f'{hexnumber}: {binnumber}')
    binnumber, version_sum = read_packet(binnumber)
    print(f'Version num {version_sum} for {hexnumber}')
    print()

hexnumber = readfile()
process_packet(hexnumber)
#process_packet('D2FE28')
#process_packet('38006F45291200')
#process_packet('EE00D40C823060')
#process_packet('8A004A801A8002F478')
#process_packet('620080001611562C8802118E34')
#process_packet('C0015000016115A2E0802F182340')
#process_packet('A0016C880162017C3686B18A3D4780')
