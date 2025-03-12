from numpy import cos, pi


# expression: \left|\cos\left(a\right)+\cos\left(b\right)+\cos\left(c\right)-\cos\left(b+c-a\right)\right|
def f(a, b, c):
    return abs(cos(a) + cos(b) + cos(c) - cos(b + c - a))


vals = {"a": None, "b": None, "c": None, "f": 0}
for a in range(0, 360):
    for b in range(0, 360):
        for c in range(0, 360):
            v = f(a * pi / 180, b * pi / 180, c * pi / 180)
            if v > vals["f"]:
                vals["a"] = a
                vals["b"] = b
                vals["c"] = c
                vals["f"] = v
                print(vals)

print(vals)
