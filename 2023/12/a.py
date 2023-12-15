def get_int_char(springs: list[str], interested: str) -> list[list[int], list[int]]:
    ret = [[], []]
    cnt = 0
    for idx, char in enumerate(springs):
        if char == interested:
            cnt += 1
            ret[1].append(idx)
        elif cnt > 0:
            ret[0].append(cnt)
            cnt = 0
    if cnt > 0:
        ret[0].append(cnt)
    return ret

total_poss = 0
with open("input", "r") as inf:
    for line in inf:
        springs, blocks = line.rstrip().split(" ")
        springs = list(springs)
        blocks = list(map(int, blocks.split(",")))
        q_idxs = get_int_char(springs, "?")[1]
        oct_rl, oct_idxs = get_int_char(springs, "#")
        for val in range(pow(2, len(q_idxs))):
            if bin(val).count("1") + len(oct_idxs) != sum(blocks):
                continue
            else:
                lookup = f"{'0'*(len(q_idxs)-(len(bin(val))-2))}{bin(val)[2:]}"
                for idx, val in enumerate(lookup):
                    if val == "1":
                        springs[q_idxs[idx]] = "#"
                    else:
                        springs[q_idxs[idx]] = "?"
                if get_int_char(springs, "#")[0] == blocks:
                    total_poss += 1

print(total_poss)
