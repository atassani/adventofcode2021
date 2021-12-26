is_prod = True

def dive():
    lines = readfile()
    x, y, aim = 0, 0, 0
    for l in lines:
        if l[0] == 'forward':
            x += int(l[1])
            y += aim * int(l[1])
        if l[0] == 'up': aim -= int(l[1])
        if l[0] == 'down': aim += int(l[1])
    print(f'x={x},y={y} resuls {x*y}')

def readfile():
    filename = ('input.txt' if is_prod else 'sample.txt')
    lines = []
    with open(filename) as file:
            lines = file.readlines()
            lines = [line.rstrip().split(' ') for line in lines]
    return lines

if __name__ == "__main__":
    dive()
