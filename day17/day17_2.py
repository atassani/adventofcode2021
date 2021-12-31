"""
Day 17: Trick shot.
"""
prod_input = 'target area: x=139..187, y=-148..-89'
test_input = 'target area: x=20..30, y=-10..-5'

#tx1, tx2, ty1, ty2 = 20, 30, -5, -10
tx1, tx2, ty1, ty2 = 139, 187, -89, -148

def reaches_target(init_vx, init_vy):
    px, py = 0, 0
    vx, vy = init_vx, init_vy
    while not beyond_target(px, py) and not in_target(px, py):
        px += vx
        py += vy
        if vx > 0:
            vx -= 1
        elif vx < 0:
            vx += 1
        vy -= 1
    if not in_target(px, py):
        return 0
    return 1

def beyond_target(px, py):
    return px > tx2 or py < ty2

def in_target(x, y):
    return x>=tx1 and x<=tx2 and y<=ty1 and y>=ty2

def number_of_hits():
    # Brute force, could limit values
    hits = 0
    for vx in range(1000):
        for vy in range(-1000,1000):
            hits += reaches_target(vx, vy)
    return hits

h = number_of_hits()
print(h)
