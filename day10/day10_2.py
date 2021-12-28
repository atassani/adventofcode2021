from functools import reduce
from operator import iconcat

is_prod = True

def synyax_scoring():
    lines = readfile()
    scores = []
    for line in lines:
        score = completion_score(line)
        if score != 0: scores.append(score)
    print(sorted(scores)[int(len(scores) / 2)])

def completion_score(line):
    closes = { '(': ')', '[': ']', '{': '}', '<': '>'}
    scores = { ')': 1, ']': 2, '}': 3, '>': 4 }
    stack = []
    for c in line:
        if c in closes.keys():
            stack.append(c)
        else:
            if stack == []: return c
            last_opening = stack.pop()
            if closes[last_opening] != c:
                return 0
    closing = []
    while stack != []:
        closing.append( closes[stack.pop()] )
    score = 0
    for c in closing:
        score = score * 5 + scores[c]
    return score

def readfile():
    filename = ('input.txt' if is_prod else 'sample.txt')
    lines = []
    with open(filename) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    return lines

if __name__ == "__main__":
    synyax_scoring()
