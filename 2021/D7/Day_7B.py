import statistics
positions = []
with open('D7_input.txt', 'r') as fopen:
    positions = [int(i) for i in fopen.readline().rstrip().split(',')]

def fuel_burn(moved):
    return int((moved*(moved+1))/2)

def calc_diff(pos, num):
    diffs = [fuel_burn(abs(i-num)) for i in pos]
    return sum(diffs)

med = int(statistics.mean(positions))

print(med)
print(calc_diff(positions, med))
