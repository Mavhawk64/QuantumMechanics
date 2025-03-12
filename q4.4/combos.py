from copy import deepcopy


def print_instset(st: list):
    for i in st:
        print(i[0][0] + i[1][0] + i[2][0] + " ", end="")
    print()
    for i in st:
        print(i[0][1] + i[1][1] + i[2][1] + " ", end="")


options = [["R", "R"], ["R", "G"], ["G", "R"], ["G", "G"]]
r122 = [
    [["R", None], [None, "R"], [None, "R"]],
    [["R", None], [None, "G"], [None, "G"]],
    [["G", None], [None, "R"], [None, "G"]],
    [["G", None], [None, "G"], [None, "R"]],
]
r212 = [
    [[None, "R"], ["R", None], [None, "R"]],
    [[None, "R"], ["G", None], [None, "G"]],
    [[None, "G"], ["R", None], [None, "G"]],
    [[None, "G"], ["G", None], [None, "R"]],
]
r221 = [
    [[None, "R"], [None, "R"], ["R", None]],
    [[None, "R"], [None, "G"], ["G", None]],
    [[None, "G"], [None, "R"], ["G", None]],
    [[None, "G"], [None, "G"], ["R", None]],
]

# For each of the none spots we have to find the combinations of R,G
o122 = []
for i in range(4):
    for x in ["R", "G"]:
        for y in ["R", "G"]:
            for z in ["R", "G"]:
                inst = deepcopy(r122[i])
                inst[0][1] = x
                inst[1][0] = y
                inst[2][0] = z
                if inst not in o122:
                    o122.append(inst)

o212 = []
for i in range(4):
    for x in ["R", "G"]:
        for y in ["R", "G"]:
            for z in ["R", "G"]:
                inst = deepcopy(r212[i])
                inst[0][0] = x
                inst[1][1] = y
                inst[2][0] = z
                if inst not in o212:
                    o212.append(inst)

o221 = []
for i in range(4):
    for x in ["R", "G"]:
        for y in ["R", "G"]:
            for z in ["R", "G"]:
                inst = deepcopy(r221[i])
                inst[0][0] = x
                inst[1][0] = y
                inst[2][1] = z
                if inst not in o221:
                    o221.append(inst)

o = []
for i in o122:
    if i in o212 and i in o221:
        o.append(i)

print_instset(o122)
print("\n")
print_instset(o212)
print("\n")
print_instset(o221)
print("\n")
print_instset(o)
