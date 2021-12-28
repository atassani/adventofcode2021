from functools import reduce
from operator import iconcat

is_prod = True

def seven_segment_display():
    segments = readfile()
    res = 0
    for line in segments:
        dic = identify_numbers(line[0])
        res += decode_number(dic, line[1])
    print(res)

def identify_numbers(inputs):
    dic = dict()
    dicfromnum = dict()
    identify_nums1478(dic, dicfromnum, inputs)
    identify_num069(dic, dicfromnum, inputs)
    identify_num235(dic, dicfromnum, inputs)
    #print({key:dicfromnum[key] for key in sorted(dicfromnum)})
    return dic

def identify_num235(dic, dicfromnum, inputs):
    num3 = [i for i in inputs if len(i)==5 and len(set(dicfromnum[1]) - set(i)) == 0][0]
    num5 = [i for i in inputs if len(i)==5 and i != num3 and len(set(dicfromnum[9]) - set(i)) == 1 ][0]
    num2 = [i for i in inputs if len(i)==5 and i not in [num3, num5]][0]
    dic[num3] = 3
    dic[num5] = 5
    dic[num2] = 2
    dicfromnum[3] = num3
    dicfromnum[5] = num5
    dicfromnum[2] = num2

def identify_num069(dic, dicfromnum, inputs):
    num4minus1 = ''.join([i for i in list(dicfromnum[4]) if i not in list(dicfromnum[1])])
    num0 = [i for i in inputs if len(i)==6 and len(set(num4minus1) - set(i)) != 0][0]
    num6 = [i for i in inputs if len(i)==6 and i != num0 and len(set(dicfromnum[1]) - set(i)) != 0][0]
    num9 = [i for i in inputs if len(i)==6 and i not in [num0, num6]][0]
    dic[num0] = 0
    dic[num6] = 6
    dic[num9] = 9
    dicfromnum[0] = num0
    dicfromnum[6] = num6
    dicfromnum[9] = num9

def identify_nums1478(dic, dicfromnum, inputs):
    num1 = [i for i in inputs if len(i)==2][0]
    num4 = [i for i in inputs if len(i)==4][0]
    num7 = [i for i in inputs if len(i)==3][0]
    num8 = [i for i in inputs if len(i)==7][0]
    dic[num1] = 1
    dic[num4] = 4
    dic[num7] = 7
    dic[num8] = 8
    dicfromnum[1] = num1
    dicfromnum[4] = num4
    dicfromnum[7] = num7
    dicfromnum[8] = num8

def decode_number(dic, outputs):
    num = ''
    for i in outputs:
        num += str(dic[i])
    return int(num)

def readfile():
    filename = ('input.txt' if is_prod else 'sample.txt')
    lines = []
    with open(filename) as file:
        lines = file.readlines()
        lines = [line.rstrip().split(' | ') for line in lines]
        segments = []
        for l in lines:
            inputs = [''.join(sorted(i)) for i in l[0].split(' ')]
            outputs = [''.join(sorted(i)) for i in l[1].split(' ')]
            segments.append([inputs, outputs])
    return segments

if __name__ == "__main__":
    seven_segment_display()
