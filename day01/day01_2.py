is_prod = True

def countIncreasing():
    lines = readfile()
    triplets = [i+j+k for i,j,k in zip(lines[:-2], lines[1:-1], lines[2:])]
    result = [(i,j) for i,j in zip(triplets[:-1], triplets[1:]) if i<j]
    print(len(result))


def readfile():
    filename = ('input.txt' if is_prod else 'sample.txt')
    lines = []
    with open(filename) as file:
            lines = file.readlines()
            lines = [int(line.strip()) for line in lines]
    return lines

if __name__ == "__main__":
    countIncreasing()
