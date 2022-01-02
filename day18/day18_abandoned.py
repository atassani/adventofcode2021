"""
Day 18. Snailfish
"""
import ast

is_prod = False

def readfile():
    filename = ('input.txt' if is_prod else 'sample.txt')
    with open(filename) as file:
        lists = [ ast.literal_eval(line.strip()) for line in file.readlines() ]
    return lists

def snail_sum(op1, op2):
    tmp = [op1, op2]
    action_done = False
    while action_done:
        action_done = False
        if pair nested in 4 pairs:
            explode leftmost pair
            action_done = True
        elif a number is >= 10:
            the leftmost number splits
            action_done = True

#lists = readfile()
lists = [ [1,2], [[3,4],5] ]
print(lists)
result_list = lists[0]
for l in lists[1:]:
    result_list = snail_sum(result_list, l)
print(result_list)
