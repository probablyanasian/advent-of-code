from collections import deque

class FF():
    def __init__(self, name, o):
        self.name = name
        self.state = False
        self.outputs = o
    
    def __repr__(self):
        return f"{self.state} -> {self.outputs}"

class Con():
    def __init__(self, name, o):
        self.name = name
        self.inputs = {}
        self.outputs = o
    
    def __repr__(self):
        return f"{self.inputs} -> {self.outputs}"
        
components = {}

with open("input", "r") as inf:
    for line in inf:
        f, t = line.rstrip().split(" -> ")
        if f[0] == "%":
            n_ff = FF(f[1:], t.split(", "))
            components[f[1:]] = n_ff
        elif f[0] == "&":
            n_c = Con(f[1:], t.split(", "))
            components[f[1:]] = n_c
        elif f == "broadcaster":
            components["broadcaster"] = t.split(", ")
        else:
            print(line, end="")

for comp in components:
    if type(components[comp]) == Con:
        for out in components[comp].outputs:
            if out in components and type(components[out]) == Con:
                components[out].inputs[comp] = False
    elif type(components[comp]) == FF:
        for out in components[comp].outputs:
            if out in components and type(components[out]) == Con:
                components[out].inputs[comp] = False
    else:
        for out in components[comp]:
            if out in components and type(components[out]) == Con:
                components[out].inputs[comp] = False

l_counter = 0
h_counter = 0
pulse_train = deque()
for _ in range(1000):
    pulse_train.append((False, "button", "broadcaster"))
    while pulse_train:
        p_type, p_from, p_to = pulse_train.popleft()
        if p_type:
            h_counter += 1
        else:
            l_counter += 1

        if p_to not in components:
            continue

        if p_to == "broadcaster":
            for out in components[p_to]:
                pulse_train.append((p_type, p_to, out))
            continue

        p_to = components[p_to]
        if type(p_to) == Con:
            p_to.inputs[p_from] = p_type
            out_val = True
            if all(p_to.inputs.values()):
                out_val = False
            for out in p_to.outputs:
                pulse_train.append((out_val, p_to.name, out))

        elif type(p_to) == FF: # for typehinting
            if not p_type:
                p_to.state = not p_to.state
                for out in p_to.outputs:
                    pulse_train.append((p_to.state, p_to.name, out))

print(h_counter)
print(l_counter)
print(h_counter*l_counter)
