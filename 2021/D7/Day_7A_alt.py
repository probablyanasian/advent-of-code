import statistics
positions = []
with open('D7_input.txt', 'r') as fopen:
    positions = [int(i) for i in fopen.readline().rstrip().split(',')]

def calc_diff(pos, num):
    diffs = [abs(i-num) for i in pos]
    return sum(diffs)

vals = [calc_diff(positions, num) for num in range(2000)]

print(min(vals))
print(vals.index(min(vals)))