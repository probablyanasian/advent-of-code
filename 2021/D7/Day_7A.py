import statistics
positions = []
with open('D7_input.txt', 'r') as fopen:
    positions = [int(i) for i in fopen.readline().rstrip().split(',')]

def calc_diff(pos, num):
    diffs = [abs(i-num) for i in pos]
    return sum(diffs)

med = int(statistics.median(positions))

print(med)
print(calc_diff(positions, med))
