fil = 'D9_input.txt'
#fil = 'test.txt'

with open(fil) as f:
    inp = [[int(i) for i in l] for l in f.read().strip().split('\n')]

ymax = len(inp)
xmax = len(inp[0])

def p2():

    field = set((x,y) for x in range(xmax) for y in range(ymax) if inp[y][x]<9)
    basins = []

    def basin(j0,k0):
        if (j0,k0) not in field:
            return 0
        field.remove((j0,k0))
        return 1 + sum(basin(j,k) for j,k in ((j0-1,k0), (j0+1,k0), (j0,k0-1), (j0,k0+1)))
        
    while field:
        x, y = field.pop()
        field.add((x,y))
        basins.append(basin(x,y))

    res = 1
    for v in sorted(basins)[-3:]:
        print(v)
        res *= v
    print(res)

p2()