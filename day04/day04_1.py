is_prod = True

def bingo():
    random_numbers, boards = readfile()
    i = 0
    winner = -1
    while winner==-1 and i<len(random_numbers):
        num=random_numbers[i]
        mark_number(boards, num)
        if not is_prod:
            print_boards(boards)
        winner = find_winner(boards)
        i+=1
    unmarked = sum_unmarked_numbers(boards[winner])
    print(f'Score for board {winner} is {unmarked}*{random_numbers[i-1]}={unmarked*random_numbers[i-1]}')

def sum_unmarked_numbers(board):
    sum=0
    for r in board:
        for i in r:
            sum += i.value if not i.marked else 0
    return sum
def find_winner(boards):
    for b in range(len(boards)):
        if is_winning_row(boards[b]) or is_winning_column(boards[b]):
            return b
    return -1

def is_winning_row(board):
    for r in board:
        if all([e.marked for e in r]):
            return True
    return False

def is_winning_column(board):
    tboard = list(zip(*board))
    for c in tboard:
        if all([e.marked for e in c]):
            return True
    return False

def mark_number(boards, num):
    for board in boards:
        for row in board:
            for e in row:
                if e.value == num:
                    e.marked=True

def print_boards(boards):
    reset = '\033[0m'
    white = '\033[37;1m'
    clear = u"\u001b[2J"

    print(clear)
    for y in range(len(boards[0])):
        for b in range(len(boards)):
            for x in range(len(boards[0][0])):
                color = white if boards[b][y][x].marked else ''
                print(f"{color}{'{:3}'.format(boards[b][y][x].value)}{reset}", end='')
            print('       ', end='')
        print()
    print()

class Cell:
    value = 0
    marked = False
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return self.value

def readfile():
    filename = ('input.txt' if is_prod else 'sample.txt')
    lines = []
    with open(filename) as file:
            lines = file.readlines()
            lines = [line.rstrip() for line in lines]
    random_numbers = list(map(int, lines[0].split(',')))
    blocks=[]
    block=[]
    for l in lines[2:]:
        if l=='':
            blocks.append(block)
            block=[]
        else:
            block.append(l)
    blocks.append(block)
    boards=[]
    for block in blocks:
        board=[]
        for l in block:
            ll = [ Cell(int(i)) for i in l.replace('  ', ' ').lstrip(' ').split(' ')]
            board.append(ll)
        boards.append(board)
    return random_numbers, boards

if __name__ == "__main__":
    bingo()
