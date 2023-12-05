import itertools

schema = []
with open("input") as inf:
    schema.extend(line.rstrip() for line in inf)

bound_x = lambda x: 0 if x < 0 else len(schema[0])-1 if x > len(schema[0])-1 else x 
bound_y = lambda y: 0 if y < 0 else len(schema)-1 if y > len(schema)-1 else y 

movement = list(itertools.product((-1, 0, 1), repeat=2))
movement.remove((0, 0))

total = 0
matched = set()
for y, line in enumerate(schema):
    for x, char in enumerate(line):
        if char == '*':
            res_map = [[" " for _ in range(11)] for _ in range(3)] # create a subset mapping for each gear
            to_search = [(x, y)]
            while to_search:
                s_x, s_y = to_search.pop(0)
                for move in movement:
                    ns_x = bound_x(s_x+move[0])
                    ns_y = bound_y(s_y+move[1])
                    if (ns_x, ns_y) in matched or (ns_x == s_x and ns_y == s_y):
                        continue
                    if schema[ns_y][ns_x].isdigit():
                        # use offset to center on res_map
                        res_map[ns_y-y+1][ns_x-x+5] = schema[ns_y][ns_x] 
                        matched.add((ns_x, ns_y))
                        to_search.append((ns_x, ns_y))
            gear_nums = [int(val) for l in ["".join(row) for row in res_map] for val in l.split()]
            if len(gear_nums) == 2:
                total += gear_nums[0]*gear_nums[1]

print(total)