def aoc_hash(inp: str) -> int:
    val = 0
    for s in inp:
        val += ord(s)
        val *= 17
        val %= 256
    return val

light_boxes: dict[int, list[str]] = {x: [] for x in range(256)}
with open("input", "r") as inf:
    for inp in inf.readline().rstrip().split(","):
        if "=" in inp:
            label, fl = inp.split("=")
            hash_val = aoc_hash(label)
            found = False
            for idx, lens in enumerate(light_boxes[hash_val]):
                if label == lens[0]:
                    light_boxes[hash_val][idx] = (label, int(fl))
                    found = True
                    break
            if not found:
                light_boxes[hash_val].append((label, int(fl)))
        else:
            label = inp[:-1]
            hash_val = aoc_hash(label)
            for idx, lens in enumerate(light_boxes[hash_val]):
                if label == lens[0]:
                    light_boxes[hash_val].remove(lens)

total_score = 0        
for box_num in light_boxes:
    for idx, lens in enumerate(light_boxes[box_num]):
        total_score += (box_num+1)*(idx+1)*lens[1]

print(total_score)