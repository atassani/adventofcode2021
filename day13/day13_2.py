from functools import reduce
from operator import iconcat

is_prod = True

def transparent_origami():
    points, folds = readfile()
    #print(points)
    #print(folds)
    mapa = build_map(points)
    #print_map(mapa)
    print()
    for fold in folds:
        mapa = do_fold(mapa, fold)
    print_map(mapa)

def do_fold(mapa, fold):
    if fold[0] == 'y':
        y = fold[1]
        for y1 in range(y+1, len(mapa)):
            for x in range(len(mapa[0])):
                new = mapa[y1][x]
                if new == '#':
                    mapa[y - (y1-y)][x] = new
        mapa = mapa[:y]
    if fold[0] == 'x':
        x = fold[1]
        for y in range(len(mapa)):
            for x1 in range(len(mapa[0])):
                new = mapa[y][x1]
                if new == '#':
                    mapa[y][x - (x1-x)] = new
        mapa = [row[:x] for row in mapa]
    return mapa

def build_map(points):
    maxx = max([p[0] for p in points])
    maxy = max([p[1] for p in points])
    mapa = [ list('.' * (maxx+1)) for y in range(maxy+1)]
    for p in points:
        mapa[int(p[1])][int(p[0])] = '#'
    return mapa

def print_map(mapa):
    for row in mapa:
        for v in row:
            print(v, end='')
        print()

def readfile():
    filename = ('input.txt' if is_prod else 'sample.txt')
    with open(filename) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
        i = 0
        points = []
        while lines[i] != '':
            point = lines[i].split(',')
            points.append( (int(point[0]), int(point[1])) )
            i += 1
        i +=1
        folds = []
        for line in lines[i:]:
            line = line.replace('fold along ', '')
            fold = line.split('=')
            folds.append( ( fold[0], int(fold[1]) ) )
    return points, folds

if __name__ == '__main__':
    transparent_origami()
