from functools import cache

@cache
def arrang(springs: str, blocks: list[int]) -> int:
    if (len([s for s in springs if s != "."]) < sum(blocks)) or (springs.count("#") > sum(blocks)):
        return 0
    if sum(blocks) == 0:
        return 1
    if springs[0] == ".":
        return arrang(springs[1:], blocks) # ignore case
    if springs[0] == "#":
        if all(map(lambda x: x != ".", springs[:blocks[0]])):
            if len(springs) == blocks[0]:
                return 1
            if springs[blocks[0]] != "#":
                return arrang(springs[blocks[0] + 1:], blocks[1:])
        return 0 # not possible
    return arrang(springs[1:], blocks) + arrang("#" + springs[1:], blocks)

total_poss = 0
chkmrk = 0
with open("input", "r") as inf:
    for line in inf:
        chkmrk += 1
        springs, blocks = line.rstrip().split(" ")

        springs = "?".join([springs]*5)
        blocks = tuple(map(int, blocks.split(",")))*5
        total_poss += arrang(springs, blocks)

print(total_poss)
