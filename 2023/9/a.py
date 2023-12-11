total = 0
with open("input", "r") as inf:
    for line in inf:
        resids = []
        seq = list(map(int, line.split()))
        resid = tuple(seq[idx]-seq[idx-1] for idx in range(1, len(seq)))
        resids.append(resid)
        while not all(map(lambda x: x == 0, resid)):
            resid = tuple(resid[idx]-resid[idx-1] for idx in range(1, len(resid)))
            resids.append(resid)
        
        addit = 0
        for r in resids[::-1]:
            addit += r[-1]
        total += seq[-1] + addit

print(total)