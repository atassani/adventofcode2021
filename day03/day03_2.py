is_prod = True

def binary_life_support():
    lines = readfile()
    i=0
    oxygen_lines=lines
    while (len(oxygen_lines) > 1):
        ones, zeros = 0, 0
        for line in oxygen_lines:
            ones += int(line[i])
            zeros += 1 if line[i]=='0' else 0
        most_freq = '1' if ones >= zeros else '0'
        oxygen_lines = [line for line in oxygen_lines if line[i]==most_freq]
        i += 1
    oxygen=int(oxygen_lines[0],2)

    i=0
    co2_lines=lines
    while (len(co2_lines) > 1):
        ones, zeros = 0, 0
        for line in co2_lines:
            ones += int(line[i])
            zeros += 1 if line[i]=='0' else 0
        least_freq = '1' if ones < zeros else '0'
        co2_lines = [line for line in co2_lines if line[i]==least_freq]
        i += 1
    co2=int(co2_lines[0],2)

    print(f'oxygen:{oxygen}, co2:{co2}, life support: {oxygen*co2}')

def readfile():
    filename = ('input.txt' if is_prod else 'sample.txt')
    lines = []
    with open(filename) as file:
            lines = file.readlines()
            lines = [line.rstrip() for line in lines]
    return lines

if __name__ == "__main__":
    binary_life_support()
