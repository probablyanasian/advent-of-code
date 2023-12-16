from functools import cache

platform = []
with open("input", "r") as inf:
    for line in inf:
        platform.append(list(line.rstrip()))


def pretty_print(cur):
    for line in cur:
        print("".join(line))
    print("")


def score(ser_arr: str, r_len: int):
    arr = [
        [x for x in ser_arr[r * r_len : (r + 1) * r_len]]
        for r in range(len(ser_arr) // r_len)
    ]
    score = 0
    for row, val in enumerate(arr):
        for c in val:
            if c == "O":
                score += len(ser_arr) // r_len - row
    return score


# we brute forcing this...
def do_north(arr):
    for idx in range(len(arr[0])):
        hold = 0
        for row, val in enumerate(arr):
            if val[idx] == "O":
                arr[row][idx] = "."
                arr[hold][idx] = "O"
                hold += 1
            elif val[idx] == "#":
                hold = row + 1
    return arr


def do_west(arr):
    for row, val in enumerate(arr):
        hold = 0
        for idx in range(len(arr[0])):
            if val[idx] == "O":
                arr[row][idx] = "."
                arr[row][hold] = "O"
                hold += 1
            elif val[idx] == "#":
                hold = idx + 1
    return arr


def do_south(arr):
    for idx in range(len(arr[0])):
        hold = len(arr) - 1
        for row, val in enumerate(arr[::-1]):
            if val[idx] == "O":
                arr[len(arr) - row - 1][idx] = "."
                arr[hold][idx] = "O"
                hold -= 1
            elif val[idx] == "#":
                hold = len(arr) - row - 2
    return arr


def do_east(arr):
    for row, val in enumerate(arr):
        hold = len(arr[0]) - 1
        for idx in range(len(arr[0]) - 1, -1, -1):
            if val[idx] == "O":
                arr[row][idx] = "."
                arr[row][hold] = "O"
                hold -= 1
            elif val[idx] == "#":
                hold = idx - 1
    return arr


@cache
def do_cycle(ser_arr: str, r_len: int):
    ordering = [do_north, do_west, do_south, do_east]
    arr = [
        [x for x in ser_arr[r * r_len : (r + 1) * r_len]]
        for r in range(len(ser_arr) // r_len)
    ]
    for f in ordering:
        f(arr)
    return "".join([x for r in arr for x in r])


arr = "".join([x for r in platform for x in r])
seen = set()
idx_lookup = {}
for i in range(1_000_000_000):
    arr = do_cycle(arr, len(platform[0]))
    if arr not in seen:
        seen.add(arr)
        idx_lookup[arr] = i
    else:
        break

equiv_cycs = (1_000_000_000 % (i - idx_lookup[arr])) + i-idx_lookup[arr]
arr = "".join([x for r in platform for x in r])
for i in range(equiv_cycs):
    arr = do_cycle(arr, len(platform[0]))
    
print(score(arr, len(platform[0])))