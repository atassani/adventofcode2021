from collections import Counter
from time import perf_counter as pfc

# Inspired by https://www.reddit.com/r/adventofcode/comments/rfzq6f/2021_day_14_solutions/hoib78w/?utm_source=share&utm_medium=web2x&context=3

is_prod = True

def readfile():
    filename = ('input.txt' if is_prod else 'sample.txt')
    with open(filename) as file:
        template, insertions = file.read().split('\n\n')
        chars = Counter(template)
        template = Counter(a+b for a, b in zip(template, template[1:]))
        insertions = {x[:2]: x[6] for x in insertions.rstrip().split('\n')}
    return template, insertions, chars

def solve(old_temp, insertions, chars, steps):
    for _ in range(steps):
        new_temp = Counter()
        for (a,b), value in old_temp.items():
            insert              = insertions[a+b]
            new_temp[a+insert] += value
            new_temp[insert+b] += value
            chars[insert]      += value
        old_temp = new_temp
    return max(chars.values()) - min(chars.values())

start = pfc()
print(solve(*readfile(), 10))
print(solve(*readfile(), 40))
print(pfc()-start)
