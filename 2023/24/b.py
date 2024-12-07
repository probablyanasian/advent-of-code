import z3

hailstones = []
with open("input", "r") as inf:
    for line in inf:
        loc, velo = line.rstrip().split(" @ ")
        x, y, z = loc.split(", ")
        v_x, v_y, v_z = velo.split(", ")
        hailstones.append((int(x), int(y), int(z), int(v_x), int(v_y), int(v_z)))

x, y, z, v_x, v_y, v_z = z3.Reals("x y z v_x v_y v_z")

solver = z3.Solver()
for idx, hail in enumerate(hailstones):
    solver.add(x + v_x * z3.Real(f"t_{idx}") == hail[0] + hail[3] * z3.Real(f"t_{idx}"))
    solver.add(y + v_y * z3.Real(f"t_{idx}") == hail[1] + hail[4] * z3.Real(f"t_{idx}"))
    solver.add(z + v_z * z3.Real(f"t_{idx}") == hail[2] + hail[5] * z3.Real(f"t_{idx}"))

print(solver.check())
print("solved")
print(solver.model().evaluate(x+y+z))

# I hate this.