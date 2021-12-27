from functools import reduce
from operator import iconcat

is_prod = True

def seven_segment_display():
    segments = readfile()
    outputs = [ i[1] for i in segments]
    output_flattened = reduce(iconcat, outputs, [])
    output1478 = [i for i in output_flattened if len(i) in [2, 4, 3, 7]]
    print(len(output1478))

def readfile():
    filename = ('input.txt' if is_prod else 'sample.txt')
    lines = []
    with open(filename) as file:
        lines = file.readlines()
        lines = [line.rstrip().split(' | ') for line in lines]
        segments = []
        for l in lines:
            segments.append([l[0].split(' '), l[1].split(' ')])
    return segments

if __name__ == "__main__":
    seven_segment_display()
