def get_vert_value(arr: list[str]) -> int:
    vert_poss = [1 for _ in range(len(arr[0]))]
    vert_poss[0] = 0 # default, unreachable
    for row in arr:
        for idx in range(1, len(arr[0])):
            if row[max((2*idx)-len(arr[0]), 0):idx] != row[2*idx-1:idx-1:-1]:
                vert_poss[idx] = 0
    
    # cheaper to loop than check twice at O(n) cost each
    for idx, val in enumerate(vert_poss):
        if val == 1:
            return idx
    return 0

def get_value(arr: list[str]) -> int:
    if value := get_vert_value(arr):
        return value
    else:
        rotate = list(arr[0])
        for line in arr[1:]:
            idx = 0
            for char in line:
                rotate[idx] += char
                idx += 1
        return get_vert_value(rotate)*100
    
total_value = 0
with open("input", "r") as inf:
    mirrors = []
    for line in inf:
        if line == "\n":
            total_value += get_value(mirrors)
            mirrors = []
            continue
        mirrors.append(line.rstrip())

total_value += get_value(mirrors)
print(total_value)
