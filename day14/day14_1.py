from collections import Counter

is_prod = True

def polymerization():
    template, rules = readfile()
    polymer = template
    for i in range(10):
        polymer = polymerase(rules, polymer)
        print(f'{i:2}: {len(polymer)}')
    counter=Counter(polymer)
    most_common = counter.most_common()[0][1]
    least_common = counter.most_common()[:-2:-1][0][1]
    print(most_common - least_common)

def polymerase(rules, polymer):
    pairs = list(zip(polymer[:-1], polymer[1:]))
    newpolymer = pairs[0][0]
    for p in pairs:
        pair = ''.join(p)
        newpolymer += rules[pair] + p[1]
    return newpolymer

def readfile():
    filename = ('input.txt' if is_prod else 'sample.txt')
    with open(filename) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
        template = lines[0]
        rules_list = [line.split(' -> ') for line in lines[2:]]
        rules = {r[0]: r[1] for r in rules_list}
    return template, rules

if __name__ == '__main__':
    polymerization()
