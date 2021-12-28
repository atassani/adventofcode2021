from functools import reduce
from operator import iconcat, mul

is_prod = True

def smoke_basin():
    mapa = readfile()
    lowpoints =[]
    for y in range(len(mapa)):
        for x in range(len(mapa[0])):
            if lower_than_neighbours(mapa, x, y):
                lowpoints.append( (x, y) )
                #print(f'({x},{y}): {mapa[y][x]}, risk={risk}')
    #print_mapa(mapa, lowpoints)
    basins = []
    for l in lowpoints:
        basins.append(recursive_find_basin(mapa, l, set()))
    three_largest_basins = sorted([len(b) for b in basins], reverse=True)[:3]
    print(three_largest_basins)
    print(reduce(mul, three_largest_basins))


def recursive_find_basin(mapa, point, basin):
    basin.add(point)
    adjacents = [ (0,1), (1,0), (0,-1), (-1,0) ]
    for a in adjacents:
        if valid_adjacent(mapa, basin, point[0]+a[0], point[1]+a[1]):
            recursive_find_basin(mapa, (point[0]+a[0], point[1]+a[1]), basin)
    return basin

def valid_adjacent(mapa, basin, x, y):
    return x>=0 and y>=0 and x<=len(mapa[0])-1 and y<=len(mapa)-1 and (x, y) not in basin and mapa[y][x]!=9

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
