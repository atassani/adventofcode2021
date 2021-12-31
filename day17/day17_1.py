"""
Day 17: Trick shot.
"""
prod_input = 'target area: x=139..187, y=-148..-89'
test_input = 'target area: x=20..30, y=-10..-5'

#tx1, tx2, ty1, ty2 = 20, 30, -5, -10
tx1, tx2, ty1, ty2 = 139, 187, -89, -148

def max_height(init_vx, init_vy):
    px, py = 0, 0
    vx, vy = init_vx, init_vy
    max_height = 0
    while not beyond_target(px, py) and not in_target(px, py):
        px += vx
        py += vy
        if vx > 0:
            vx -= 1
        elif vx < 0:
            vx += 1
        vy -= 1
        max_height = max(max_height, py)
    if not in_target(px, py):
        max_height = -1
    return max_height

def beyond_target(px, py):
    return px > tx2 or py < ty2

def in_target(x, y):
    return x>=tx1 and x<=tx2 and y<=ty1 and y>=ty2

def find_max_height():
    # Brute force, could limit values
    mh = -1
    for vx in range(1000):
        for vy in range(1000):
            mh = max(mh, max_height(vx, vy))
    return mh

mh = find_max_height()
print(mh)
