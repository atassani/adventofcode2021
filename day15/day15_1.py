from queue import PriorityQueue

is_prod = True

# Applying Dijkstra's algorithm, explained if __name__ == '__main__':
# https://stackabuse.com/dijkstras-algorithm-in-python/

def readfile():
    filename = ('input.txt' if is_prod else 'sample.txt')
    with open(filename) as file:
        mapa = [ [int(i) for i in list(line.rstrip())] for line in file.readlines()]
    return mapa

def print_mapa(mapa, path = []):
    clear = u"\u001b[2J"
    reset = '\033[0m'
    white = '\033[37;1m'
    blue = '\033[37;44m'

    print(f'{clear}')
    print(f'{blue}   ', end='')
    for x in range(len(mapa[0])):
        print(f'{x :3}', end='')
    print(f'{reset}')
    for y1, y in enumerate(mapa):
        print(f'{blue}{y1 :2}{reset} ', end='')
        for x1, x in enumerate(y):
            color = white if (x1,y1) in path else ''
            value = mapa[y1][x1] if mapa[y1][x1] != float('inf') else '∞'
            print(f'{color}{value :3}{reset}', end='')
        print()
    print()

def neighbours(mapa, current_vertex, visited):
    directions = [ (0,1), (1,0), (0,-1), (-1,0) ]
    px, py = current_vertex[0], current_vertex[1]
    neighs = []
    for dir in directions:
        x, y = px + dir[0], py + dir[1]
        if x>=0 and x<len(mapa[0]) and y>=0 and y<len(mapa) and (x, y) not in visited:
            neighs.append( (x, y) )
    return neighs

def dijkstra(mapa, start_vertex):
    sx,sy = start_vertex[0], start_vertex[1]
    visited = set()
    nodes=[[float('inf') for x in range(len(mapa[0]))] for y in range(len(mapa))]
    nodes[sy][sx] = 0
    pq = PriorityQueue()
    pq.put( (0, (sx,sy)) )
    while not pq.empty():
        (dist, current_vertex) = pq.get()
        visited.add(current_vertex)
        for neighbour in neighbours(mapa, current_vertex, visited):
            nx, ny = neighbour[0], neighbour[1]
            cx, cy = current_vertex[0], current_vertex[1]
            new_cost = nodes[cy][cx] + mapa[ny][nx]
            if nodes[ny][nx] > new_cost:
                nodes[ny][nx] = new_cost
                pq.put( (new_cost, neighbour) )
    return nodes

mapa = readfile()
nodes = dijkstra(mapa, (0,0))
#print_mapa(nodes)
end_vertex = (len(mapa[0])-1, len(mapa)-1)
ex, ey = end_vertex[0], end_vertex[1]
print(f'Cost of {end_vertex} is {nodes[ey][ex]}')
