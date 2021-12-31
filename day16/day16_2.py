"""
Day 16. Packet Decoder
"""
from operator import mul
from functools import reduce

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
    return binnumber, int(literal, 2)

def read_packet(binnumber):
    version_sum = 0
    value = 0
    binnumber, version, type = read_header(binnumber)
    version_sum += version
    #print(f'version_sum={version_sum}')
    if type == 4:
        binnumber, literal = process_literal(binnumber)
        value = literal
    else:
        binnumber, length_type_id = read(binnumber, 1)
        #print(f'Operator packet {binnumber}, type={length_type_id}, ', end='')
        subvalues = []
        if length_type_id == '0':
            binnumber, spl  =read(binnumber, 15)
            subpackets_length = int(spl, 2)
            #print(f'subpacket length={subpackets_length}')
            binnumber, subpacket = read(binnumber, subpackets_length)
            while len(subpacket) != 0:
                #print(f'subpacket {subpacket}')
                subpacket, version, subvalue = read_packet(subpacket)
                version_sum += version
                subvalues.append(subvalue)
        else:
            number_of_subpackets = int(binnumber[:11], 2)
            #print(f'number of subpackets={number_of_subpackets}')
            binnumber = binnumber[11:]
            for _ in range(number_of_subpackets):
                #print(f'subpacket {binnumber}')
                binnumber, version, subvalue = read_packet(binnumber)
                version_sum += version
                subvalues.append(subvalue)
        if type == 0:
            value = sum(subvalues)
        if type == 1:
            value = reduce(mul, subvalues, 1)
        if type == 2:
            value = min(subvalues)
        if type == 3:
            value = max(subvalues)
        if type == 5:
            value = 1 if subvalues[0] > subvalues[1] else 0
        if type == 6:
            value = 1 if subvalues[0] < subvalues[1] else 0
        if type == 7:
            value = 1 if subvalues[0] == subvalues[1] else 0

    return binnumber, version_sum, value


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
    binnumber, version_sum, value = read_packet(binnumber)
    print(f'Value {value} for {hexnumber}')
    print()

print('finds the sum of 1 and 2, resulting in the value 3.')
process_packet('C200B40A82')
print('finds the product of 6 and 9, resulting in the value 54.')
process_packet('04005AC33890')
print('finds the minimum of 7, 8, and 9, resulting in the value 7.')
process_packet('880086C3E88112')
print('finds the maximum of 7, 8, and 9, resulting in the value 9.')
process_packet('CE00C43D881120')
print('produces 1, because 5 is less than 15.')
process_packet('D8005AC2A8F0')
print('produces 0, because 5 is not greater than 15.')
process_packet('F600BC2D8F')
print('produces 0, because 5 is not equal to 15.')
process_packet('9C005AC2F8F0')
print('produces 1, because 1 + 3 = 2 * 2.')
process_packet('9C0141080250320F1802104A08')

hexnumber = readfile()
process_packet(hexnumber)
