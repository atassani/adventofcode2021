from functools import reduce
from operator import iconcat

is_prod = True

def smoke_basin():
    mapa = readfile()
    risk = 0
    lowpoints =[]
    for y in range(len(mapa)):
        for x in range(len(mapa[0])):
            if lower_than_neighbours(mapa, x, y):
                lowpoints.append( (x, y) )
                risk += mapa[y][x] + 1
                #print(f'({x},{y}): {mapa[y][x]}, risk={risk}')
    print_mapa(mapa, lowpoints)
    print(risk)

def print_mapa(mapa, lowpoints):
    reset = '\033[0m'
    white = '\033[37;1m'
    clear = u"\u001b[2J"
    print(f'{clear}')
    for y1, y in enumerate(mapa):
        for x1, x in enumerate(y):
            if (x1, y1) in lowpoints:
                color = white
            else:
                color = ''
            print(f'{color}{mapa[y1][x1]}{reset}', end='')
        print()

def lower_than_neighbours(mapa, x, y):
    current = mapa[y][x]
    adjacents = [ (0,1), (1,0), (0,-1), (-1,0) ]
    for a in adjacents:
        if value_greater_than_current(mapa, current, x+a[0], y+a[1]):
            return False
    return True

def value_greater_than_current(mapa, current, x, y):
    if x>=0 and y>=0 and x<=len(mapa[0])-1 and y<=len(mapa)-1 and mapa[y][x]<=current:
        return True
    else:
        return False

def readfile():
    filename = ('input.txt' if is_prod else 'sample.txt')
    lines = []
    with open(filename) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
        mapa = [list(map(int, list(l))) for l in lines]
    return mapa

if __name__ == "__main__":
    smoke_basin()
