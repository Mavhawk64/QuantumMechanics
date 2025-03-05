import sympy as sp


def cstr(i):
    if i == 0:
        return '0'
    if i == 1:
        return '1'
    if i == -1j:
        return '-i'


a, b, c, d, e, f, g, h = sp.symbols('a b c d e f g h')  # can be complex

# a = 1 - |b|^2
a = 1 - abs(b)**2
d = -a
# c = complex conjugate of b
c = b.conjugate()

# Similarly for efgh
e = 1 - abs(f)**2
h = -e
g = f.conjugate()

A = sp.Matrix([[a, b], [c, d]])
B = sp.Matrix([[e, f], [g, h]])

# tensor product of A and B
AB = sp.Matrix([[a*e, a*f, b*e, b*f], [a*g, a*h, b*g, b*h],
               [c*e, c*f, d*e, d*f], [c*g, c*h, d*g, d*h]])

# AB act on -1/sqrt2 [[0], [1], [-1], [0]]
n_psi_epr = sp.Matrix([[0], [1], [-1], [0]])

res = AB * n_psi_epr
# print(sp.latex(res))

n_psi_epr_dagger = n_psi_epr.conjugate().transpose()

res = n_psi_epr_dagger * res

# should be constant, so
res = res[0].simplify() / 2

# print(sp.latex(res))

print("Case 1: f = b")
print("b = 0")
print(sp.latex(res.subs({f: b}).subs({b: 0}).simplify()))
print("b = 1")
print(sp.latex(res.subs({f: b}).subs({b: 1}).simplify()))
print("b = -i")
print(sp.latex(res.subs({f: b}).subs({b: -1j}).simplify()))
print("Case 2: f != b")
bs = [0, 1, -1j]
for i in bs:
    for j in bs:
        if i == j:
            continue
        print(f"b = {cstr(i)}, f = {cstr(j)}")
        print(sp.latex(res.subs({f: i}).subs({b: j}).simplify()))
