sum = 0

with open("input") as inf:
    for line in inf:
        nums = [s for s in line if s.isdigit()]
        sum += int(nums[0] + nums[-1])
        
print(sum)
