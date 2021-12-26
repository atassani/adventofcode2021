is_prod = True

def dumboOctopusesFlash():
    board = readfile()
    print_board(board)
    #input()
    total_flashes = 0
    for step in range(1, 100+1):
        flashes = process_step(board)
        total_flashes += len(flashes)
        print_board(board, step, flashes, total_flashes)
        #input()

def process_step(board):
    increase_one_all_board(board)
    flash_coords = get_flash_coords(board)
    total_flash_coords = flash_coords
    while len(flash_coords) > 0:
            flash_coords = flash_board(board, flash_coords)
            total_flash_coords.extend(flash_coords)
    flashed_to_zero(board)
    return total_flash_coords

def increase_one_all_board(board):
    for y in range(len(board)):
        for x in range(len(board[y])):
            board[y][x] += 1

def get_flash_coords(board):
    flashed_coords = []
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] > 9:
                flashed_coords.append( (x,y) )
    return flashed_coords

def flash_board(board, flash_coords):
    new_flashed = []
    for x, y in flash_coords:
        board[y][x] = -1
        surroundings = [ (x-1, y), (x-1, y-1), (x, y-1), (x+1, y-1), (x+1, y), (x+1, y+1), (x, y+1), (x-1, y+1) ]
        for coord in surroundings:
            new_flashed += increase_one_coord(board, *coord)
    return new_flashed

def increase_one_coord(board, x, y):
    flashed = []
    if x >= 0 and x < len(board[0]) and y >= 0 and y < len(board) and board[y][x]>0 and board[y][x]<10:
        board[y][x] += 1
        if board[y][x] > 9:
            board[y][x] = -1
            flashed = [(x, y)]
    return flashed

def flashed_to_zero(board):
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == -1:
                board[y][x] = 0

def print_board(board, step = 0, highlight = [], flashes=0):
    reset = '\033[0m'
    white = '\033[37;1m'
    cyan = '\033[36;1m'
    blue = '\033[44m'
    fgblue = '\033[34;1m'
    fgRed = '\033[31;1m'
    fgBrightRed = '\033[31;1m'

    flashed_step = []
    height = len(board)
    width = len(board[0])

    print(u"\u001b[2J") # clear
    print(f'{blue}{white}    0  1  2  3  4  5  6{reset} hl:{len(highlight)} fs:{len(flashed_step)}')
    for yi, y in enumerate(board):
        print(f'{blue}{white}{yi}:{reset} ', end='')
        for xi, x in enumerate(y):
            coord = (xi, yi)
            if coord in highlight:
                if x == 0:
                    print(f'{white} 0 {reset}', end='')
                else:
                    print(f'{fgblue} {x} {reset}', end='')
            else:
                if x == 10:
                    print(f'{fgBrightRed} 0 {reset}', end='')
                else:
                    print(f' {x} ', end='')
        print()
    print(f'[{width}x{height} S:{step} F:{cyan}{flashes}{reset}]')

def readfile():
    filename = ('input.txt' if is_prod else 'sample.txt')
    lines = []
    with open(filename) as file:
            lines = file.readlines()
            lines = [list(map(int, list(line.rstrip()))) for line in lines]
    return lines

if __name__ == "__main__":
    dumboOctopusesFlash()
