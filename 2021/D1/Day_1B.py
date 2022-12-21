file = [int(i) for i in open("D1_input.txt")]
tot = len([1 for i in range(len(file)-2) if sum(file[i+1:i+4]) > sum(file[i:i+3])])
print(tot)
