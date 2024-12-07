from math import lcm
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
rx_conj = ""

with open("input", "r") as inf:
    for line in inf:
        f, t = line.rstrip().split(" -> ")
        if f[0] == "%":
            n_ff = FF(f[1:], t.split(", "))
            components[f[1:]] = n_ff
        elif f[0] == "&":
            if t == "rx":
                rx_conj = f[1:]
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

pulse_train = deque()
rx_low = False
button_count = 0
lcm_list = {f_inps: 0 for f_inps in components[rx_conj].inputs}
# lcm_list = {t_inps: 0 for f_inps in components[rx_conj].inputs for s_inps in components[f_inps].inputs for t_inps in components[s_inps].inputs}
for _ in range(10_000):
    button_count += 1
    pulse_train.append((False, "button", "broadcaster"))
    while pulse_train:
        p_type, p_from, p_to = pulse_train.popleft()

        if p_to not in components:
            continue
            
        if p_to in lcm_list:
            if lcm_list[p_to] == 0 and not p_type and button_count > 5:
                    lcm_list[p_to] = button_count


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

print(lcm(*map(int, lcm_list.values())))
