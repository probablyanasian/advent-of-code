sum = 0

c = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

with open("input") as inf:
    for line in inf:
        nums = []
        for k in c:
            line = line.replace(k, k+c[k]+k)
        for s in line.rstrip():
            if s.isdigit():
                nums.append(s)
        sum += int(nums[0] + nums[-1])
        
print(sum)
