from functools import reduce
from operator import iconcat

is_prod = True

def hydrothermal_vents():
    coords = readfile()
    coords = [c for c in coords if c[0][0] == c[1][0] or c[0][1] == c[1][1]]
    xs = [p[0][0] for p in coords]
    xs.extend([p[1][0] for p in coords])
    ys = [p[0][1] for p in coords]
    ys.extend([p[1][1] for p in coords])
    maxx = max(xs)+1
    maxy = max(ys)+1
    board = [[0 for i in range(0,maxx)] for j in range(0,maxy)]
    apply_coordinates(board, coords)
    if not is_prod:
        print_board(board)
    flattened = reduce(iconcat, board, [])
    res = len([i for i in flattened if i>1])
    print(f'Number of items with 2 or more: {res}')

def apply_coordinates(board, coords):
    for c in coords:
        ori=c[0]
        end=c[1]
        x1,y1 = ori[0],ori[1]
        x2,y2 = end[0],end[1]
        x,y = x1, y1
        while x<=x2 and y<=y2:
            #print(f'({x1},{y1})->({x2},{y2}),({x},{y})')
            board[y][x]+=1
            if x1 != x2: x+=1
            if y1 != y2: y+=1

def print_board(board):
    for row in board:
        for i in row:
            print('.' if i==0 else str(i), end='')
        print()

def readfile():
    filename = ('input.txt' if is_prod else 'sample.txt')
    lines = []
    with open(filename) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
        lines = [list(map(lambda v: tuple(v.split(',')), l)) for l in [l.split(' -> ') for l in lines]]
        res = []
        for line in lines:
            l = []
            for pair in line:
                pair = tuple(map(int, pair))
                l.append(pair)
            res.append(sorted(l))
    return res

if __name__ == "__main__":
    hydrothermal_vents()
