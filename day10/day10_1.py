from functools import reduce
from operator import iconcat

is_prod = True

def synyax_scoring():
    lines = readfile()
    scores = { ')': 3, ']': 57, '}': 1197, '>': 25137, '': 0 }
    total_score = 0
    for line in lines:
        char = first_illegal_character(line)
        total_score += scores[char]
    print(total_score)

def first_illegal_character(line):
    closes = { '(': ')', '[': ']', '{': '}', '<': '>'}
    stack = []
    for c in line:
        if c in closes.keys():
            stack.append(c)
        else:
            if stack == []: return c
            last_opening = stack.pop()
            if closes[last_opening] != c:
                return c
    return ''

def readfile():
    filename = ('input.txt' if is_prod else 'sample.txt')
    lines = []
    with open(filename) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    return lines

if __name__ == "__main__":
    synyax_scoring()
