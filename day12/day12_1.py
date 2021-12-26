is_prod = True

def passagePathing():
    dic = readfile()
    results = find_possible_routes(dic, 'start', ['start'])
    results = [','.join(i) for i in results]
    for i in list(sorted(results)):
        print(i)
    print(f'There are {len(results)} different paths')

def find_possible_routes(dic, origin, route):
    result = []
    for elem in dic[origin]:
        explore_route(dic, elem, route.copy(), result)
    return result

def explore_route(dic, elem, route, routes):
    if elem=='end' or elem == elem.upper() or elem not in route:
        route.append(elem)
        if elem != 'end':
            for item in dic[elem]:
                explore_route(dic, item, route.copy(), routes)
        else:
            routes.append(route)

def readfile():
    filename = ('input.txt' if is_prod else 'sample.txt')
    dic = dict()
    with open(filename) as file:
            lines = file.readlines()
            lines = [line.rstrip().split('-') for line in lines]
            for origin, end in lines:
                if origin in dic:
                    dic[origin].append(end)
                else:
                    dic[origin] = [end]
                if origin != 'start' and end != 'end':
                    if end in dic:
                        dic[end].append(origin)
                    else:
                        dic[end] = [origin]
    return dic

if __name__ == "__main__":
    passagePathing()
