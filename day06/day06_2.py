from functools import reduce
from operator import iconcat

is_prod = True

def lanternfish():
    dic = readfile()
    for day in range(256):
        pass_day(dic)
    print(sum(dic.values()))

def pass_day(dic):
    dic0 = dic[0]
    for i in range(0, 8):
        dic[i] = dic[i+1]
    dic[6] += dic0
    dic[8] = dic0

def readfile():
    filename = ('input.txt' if is_prod else 'sample.txt')
    lines = []
    with open(filename) as file:
        lines = file.readlines()
        lines = [line.rstrip().split(',') for line in lines][0]
        numbers = list(map(int, lines))
        numbers = sorted(numbers)
        dic = dict.fromkeys(list(range(9)), 0)
        for i in numbers:
            dic[i] += 1
    return dic

if __name__ == "__main__":
    lanternfish()
