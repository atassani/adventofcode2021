is_prod = True

def binary_power_consumption():
    lines = readfile()
    ones = [0] * len(lines[0])
    zeros = [0] * len(lines[0])
    for line in lines:
        for i in range(len(line)):
            ones[i] += int(line[i])
            zeros[i] += 1 if line[i]=='0' else 0
    gamma_rate = []
    epsilon_rate = []
    for i, one in enumerate(ones):
        if one > zeros[i]:
            gamma_rate.append('1')
            epsilon_rate.append('0')
        else:
            gamma_rate.append('0')
            epsilon_rate.append('1')
    gamma_rate_decimal=int(''.join(gamma_rate), 2)
    epsilon_rate_decimal=int(''.join(epsilon_rate), 2)
    print(f"gamma rate= {gamma_rate_decimal}, epsilon rate= {epsilon_rate_decimal}")
    print(f"power consumption={gamma_rate_decimal * epsilon_rate_decimal}")

    # power consumption = gamma rate * epsilon rate
    # gamma rate -> most commont bit
    # epsilon rate -> least common bit
    #

def readfile():
    filename = ('input.txt' if is_prod else 'sample.txt')
    lines = []
    with open(filename) as file:
            lines = file.readlines()
            lines = [line.rstrip() for line in lines]
    return lines

if __name__ == "__main__":
    binary_power_consumption()
