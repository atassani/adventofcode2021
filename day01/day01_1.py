is_prod = True

def countIncreasing():
    lines = readfile()
    result = [(i,j) for i,j in zip(lines[:-1], lines[1:]) if i<j]
    print(len(result))

def readfile():
    filename = ('input.txt' if is_prod else 'sample.txt')
    lines = []
    with open(filename) as file:
            lines = file.readlines()
            lines = [int(line.rstrip()) for line in lines]
    return lines

if __name__ == "__main__":
    countIncreasing()
