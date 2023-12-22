def aoc_hash(inp: str) -> int:
    val = 0
    for s in inp:
        val += ord(s)
        val *= 17
        val %= 256
    return val

total_value = 0
with open("input", "r") as inf:
    for inp in inf.readline().rstrip().split(","):
        total_value += aoc_hash(inp)

print(total_value)