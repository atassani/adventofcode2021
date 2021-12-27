from functools import reduce
from operator import iconcat

is_prod = True

def whale():
    positions = readfile()
    #print(positions)
    minp = min(positions)
    maxp = max(positions)
    bestcost = 99999999
    bestposi = 0
    centre = minp
    while centre <= maxp:
        cost = calculate_cost(positions, centre)
        if cost < bestcost:
            bestcost = cost
            bestposi = centre
        centre += 1
    print(f'Best centre is {bestposi} and cost is {bestcost}')

def calculate_cost(positions, centre):
    cost = 0
    for i in positions:
        cost += abs(i-centre)
    return cost

def readfile():
    filename = ('input.txt' if is_prod else 'sample.txt')
    lines = []
    with open(filename) as file:
        lines = file.readlines()
        lines = [line.rstrip().split(',') for line in lines][0]
        positions = list(map(int, lines))
    return positions

if __name__ == "__main__":
    whale()
